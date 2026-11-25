import math
import random
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from .models import (
    CongestionLevel,
    TrafficSegment,
    TrafficSummary,
    RouteDelayRequest,
    RouteDelayResponse,
    AccidentEvent,
)
from .roads_cap_bon import ROAD_SEGMENTS_CAP_BON


def haversine_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calcule la distance géodésique en kilomètres entre deux coordonnées GPS."""
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2.0) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2.0) ** 2
    )
    return R * 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))


def _point_to_segment_distance_km(
    lat: float, lon: float, lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
    """Calcule la distance minimale en km entre un point GPS et un segment [A, B]."""
    cos_lat = math.cos(math.radians(lat))
    km_per_deg_lat = 111.32
    km_per_deg_lon = 111.32 * cos_lat

    px = (lon - lon1) * km_per_deg_lon
    py = (lat - lat1) * km_per_deg_lat
    dx = (lon2 - lon1) * km_per_deg_lon
    dy = (lat2 - lat1) * km_per_deg_lat

    seg_len_sq = dx * dx + dy * dy
    if seg_len_sq == 0.0:
        return haversine_distance_km(lat, lon, lat1, lon1)

    t = max(0.0, min(1.0, (px * dx + py * dy) / seg_len_sq))
    proj_lat = lat1 + t * (lat2 - lat1)
    proj_lon = lon1 + t * (lon2 - lon1)
    return haversine_distance_km(lat, lon, proj_lat, proj_lon)


def point_to_polyline_min_distance(lat: float, lon: float, polyline: List[List[float]]) -> float:
    """Calcule la distance minimale en km entre un point GPS et une polyligne de tronçon."""
    if not polyline:
        return float("inf")
    if len(polyline) == 1:
        return haversine_distance_km(lat, lon, polyline[0][0], polyline[0][1])

    min_dist = float("inf")
    for i in range(len(polyline) - 1):
        d = _point_to_segment_distance_km(
            lat, lon, polyline[i][0], polyline[i][1], polyline[i + 1][0], polyline[i + 1][1]
        )
        if d < min_dist:
            min_dist = d
    return min_dist


class TrafficEngine:
    """
    Moteur de simulation dynamique de circulation pour le Cap Bon Nord-Est
    (Kélibia, Hammam El Ghezaz, El Haouaria et environs immédiats).
    Gère les flux routiers, les heures de pointe, les intempéries et les impacts d'accidents.
    """

    def __init__(self):
        self.preset_name: str = "NORMAL"
        self.segments: Dict[str, TrafficSegment] = {}
        self.active_accidents: Dict[str, AccidentEvent] = {}
        self.weather_rain: bool = False
        self._initialize_segments()

    def _determine_color_and_level(self, index: float, has_incident: bool) -> Tuple[str, CongestionLevel]:
        if has_incident or index >= 4.4:
            return "#991b1b", CongestionLevel.BLOCKED
        elif index >= 3.2:
            return "#ef4444", CongestionLevel.HEAVY
        elif index >= 2.0:
            return "#f59e0b", CongestionLevel.MODERATE
        else:
            return "#10b981", CongestionLevel.FLUID

    def _initialize_segments(self):
        """Initialise tous les tronçons routiers avec les conditions du préréglage actif."""
        for seg in ROAD_SEGMENTS_CAP_BON:
            base_speed = seg["base_speed_kmh"]
            index = 1.6 + random.uniform(-0.2, 0.3)
            current_speed = max(10.0, base_speed * (1.0 - (index - 1.0) * 0.18))
            color, level = self._determine_color_and_level(index, False)

            self.segments[seg["id"]] = TrafficSegment(
                id=seg["id"],
                name=seg["name"],
                zone=seg["zone"],
                coordinates=seg["coordinates"],
                base_speed_kmh=base_speed,
                current_speed_kmh=round(current_speed, 1),
                congestion_level=level,
                congestion_index=round(index, 2),
                color=color,
                delay_seconds=0.0,
                vehicle_density=random.randint(18, 35),
                has_incident=False,
                incident_description=None,
            )

    def set_preset(self, preset: str):
        """Applique un scénario prédéfini de circulation."""
        preset = preset.upper()
        self.preset_name = preset

        preset_params = {
            "FLUID": {"index_mean": 1.2, "index_spread": 0.2, "speed_ratio": 0.95, "density": (10, 20)},
            "NORMAL": {"index_mean": 2.1, "index_spread": 0.4, "speed_ratio": 0.78, "density": (25, 45)},
            "RUSH_HOUR_MORNING": {"index_mean": 3.9, "index_spread": 0.6, "speed_ratio": 0.35, "density": (70, 95)},
            "RUSH_HOUR_EVENING": {"index_mean": 4.1, "index_spread": 0.5, "speed_ratio": 0.30, "density": (75, 100)},
            "RAIN_STORM": {"index_mean": 3.6, "index_spread": 0.7, "speed_ratio": 0.40, "density": (60, 85)},
            "GRIDLOCK": {"index_mean": 4.7, "index_spread": 0.3, "speed_ratio": 0.15, "density": (95, 120)},
        }

        params = preset_params.get(preset, preset_params["NORMAL"])

        for seg_id, segment in self.segments.items():
            # Si un accident est actif sur ce tronçon, maintenir le blocage
            if segment.has_incident:
                continue

            # Biais particulier selon la zone du Cap Bon Nord-Est pour réalisme local
            zone_bias = 0.0
            if "RUSH_HOUR_MORNING" in preset and segment.zone in ["KELIBIA", "MENZEL_HORR", "DAR_ALLOUCHE"]:
                zone_bias = 0.4
            elif "RUSH_HOUR_EVENING" in preset and segment.zone in ["KELIBIA", "HAMMAM_EL_GHEZAZ", "EL_HAOUARIA", "KERKOUANE"]:
                zone_bias = 0.45

            idx = min(5.0, max(1.0, params["index_mean"] + zone_bias + random.uniform(-params["index_spread"], params["index_spread"])))
            speed = max(8.0, segment.base_speed_kmh * params["speed_ratio"] * (1.0 - (idx - 1.0) * 0.12))
            density = random.randint(*params["density"])

            color, level = self._determine_color_and_level(idx, False)

            segment.congestion_index = round(idx, 2)
            segment.current_speed_kmh = round(speed, 1)
            segment.congestion_level = level
            segment.color = color
            segment.vehicle_density = density
            segment.delay_seconds = round(max(0.0, (1.0 / max(1.0, speed) - 1.0 / segment.base_speed_kmh) * 3600.0 * 2.0), 1)

    def add_accident_incident(self, incident: AccidentEvent):
        """
        Déclenche un ralentissement sévère immédiat sur les tronçons routiers
        situés à proximité de l'accident (rayon de 800m).
        """
        key = f"acc_{incident.alerte_id or random.randint(1000, 9999)}"
        self.active_accidents[key] = incident

        impacted_any = False
        for seg_id, seg in self.segments.items():
            dist = point_to_polyline_min_distance(incident.latitude, incident.longitude, seg.coordinates)
            if dist <= 0.8:  # 800 mètres
                impacted_any = True
                seg.has_incident = True
                seg.incident_description = f"🚨 {incident.description} (Gravité: {incident.gravite})"
                seg.congestion_index = 4.85
                seg.congestion_level = CongestionLevel.BLOCKED
                seg.color = "#991b1b"
                seg.current_speed_kmh = round(max(5.0, seg.base_speed_kmh * 0.12), 1)
                seg.vehicle_density = 110
                seg.delay_seconds = 240.0

        # Si aucun tronçon à < 800m, impacter le plus proche
        if not impacted_any and self.segments:
            closest_seg = min(
                self.segments.values(),
                key=lambda s: point_to_polyline_min_distance(incident.latitude, incident.longitude, s.coordinates),
            )
            closest_seg.has_incident = True
            closest_seg.incident_description = f"🚨 {incident.description} (Gravité: {incident.gravite})"
            closest_seg.congestion_index = 4.7
            closest_seg.congestion_level = CongestionLevel.BLOCKED
            closest_seg.color = "#991b1b"
            closest_seg.current_speed_kmh = round(max(5.0, closest_seg.base_speed_kmh * 0.15), 1)

    def clear_accident_incident(self, alerte_id: Optional[int] = None):
        """Lève les restrictions d'accident et rétablit progressivement la circulation."""
        to_delete = []
        if alerte_id is not None:
            target_key = f"acc_{alerte_id}"
            for k in list(self.active_accidents.keys()):
                if k == target_key or str(alerte_id) in k:
                    to_delete.append(k)
        else:
            to_delete = list(self.active_accidents.keys())

        for k in to_delete:
            self.active_accidents.pop(k, None)

        # Si plus aucun accident, rétablir tous les tronçons marqués
        if not self.active_accidents:
            for seg in self.segments.values():
                if seg.has_incident:
                    seg.has_incident = False
                    seg.incident_description = None
            self.set_preset(self.preset_name)

    def tick(self):
        """Micro-oscillation périodique (toutes les 3-5s) pour simuler la fluidité organique."""
        for seg in self.segments.values():
            if seg.has_incident:
                continue

            # Petite oscillation aléatoire +/- 3%
            noise = random.uniform(-0.06, 0.06)
            new_idx = max(1.0, min(5.0, seg.congestion_index + noise))
            seg.congestion_index = round(new_idx, 2)
            seg.color, seg.congestion_level = self._determine_color_and_level(new_idx, False)

            # Ajustement vitesse
            speed_ratio = max(0.15, 1.0 - (new_idx - 1.0) * 0.20)
            seg.current_speed_kmh = round(max(6.0, seg.base_speed_kmh * speed_ratio), 1)

    def calculate_route_delay(self, req: RouteDelayRequest) -> RouteDelayResponse:
        """
        Calcule la durée de trajet et le retard réel de trafic entre une Caserne et le sinistre
        en inspectant les tronçons routiers traversés par le corridor.
        """
        distance_straight = haversine_distance_km(
            req.origin_lat, req.origin_lng, req.destination_lat, req.destination_lng
        )
        # Distance routière réelle (~1.28x la ligne droite sur le réseau du Cap Bon)
        distance_km = round(distance_straight * 1.28, 2)

        # Identifier les tronçons intersectant ou proches du trajet
        lat_min = min(req.origin_lat, req.destination_lat) - 0.02
        lat_max = max(req.origin_lat, req.destination_lat) + 0.02
        lng_min = min(req.origin_lng, req.destination_lng) - 0.02
        lng_max = max(req.origin_lng, req.destination_lng) + 0.02

        impacted_segments = []
        weighted_indices = []
        impacted_base_speeds = []

        for seg in self.segments.values():
            pts = seg.coordinates
            hit = any(lat_min <= pt[0] <= lat_max and lng_min <= pt[1] <= lng_max for pt in pts)
            if not hit and len(pts) >= 2:
                # Vérifier aussi les points milieux des sous-segments pour les axes interurbains longs
                for i in range(len(pts) - 1):
                    mid_lat = (pts[i][0] + pts[i + 1][0]) * 0.5
                    mid_lng = (pts[i][1] + pts[i + 1][1]) * 0.5
                    if lat_min <= mid_lat <= lat_max and lng_min <= mid_lng <= lng_max:
                        hit = True
                        break
            if hit:
                impacted_segments.append(seg.name)
                weighted_indices.append(seg.congestion_index)
                impacted_base_speeds.append(seg.base_speed_kmh)

        if not weighted_indices:
            avg_index = sum(s.congestion_index for s in self.segments.values()) / max(1, len(self.segments))
            nominal_speed = 62.0
        else:
            avg_index = sum(weighted_indices) / len(weighted_indices)
            avg_base_speed = sum(impacted_base_speeds) / len(impacted_base_speeds)
            nominal_speed = min(85.0, max(45.0, avg_base_speed * 0.9))

        free_flow_duration_min = round((distance_km / nominal_speed) * 60.0, 1)

        # Facteur de congestion
        # En mode véhicule d'urgence (198), les gyrophares divisent par deux l'impact du trafic standard
        emergency_attenuation = 0.55 if req.emergency_mode else 1.0
        congestion_penalty_ratio = (avg_index - 1.0) * 0.35 * emergency_attenuation

        effective_speed = max(18.0, nominal_speed / (1.0 + congestion_penalty_ratio))
        traffic_duration_min = round((distance_km / effective_speed) * 60.0, 1)

        delay_minutes = max(0.0, round(traffic_duration_min - free_flow_duration_min, 1))

        if avg_index >= 4.0:
            status = "Ralentissement majeur — Corridor très congestionné"
            warning = "🚨 Fort ralentissement sur le trajet. Priorité gyrophares requise."
        elif avg_index >= 2.5:
            status = "Ralentissement modéré — Trafic dense"
            warning = f"Trafic ralenti (+{delay_minutes} min estimées)."
        else:
            status = "Trafic fluide — Trajet optimal"
            warning = None

        return RouteDelayResponse(
            distance_km=distance_km,
            free_flow_duration_min=free_flow_duration_min,
            traffic_duration_min=traffic_duration_min,
            delay_minutes=delay_minutes,
            traffic_status=status,
            impacted_segments=list(set(impacted_segments))[:4],
            congestion_factor=round(avg_index, 2),
            warning=warning,
        )

    def get_summary(self) -> TrafficSummary:
        """Génère une synthèse régionale de la circulation."""
        segs = list(self.segments.values())
        if not segs:
            avg_idx = 1.0
            avg_spd = 50.0
            congested_count = 0
        else:
            avg_idx = sum(s.congestion_index for s in segs) / len(segs)
            avg_spd = sum(s.current_speed_kmh for s in segs) / len(segs)
            congested_count = sum(1 for s in segs if s.congestion_index >= 3.2)

        if avg_idx >= 4.0:
            status = "CONGESTION_CRITIQUE"
        elif avg_idx >= 2.8:
            status = "CIRCULATION_DENSE"
        elif avg_idx >= 1.8:
            status = "CIRCULATION_NORMALE"
        else:
            status = "CIRCULATION_FLUIDE"

        # Calcul par zone
        zone_indices = {}
        for seg in segs:
            zone_indices.setdefault(seg.zone, []).append(seg.congestion_index)
        zone_summary = {z: round(sum(vals) / len(vals), 2) for z, vals in zone_indices.items()}

        return TrafficSummary(
            average_congestion_index=round(avg_idx, 2),
            global_status=status,
            active_incidents=len(self.active_accidents),
            average_speed_kmh=round(avg_spd, 1),
            congested_segments_count=congested_count,
            total_segments=len(segs),
            preset_name=self.preset_name,
            timestamp=datetime.now().isoformat(),
            zone_indices=zone_summary,
        )
