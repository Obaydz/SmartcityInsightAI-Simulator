import asyncio
from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from simulator.models import (
    AccidentEvent,
    PresetRequest,
    RouteDelayRequest,
    RouteDelayResponse,
    TrafficSegment,
    TrafficSummary,
)
from simulator.traffic_engine import TrafficEngine

# Instance singleton du moteur de circulation
engine = TrafficEngine()

# Ensemble des WebSockets connectés
connected_websockets: List[WebSocket] = []


async def simulation_loop():
    """Tâche d'arrière-plan simulant l'évolution dynamique du trafic et diffusant sur WebSocket."""
    while True:
        await asyncio.sleep(3.0)
        engine.tick()

        # Diffusion temps réel aux clients WebSocket
        if connected_websockets:
            summary = engine.get_summary().model_dump()
            dead_connections = []
            for ws in connected_websockets:
                try:
                    await ws.send_json({"event": "TRAFFIC_UPDATE", "summary": summary})
                except Exception:
                    dead_connections.append(ws)
            for dead in dead_connections:
                if dead in connected_websockets:
                    connected_websockets.remove(dead)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Démarrage de la boucle de simulation en arrière-plan
    sim_task = asyncio.create_task(simulation_loop())
    yield
    sim_task.cancel()


app = FastAPI(
    title="SmartCity Insight AI — Simulateur de Trafic (Cap Bon Nord-Est : Kélibia, Hammam El Ghezaz, El Haouaria)",
    description=(
        "API autonome de simulation de la circulation routière en temps réel pour le Cap Bon Nord-Est "
        "(Kélibia, Hammam El Ghezaz, El Haouaria, Dar Allouche, Kerkouane, Azmour, Menzel Horr). "
        "Remplace l'API Google Maps Traffic & Routes en fournissant la congestion des tronçons, "
        "le calcul dynamique des retards d'intervention d'urgence et la synchronisation avec les alertes d'accidents."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# Configuration CORS ouverte pour autoriser le frontend Vite React (5173) et Daphne (8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", summary="Console Web de Supervision du Simulateur")
async def serve_dashboard():
    return FileResponse("static/index.html")


@app.get("/health", summary="Vérification de l'état de santé du service")
async def health_check():
    return {
        "status": "online",
        "service": "smartcity-traffic-simulator",
        "city": "Cap Bon Nord-Est (Kélibia, Hammam El Ghezaz, El Haouaria), Tunisie",
        "preset": engine.preset_name,
    }


@app.get("/api/traffic/segments", response_model=List[TrafficSegment], summary="Liste des tronçons routiers et congestion")
async def get_traffic_segments():
    """Retourne la totalité des tronçons routiers avec coordonnées, vitesses et niveaux de congestion."""
    return list(engine.segments.values())


@app.get("/api/traffic/summary", response_model=TrafficSummary, summary="Synthèse régionale globale du trafic")
async def get_traffic_summary():
    """Retourne l'indice moyen, la vitesse moyenne et l'état global du trafic dans le Cap Bon Nord-Est."""
    return engine.get_summary()


@app.get("/api/traffic/zone-risk-data", summary="Indices de trafic par zone pour le modèle Risk Map (Random Forest)")
async def get_zone_risk_data():
    """Fournit les indices de congestion par zone pour alimenter le modèle ML de prédiction des accidents."""
    summary = engine.get_summary()
    return {
        "global_trafic_index": summary.average_congestion_index,
        "zone_indices": summary.zone_indices,
        "timestamp": summary.timestamp,
    }


@app.post("/api/traffic/route-delay", response_model=RouteDelayResponse, summary="Calcul du retard et durée avec trafic sur un trajet d'urgence")
async def calculate_route_delay(req: RouteDelayRequest):
    """
    Calcule le temps de trajet optimal d'une caserne de pompiers vers un accident
    en tenant compte de la congestion des tronçons routiers traversés.
    """
    return engine.calculate_route_delay(req)


@app.post("/api/traffic/events/accident", summary="Notifier un accident et créer un bouchon localisé")
async def notify_accident(event: AccidentEvent):
    """
    Reçoit un signalement d'accident (depuis le poste Protection Civile ou les signalements citoyens)
    et provoque un ralentissement sévère immédiat sur l'artère la plus proche.
    """
    engine.add_accident_incident(event)
    return {
        "message": f"Accident pris en compte. Ralentissement créé autour de ({event.latitude}, {event.longitude})",
        "active_incidents": len(engine.active_accidents),
    }


@app.post("/api/traffic/events/clear", summary="Lever les restrictions d'un accident résolu")
async def clear_accident(alerte_id: int = None):
    """Rétablit progressivement la circulation normale suite à la clôture de l'intervention."""
    engine.clear_accident_incident(alerte_id)
    return {
        "message": "Restrictions levées et circulation rétablie",
        "active_incidents": len(engine.active_accidents),
    }


@app.post("/api/simulation/preset", summary="Changer de scénario de trafic instantanément")
async def set_simulation_preset(req: PresetRequest):
    """Permet de basculer instantanément de scénario : FLUID, NORMAL, RUSH_HOUR_MORNING, RUSH_HOUR_EVENING, RAIN_STORM, GRIDLOCK."""
    engine.set_preset(req.preset)
    return {
        "message": f"Scénario {req.preset} appliqué avec succès",
        "summary": engine.get_summary(),
    }


@app.websocket("/ws/traffic")
async def websocket_traffic_endpoint(websocket: WebSocket):
    """Flux WebSocket diffusant les mises à jour de trafic en continu aux clients connectés."""
    await websocket.accept()
    connected_websockets.append(websocket)
    try:
        # Envoi immédiat de l'état actuel
        await websocket.send_json({
            "event": "INITIAL_TRAFFIC_STATE",
            "summary": engine.get_summary().model_dump(),
        })
        while True:
            # Maintenir la connexion active
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_text("pong")
    except WebSocketDisconnect:
        if websocket in connected_websockets:
            connected_websockets.remove(websocket)
    except Exception:
        if websocket in connected_websockets:
            connected_websockets.remove(websocket)
