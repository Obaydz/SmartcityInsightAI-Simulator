# 🚦 SmartCity Traffic Simulator — Cap Bon Nord-Est

Moteur de simulation autonome et dynamique de la circulation routière dans le **Cap Bon Nord-Est** (Gouvernorat de Nabeul : **Kélibia, Hammam El Ghezaz, El Haouaria** et leurs environs immédiats : **Dar Allouche, Kerkouane, Azmour, Menzel Horr**), conçu pour remplacer l'API Google Maps Traffic dans le cadre du projet **SmartCity Insight AI**.

---

## 🎯 Pourquoi ce projet séparé ?

1. **Remplacement de l'API Google Maps Traffic** : En l'absence de clé Google Maps avec accès aux données de trafic temps réel, ce simulateur modélise fidèlement **50 tronçons routiers** du Cap Bon Nord-Est (Kélibia Centre & Port/El Mansourah, RR27 Hammam El Ghezaz, route côtière Kerkouane–Dar Allouche, RR27 Nord vers El Haouaria, Les Grottes, Sidi Daoud / Zaouiet El Mgaïez, route d'Azmour et axe MC27 Menzel Horr–Kélibia).
2. **Couche de Trafic Leaflet** : Fournit les coordonnées géodésiques, vitesses et niveaux de congestion (Vert `#10b981`, Orange `#f59e0b`, Rouge `#ef4444`, Bloqué `#991b1b`) pour affichage cartographique interactif dans `smartcity-insight-ai`.
3. **Calcul de Retard Réel d'Intervention** : Remplace l'ancien délai statique de 2 minutes par un calcul d'itinéraire tenant compte des tronçons réellement traversés par les ambulances ou camions de la Protection Civile.
4. **Alimentation du Modèle IA Risk Map (Random Forest)** : Expose l'indice moyen de trafic par zone (`trafic_index`) pour prédire le risque d'accident.
5. **Boucle d'Événements Réciproque** : Lorsqu'un accident est signalé, le simulateur crée un bouchon localisé, et le résorbe lorsque l'intervention est clôturée.

---

## 🚀 Démarrage Rapide

### 1. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancement du Serveur (Port 8001)
Sous Linux :
```bash
./run_simulator.sh
```
Ou sous Windows :
```cmd
run_simulator.bat
```
*(Ou directement avec uvicorn : `python -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload`)*

---

## 🖥️ Interfaces Disponibles

- **Console Web Interactive** : [http://localhost:8001/](http://localhost:8001/)  
  Permet de visualiser les KPIs de trafic en direct, d'injecter des accidents et d'activer les scénarios de démonstration (Heure de pointe, Intempéries, etc.).
- **Documentation Swagger OpenAPI** : [http://localhost:8001/docs](http://localhost:8001/docs)  
  Pour tester et documenter l'ensemble des endpoints REST.

---

## 📡 Endpoints API REST & WebSockets

| Méthode | Endpoint | Description |
|---|---|---|
| `GET` | `/api/traffic/segments` | Liste complète des tronçons avec géométrie, vitesse et couleur |
| `GET` | `/api/traffic/summary` | Synthèse régionale globale (indice moyen, état) |
| `GET` | `/api/traffic/zone-risk-data` | Indice de trafic par zone pour le modèle Random Forest |
| `POST` | `/api/traffic/route-delay` | Calcul du retard et de la durée d'intervention avec trafic |
| `POST` | `/api/traffic/events/accident` | Déclaration d'un accident et création d'un bouchon localisé |
| `POST` | `/api/traffic/events/clear` | Rétablissement du trafic après clôture d'intervention |
| `POST` | `/api/simulation/preset` | Bascule immédiate de scénario (FLUID, NORMAL, RUSH_HOUR, RAIN_STORM, GRIDLOCK) |
| `WS` | `/ws/traffic` | Flux WebSocket poussant les variations en temps réel |
# SmartcityInsightAI-Simulator
