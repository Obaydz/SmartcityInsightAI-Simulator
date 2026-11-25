"""
Définition géographique et caractéristiques de 50 tronçons routiers du Cap Bon Nord-Est
(Gouvernorat de Nabeul) : Kélibia, Hammam El Ghezaz, El Haouaria et leurs environs immédiats
(Dar Allouche, Kerkouane, Azmour, Menzel Horr).
"""

from typing import List, Dict, Any

ROAD_SEGMENTS_CAP_BON: List[Dict[str, Any]] = [
    # =========================================================================
    # 1. KÉLIBIA (10 tronçons)
    # =========================================================================
    {
        "id": "seg_kelibia_centre_martyrs",
        "name": "Kélibia Centre — Avenue des Martyrs",
        "zone": "KELIBIA",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.8435, 11.0840],
            [36.8458, 11.0890],
            [36.8476, 11.0939],
            [36.8495, 11.0975],
        ],
    },
    {
        "id": "seg_kelibia_entree_sud_mc27",
        "name": "Kélibia — Entrée Sud (Route de Menzel Temime / MC27)",
        "zone": "KELIBIA",
        "base_speed_kmh": 55.0,
        "coordinates": [
            [36.8340, 11.0450],
            [36.8380, 11.0580],
            [36.8415, 11.0720],
            [36.8435, 11.0840],
        ],
    },
    {
        "id": "seg_kelibia_sortie_nord_rr27",
        "name": "Kélibia — Sortie Nord (Avenue de l'Environnement / RR27)",
        "zone": "KELIBIA",
        "base_speed_kmh": 50.0,
        "coordinates": [
            [36.8476, 11.0939],
            [36.8520, 11.0955],
            [36.8570, 11.0975],
            [36.8615, 11.1005],
        ],
    },
    {
        "id": "seg_kelibia_route_port",
        "name": "Kélibia — Avenue du Port de Pêche",
        "zone": "KELIBIA",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.8476, 11.0939],
            [36.8450, 11.1005],
            [36.8420, 11.1080],
            [36.8390, 11.1165],
        ],
    },
    {
        "id": "seg_kelibia_fort_citadelle",
        "name": "Kélibia — Route du Fort (Citadelle Byzantine)",
        "zone": "KELIBIA",
        "base_speed_kmh": 35.0,
        "coordinates": [
            [36.8420, 11.1080],
            [36.8442, 11.1115],
            [36.8458, 11.1155],
        ],
    },
    {
        "id": "seg_kelibia_mansourah_nord",
        "name": "Kélibia — Corniche & Plage El Mansourah",
        "zone": "KELIBIA",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.8458, 11.1155],
            [36.8491, 11.1257],
            [36.8555, 11.1235],
            [36.8610, 11.1205],
        ],
    },
    {
        "id": "seg_kelibia_mansourah_interieure",
        "name": "Kélibia — Avenue El Mansourah (Liaison Centre ➔ Plage)",
        "zone": "KELIBIA",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.8495, 11.0975],
            [36.8502, 11.1065],
            [36.8498, 11.1160],
            [36.8491, 11.1257],
        ],
    },
    {
        "id": "seg_kelibia_ain_el_grinz",
        "name": "Kélibia — Route de Aïn El Grinz (Plage Sud)",
        "zone": "KELIBIA",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.8415, 11.0720],
            [36.8350, 11.0785],
            [36.8285, 11.0860],
            [36.8240, 11.0940],
        ],
    },
    {
        "id": "seg_kelibia_rocade_ouest",
        "name": "Kélibia — Rocade Ouest (Liaison MC27 ➔ Route d'Azmour)",
        "zone": "KELIBIA",
        "base_speed_kmh": 60.0,
        "coordinates": [
            [36.8415, 11.0720],
            [36.8485, 11.0750],
            [36.8555, 11.0790],
            [36.8620, 11.0830],
        ],
    },
    {
        "id": "seg_kelibia_hopital_lycee",
        "name": "Kélibia — Avenue de l'Hôpital Régional & Lycée",
        "zone": "KELIBIA",
        "base_speed_kmh": 35.0,
        "coordinates": [
            [36.8485, 11.0750],
            [36.8495, 11.0825],
            [36.8510, 11.0900],
            [36.8520, 11.0955],
        ],
    },

    # =========================================================================
    # 2. HAMMAM EL GHEZAZ (7 tronçons)
    # =========================================================================
    {
        "id": "seg_heg_rr27_entree_sud",
        "name": "Hammam El Ghezaz — RR27 Entrée Sud (depuis Kélibia)",
        "zone": "HAMMAM_EL_GHEZAZ",
        "base_speed_kmh": 60.0,
        "coordinates": [
            [36.8615, 11.1005],
            [36.8675, 11.1045],
            [36.8730, 11.1080],
            [36.8770, 11.1108],
        ],
    },
    {
        "id": "seg_heg_centre_bourguiba",
        "name": "Hammam El Ghezaz Centre — Avenue Habib Bourguiba",
        "zone": "HAMMAM_EL_GHEZAZ",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.8745, 11.1085],
            [36.8770, 11.1108],
            [36.8800, 11.1125],
        ],
    },
    {
        "id": "seg_heg_route_plage",
        "name": "Hammam El Ghezaz — Avenue de la Plage",
        "zone": "HAMMAM_EL_GHEZAZ",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.8770, 11.1108],
            [36.8765, 11.1165],
            [36.8755, 11.1225],
        ],
    },
    {
        "id": "seg_heg_corniche_sud",
        "name": "Hammam El Ghezaz — Corniche Sud (Liaison El Mansourah)",
        "zone": "HAMMAM_EL_GHEZAZ",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.8610, 11.1205],
            [36.8685, 11.1220],
            [36.8755, 11.1225],
        ],
    },
    {
        "id": "seg_heg_corniche_nord",
        "name": "Hammam El Ghezaz — Corniche Nord (Plage Sidi Abdelwahed)",
        "zone": "HAMMAM_EL_GHEZAZ",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.8755, 11.1225],
            [36.8835, 11.1215],
            [36.8920, 11.1195],
        ],
    },
    {
        "id": "seg_heg_rr27_sortie_nord",
        "name": "Hammam El Ghezaz — RR27 Sortie Nord (vers Kerkouane)",
        "zone": "HAMMAM_EL_GHEZAZ",
        "base_speed_kmh": 65.0,
        "coordinates": [
            [36.8770, 11.1108],
            [36.8850, 11.1102],
            [36.8940, 11.1095],
            [36.9020, 11.1080],
        ],
    },
    {
        "id": "seg_heg_route_dar_chouchane",
        "name": "Hammam El Ghezaz — Route de Dar Chouchane ➔ Azmour",
        "zone": "HAMMAM_EL_GHEZAZ",
        "base_speed_kmh": 50.0,
        "coordinates": [
            [36.8770, 11.1108],
            [36.8825, 11.0840],
            [36.8930, 11.0620],
            [36.9050, 11.0400],
        ],
    },

    # =========================================================================
    # 3. EL HAOUARIA & ENVIRONS OUEST/NORD (10 tronçons)
    # =========================================================================
    {
        "id": "seg_haouaria_centre_republique",
        "name": "El Haouaria Centre — Avenue de la République",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [37.0445, 11.0165],
            [37.0500, 11.0144],
            [37.0545, 11.0110],
        ],
    },
    {
        "id": "seg_haouaria_entree_sud_rr27",
        "name": "El Haouaria — RR27 Entrée Sud (Boukrim ➔ El Haouaria)",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 70.0,
        "coordinates": [
            [37.0080, 11.0360],
            [37.0220, 11.0285],
            [37.0350, 11.0215],
            [37.0445, 11.0165],
        ],
    },
    {
        "id": "seg_haouaria_route_grottes",
        "name": "El Haouaria — Route des Grottes (Ghar El Kebir)",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [37.0500, 11.0144],
            [37.0565, 11.0040],
            [37.0620, 10.9945],
            [37.0655, 10.9860],
        ],
    },
    {
        "id": "seg_haouaria_route_cap_bon_phare",
        "name": "El Haouaria — Route du Phare de Cap Bon (Ras Ettib)",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [37.0500, 11.0144],
            [37.0610, 11.0250],
            [37.0710, 11.0350],
            [37.0790, 11.0445],
        ],
    },
    {
        "id": "seg_haouaria_plage_est",
        "name": "El Haouaria — Avenue de la Plage & Ras Ed-Drek",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [37.0500, 11.0144],
            [37.0525, 11.0385],
            [37.0615, 11.0490],
        ],
    },
    {
        "id": "seg_haouaria_route_sidi_daoud",
        "name": "El Haouaria ➔ El Menzel ➔ Sidi Daoud",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 65.0,
        "coordinates": [
            [37.0500, 11.0144],
            [37.0430, 10.9820],
            [37.0320, 10.9460],
            [37.0217, 10.9115],
        ],
    },
    {
        "id": "seg_haouaria_sidi_daoud_port",
        "name": "Sidi Daoud — Route du Port & Madrague",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [37.0217, 10.9115],
            [37.0255, 10.9055],
            [37.0290, 10.9005],
        ],
    },
    {
        "id": "seg_haouaria_sidi_daoud_zaouiet",
        "name": "Route Côtière Ouest — Sidi Daoud ➔ Zaouiet El Mgaïez",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 60.0,
        "coordinates": [
            [37.0217, 10.9115],
            [36.9930, 10.8960],
            [36.9640, 10.8810],
            [36.9351, 10.8693],
        ],
    },
    {
        "id": "seg_haouaria_boukrim_ouest",
        "name": "Boukrim — Route Intérieure vers Sidi Daoud",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 55.0,
        "coordinates": [
            [37.0180, 11.0310],
            [37.0190, 10.9920],
            [37.0205, 10.9520],
            [37.0217, 10.9115],
        ],
    },
    {
        "id": "seg_haouaria_saheb_el_jebel",
        "name": "El Haouaria Sud — Route de Saheb El Jebel",
        "zone": "EL_HAOUARIA",
        "base_speed_kmh": 50.0,
        "coordinates": [
            [37.0350, 11.0215],
            [37.0120, 10.9940],
            [36.9880, 10.9680],
        ],
    },

    # =========================================================================
    # 4. DAR ALLOUCHE (6 tronçons)
    # =========================================================================
    {
        "id": "seg_dar_allouche_centre",
        "name": "Dar Allouche Centre — Avenue Principale (RR27)",
        "zone": "DAR_ALLOUCHE",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.9620, 11.0595],
            [36.9673, 11.0542],
            [36.9735, 11.0505],
        ],
    },
    {
        "id": "seg_dar_allouche_rr27_nord",
        "name": "Dar Allouche — RR27 Nord vers Boukrim / El Haouaria",
        "zone": "DAR_ALLOUCHE",
        "base_speed_kmh": 70.0,
        "coordinates": [
            [36.9735, 11.0505],
            [36.9850, 11.0455],
            [36.9965, 11.0410],
            [37.0080, 11.0360],
        ],
    },
    {
        "id": "seg_dar_allouche_route_plage",
        "name": "Dar Allouche — Route de la Plage (Est)",
        "zone": "DAR_ALLOUCHE",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.9673, 11.0542],
            [36.9720, 11.0695],
            [36.9775, 11.0840],
        ],
    },
    {
        "id": "seg_dar_allouche_liaison_azmour",
        "name": "Dar Allouche Ouest — Route vers Azmour",
        "zone": "DAR_ALLOUCHE",
        "base_speed_kmh": 60.0,
        "coordinates": [
            [36.9673, 11.0542],
            [36.9560, 11.0410],
            [36.9445, 11.0285],
        ],
    },
    {
        "id": "seg_dar_allouche_route_oued_el_abid",
        "name": "Dar Allouche — Route Agricole Oued El Abid",
        "zone": "DAR_ALLOUCHE",
        "base_speed_kmh": 50.0,
        "coordinates": [
            [36.9735, 11.0505],
            [36.9760, 11.0310],
            [36.9790, 11.0120],
        ],
    },
    {
        "id": "seg_dar_allouche_liaison_kerkouane_nord",
        "name": "Dar Allouche — Piste Côtière Sud vers Kerkouane",
        "zone": "DAR_ALLOUCHE",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.9775, 11.0840],
            [36.9660, 11.0920],
            [36.9550, 11.0980],
        ],
    },

    # =========================================================================
    # 5. KERKOUANE (6 tronçons)
    # =========================================================================
    {
        "id": "seg_kerkouane_rr27_sud",
        "name": "Kerkouane — RR27 Entrée Sud (Oued El Ksab ➔ Kerkouane)",
        "zone": "KERKOUANE",
        "base_speed_kmh": 65.0,
        "coordinates": [
            [36.9020, 11.1080],
            [36.9165, 11.1050],
            [36.9310, 11.1020],
            [36.9457, 11.0989],
        ],
    },
    {
        "id": "seg_kerkouane_site_punique",
        "name": "Kerkouane — Avenue du Site Archéologique Punique",
        "zone": "KERKOUANE",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.9457, 11.0989],
            [36.9465, 11.1025],
            [36.9475, 11.1060],
        ],
    },
    {
        "id": "seg_kerkouane_rr27_dar_allouche",
        "name": "Kerkouane — RR27 Nord vers Dar Allouche",
        "zone": "KERKOUANE",
        "base_speed_kmh": 65.0,
        "coordinates": [
            [36.9457, 11.0989],
            [36.9515, 11.0860],
            [36.9570, 11.0725],
            [36.9620, 11.0595],
        ],
    },
    {
        "id": "seg_kerkouane_village_centre",
        "name": "Kerkouane Village — Rue Principale",
        "zone": "KERKOUANE",
        "base_speed_kmh": 35.0,
        "coordinates": [
            [36.9410, 11.0920],
            [36.9445, 11.0955],
            [36.9457, 11.0989],
        ],
    },
    {
        "id": "seg_kerkouane_plage_sud",
        "name": "Kerkouane — Piste Côtière Plage Sud (Oued El Ksab)",
        "zone": "KERKOUANE",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.9457, 11.0989],
            [36.9325, 11.1085],
            [36.9180, 11.1145],
        ],
    },
    {
        "id": "seg_kerkouane_liaison_azmour",
        "name": "Kerkouane Ouest — Route vers Azmour",
        "zone": "KERKOUANE",
        "base_speed_kmh": 55.0,
        "coordinates": [
            [36.9410, 11.0920],
            [36.9355, 11.0640],
            [36.9300, 11.0360],
            [36.9244, 11.0078],
        ],
    },

    # =========================================================================
    # 6. AZMOUR (5 tronçons)
    # =========================================================================
    {
        "id": "seg_azmour_centre",
        "name": "Azmour Centre — Avenue Principale",
        "zone": "AZMOUR",
        "base_speed_kmh": 40.0,
        "coordinates": [
            [36.9200, 11.0125],
            [36.9244, 11.0078],
            [36.9295, 11.0035],
        ],
    },
    {
        "id": "seg_azmour_kelibia_sud",
        "name": "Route d'Azmour — Tronçon Kélibia ➔ Azmour",
        "zone": "AZMOUR",
        "base_speed_kmh": 65.0,
        "coordinates": [
            [36.8620, 11.0830],
            [36.8810, 11.0580],
            [36.9005, 11.0350],
            [36.9200, 11.0125],
        ],
    },
    {
        "id": "seg_azmour_dar_allouche_nord",
        "name": "Route d'Azmour — Tronçon Azmour ➔ Dar Allouche",
        "zone": "AZMOUR",
        "base_speed_kmh": 60.0,
        "coordinates": [
            [36.9244, 11.0078],
            [36.9345, 11.0180],
            [36.9445, 11.0285],
        ],
    },
    {
        "id": "seg_azmour_zaouiet_ouest",
        "name": "Azmour Ouest — Route vers Zaouiet El Mgaïez",
        "zone": "AZMOUR",
        "base_speed_kmh": 55.0,
        "coordinates": [
            [36.9244, 11.0078],
            [36.9280, 10.9610],
            [36.9315, 10.9150],
            [36.9351, 10.8693],
        ],
    },
    {
        "id": "seg_azmour_jebel_abderrahmane",
        "name": "Azmour — Piste Jebel Sidi Abderrahmane",
        "zone": "AZMOUR",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.9295, 11.0035],
            [36.9420, 10.9860],
            [36.9550, 10.9690],
        ],
    },

    # =========================================================================
    # 7. MENZEL HORR & CORRIDOR SUD (6 tronçons)
    # =========================================================================
    {
        "id": "seg_menzel_horr_centre",
        "name": "Menzel Horr Centre — Traversée MC27",
        "zone": "MENZEL_HORR",
        "base_speed_kmh": 45.0,
        "coordinates": [
            [36.7210, 10.9525],
            [36.7278, 10.9567],
            [36.7350, 10.9595],
        ],
    },
    {
        "id": "seg_menzel_horr_lebna_plage",
        "name": "Menzel Horr — Route Côtière de Lebna Plage",
        "zone": "MENZEL_HORR",
        "base_speed_kmh": 50.0,
        "coordinates": [
            [36.7278, 10.9567],
            [36.7310, 10.9710],
            [36.7345, 10.9850],
        ],
    },
    {
        "id": "seg_menzel_horr_skalba",
        "name": "Menzel Horr Nord — MC27 vers Skalba & Menzel Temime",
        "zone": "MENZEL_HORR",
        "base_speed_kmh": 75.0,
        "coordinates": [
            [36.7350, 10.9595],
            [36.7485, 10.9465],
            [36.7620, 10.9350],
            [36.7937, 10.9079],
        ],
    },
    {
        "id": "seg_menzel_horr_menzel_yahia",
        "name": "Menzel Temime Est ➔ Menzel Yahia (MC27)",
        "zone": "MENZEL_HORR",
        "base_speed_kmh": 75.0,
        "coordinates": [
            [36.7937, 10.9079],
            [36.8040, 10.9380],
            [36.8140, 10.9680],
        ],
    },
    {
        "id": "seg_menzel_horr_oued_el_khatef",
        "name": "Menzel Yahia ➔ Oued El Khatef ➔ Entrée Kélibia",
        "zone": "MENZEL_HORR",
        "base_speed_kmh": 75.0,
        "coordinates": [
            [36.8140, 10.9680],
            [36.8260, 11.0120],
            [36.8340, 11.0450],
        ],
    },
    {
        "id": "seg_menzel_horr_oued_chiba",
        "name": "Menzel Horr Ouest — Route du Barrage Oued Chiba",
        "zone": "MENZEL_HORR",
        "base_speed_kmh": 55.0,
        "coordinates": [
            [36.7278, 10.9567],
            [36.7380, 10.9280],
            [36.7480, 10.9010],
        ],
    },
]
