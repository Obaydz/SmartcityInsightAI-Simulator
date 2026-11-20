"""
Définition géographique et caractéristiques des principales artères routières du Grand Tunis.
Ces tronçons modélisent les corridors de transport critiques surveillés par la Protection Civile
et la municipalité de Tunis.
"""

from typing import List, Dict, Any

ROAD_SEGMENTS_TUNIS: List[Dict[str, Any]] = [
    {
        "id": "seg_bourguiba",
        "name": "Avenue Habib Bourguiba & Avenue de France",
        "zone": "TUNIS_CENTRE",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.7995, 10.1720],  # Place de la Victoire (Porte de France)
            [36.8002, 10.1800],  # Cathédrale Saint-Vincent
            [36.8008, 10.1865],  # Horloge / Place 14 Janvier
            [36.8015, 10.1920],  # Tunis Marine (TGM)
        ],
    },
    {
        "id": "seg_mohamed_v",
        "name": "Avenue Mohamed V",
        "zone": "TUNIS_CENTRE",
        "base_speed_kmh": 50.0,
        "coordinates": [
            [36.8008, 10.1865],  # Place 14 Janvier
            [36.8085, 10.1845],  # Place des Droits de l'Homme
            [36.8142, 10.1824],  # Cité de la Culture
            [36.8220, 10.1805],  # Place Pasteur
        ],
    },
    {
        "id": "seg_route_x_sud",
        "name": "Route X — Tronçon Sud (Bardo / Bab Saadoun)",
        "zone": "BARDO",
        "base_speed_kmh": 70.0,
        "coordinates": [
            [36.7900, 10.1470],  # Échangeur Ben Dahha
            [36.8010, 10.1410],  # Échangeur Denden / Bardo
            [36.8115, 10.1384],  # Rond-point Bardo / Hôpital Militaire
            [36.8210, 10.1500],  # Jonction Bab Saadoun
        ],
    },
    {
        "id": "seg_route_x_nord",
        "name": "Route X — Tronçon Nord (El Manar / Campus)",
        "zone": "EL_MANAR",
        "base_speed_kmh": 75.0,
        "coordinates": [
            [36.8210, 10.1500],  # Jonction Bab Saadoun
            [36.8320, 10.1520],  # Campus Universitaire El Manar
            [36.8430, 10.1660],  # Échangeur El Menzah / Ennasr
            [36.8520, 10.1780],  # Jonction GP8 Ariana
        ],
    },
    {
        "id": "seg_rn9_marsa_ouest",
        "name": "RN9 — Route de La Marsa (Tunis Marine ➔ Lac 1)",
        "zone": "LAC",
        "base_speed_kmh": 80.0,
        "coordinates": [
            [36.8015, 10.1920],  # Tunis Marine
            [36.8150, 10.2080],  # Jonction Pont Radès-La Goulette
            [36.8280, 10.2250],  # Échangeur Les Berges du Lac 1
        ],
    },
    {
        "id": "seg_rn9_marsa_est",
        "name": "RN9 — Route de La Marsa (Lac 2 ➔ Ain Zaghouan ➔ Marsa)",
        "zone": "BANLIEUE_NORD",
        "base_speed_kmh": 90.0,
        "coordinates": [
            [36.8280, 10.2250],  # Échangeur Lac 1
            [36.8400, 10.2500],  # Échangeur Les Berges du Lac 2
            [36.8524, 10.2785],  # Échangeur Ain Zaghouan / Carrefour
            [36.8680, 10.3050],  # Sidi Daoud
            [36.8785, 10.3250],  # Entrée La Marsa Ville
        ],
    },
    {
        "id": "seg_sortie_sud_bab_alioua",
        "name": "Sortie Sud & GP1 — Échangeur Bab Alioua",
        "zone": "BANLIEUE_SUD",
        "base_speed_kmh": 65.0,
        "coordinates": [
            [36.7954, 10.1820],  # Avenue de Carthage
            [36.7865, 10.1832],  # Échangeur Bab Alioua
            [36.7770, 10.1950],  # Jonction Djebel Jelloud
            [36.7650, 10.2100],  # Pont de Mégrine / Entrée Autoroute A1
        ],
    },
    {
        "id": "seg_gp8_ariana",
        "name": "GP8 — Route de Bizerte (Ariana Ouest)",
        "zone": "ARIANA",
        "base_speed_kmh": 60.0,
        "coordinates": [
            [36.8220, 10.1805],  # Place Pasteur
            [36.8410, 10.1740],  # Cité El Khadra
            [36.8600, 10.1650],  # Ariana Ouest (Échangeur GP8)
            [36.8820, 10.1530],  # Direction Borj Louzir / Bizerte
        ],
    },
    {
        "id": "seg_berges_du_lac",
        "name": "Boulevard Principal des Berges du Lac 1",
        "zone": "LAC",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.8280, 10.2250],  # Entrée RN9
            [36.8340, 10.2330],  # Rue du Lac Windermere (Ambassades)
            [36.8385, 10.2440],  # Place Taher Haddad (Lac 1)
            [36.8415, 10.2520],  # Jonction Boulevard du Lac Nord
        ],
    },
    {
        "id": "seg_ariana_centre",
        "name": "Avenue Taïeb Mhiri (Ariana Centre)",
        "zone": "ARIANA",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.8490, 10.1900],  # Rond-point El Menzeh 6
            [36.8580, 10.1930],  # Avenue Habib Bourguiba Ariana
            [36.8625, 10.1956],  # Caserne Ariana & Marché
            [36.8710, 10.1985],  # Sortie Ariana Nord
        ],
    },
    {
        "id": "seg_liberte_thameur",
        "name": "Avenue de la Liberté & Bab El Khadra",
        "zone": "TUNIS_CENTRE",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.8040, 10.1805],  # Le Passage (Station de Bus)
            [36.8123, 10.1784],  # Bab El Khadra (Caserne Centrale)
            [36.8190, 10.1765],  # Avenue de Madrid / Jardin du Belvédère
            [36.8220, 10.1805],  # Place Pasteur
        ],
    },
    {
        "id": "seg_goulette_roosevelt",
        "name": "Avenue Franklin Roosevelt (La Goulette / Le Kram)",
        "zone": "BANLIEUE_NORD",
        "base_speed_kmh": 50.0,
        "coordinates": [
            [36.8120, 10.3010],  # Canal de La Goulette
            [36.8182, 10.3045],  # Caserne Portuaire de La Goulette
            [36.8280, 10.3120],  # Casino de La Goulette
            [36.8380, 10.3180],  # Entrée Le Kram Plage
        ],
    },
]
