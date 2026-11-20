from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum


class CongestionLevel(str, Enum):
    FLUID = "FLUID"          # Fluide (Vert)
    MODERATE = "MODERATE"    # Dense / Ralentissement (Jaune-Orange)
    HEAVY = "HEAVY"          # Congestionné (Rouge)
    BLOCKED = "BLOCKED"      # Bloqué / Accident (Rouge foncé)


class TrafficSegment(BaseModel):
    id: str
    name: str
    zone: str
    coordinates: List[List[float]] = Field(description="Liste de paires [latitude, longitude]")
    base_speed_kmh: float
    current_speed_kmh: float
    congestion_level: CongestionLevel
    congestion_index: float = Field(ge=1.0, le=5.0, description="Indice de 1.0 (fluide) à 5.0 (paralysé)")
    color: str = Field(description="Code couleur hexadécimal pour l'affichage cartographique")
    delay_seconds: float = 0.0
    vehicle_density: int = 20
    has_incident: bool = False
    incident_description: Optional[str] = None


class TrafficSummary(BaseModel):
    average_congestion_index: float
    global_status: str
    active_incidents: int
    average_speed_kmh: float
    congested_segments_count: int
    total_segments: int
    preset_name: str
    timestamp: str
    zone_indices: dict = Field(default_factory=dict)


class RouteDelayRequest(BaseModel):
    origin_lat: float
    origin_lng: float
    destination_lat: float
    destination_lng: float
    emergency_mode: bool = True  # Les véhicules prioritaires avec gyrophares ont un facteur de réduction du retard


class RouteDelayResponse(BaseModel):
    distance_km: float
    free_flow_duration_min: float
    traffic_duration_min: float
    delay_minutes: float
    traffic_status: str
    impacted_segments: List[str]
    congestion_factor: float
    warning: Optional[str] = None


class AccidentEvent(BaseModel):
    alerte_id: Optional[int] = None
    latitude: float
    longitude: float
    gravite: str = "GRAVE"
    description: Optional[str] = "Accident de la circulation"


class PresetRequest(BaseModel):
    preset: str = Field(description="FLUID, NORMAL, RUSH_HOUR_MORNING, RUSH_HOUR_EVENING, RAIN_STORM, GRIDLOCK")
