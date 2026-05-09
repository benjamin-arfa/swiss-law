"""SR 901.022 Art. 2

Generated from: ch/901/fr/901.022.md

Art. 2: Definitions des types de centres et seuils de population.

a. Centre rural: 2000-10'000 habitants
b. Petit centre urbain: >= 8500 habitants et >= 3500 personnes actives,
   a >= 10 km d'un centre plus important
c. Centre urbain moyen: >= 40'000 habitants ou personnes actives,
   a >= 10 km d'un centre plus important
e. Grand centre urbain: >= 70'000 habitants ou personnes actives
f. Centre metropolitain: >= 200'000 habitants ou personnes actives
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class rpol_nombre_habitants(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre d'habitants de la commune"
    reference = "SR 901.022 Art. 2"


class rpol_nombre_personnes_actives(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de personnes actives dans la commune"
    reference = "SR 901.022 Art. 2"


class rpol_distance_centre_plus_important(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Distance au centre plus important (km)"
    reference = "SR 901.022 Art. 2"


class rpol_services_centraux_regionaux(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune assure des services centraux importants au niveau regional"
    reference = "SR 901.022 Art. 2"


class rpol_est_centre_rural(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune est un centre rural (Art. 2 let. a)"
    reference = "SR 901.022 Art. 2 let. a"

    def formula(person, period, parameters):
        p = parameters(period)
        habitants = person('rpol_nombre_habitants', period)
        services = person('rpol_services_centraux_regionaux', period)
        seuil_min = p.sr_901_022.art_2.centre_rural_habitants_min
        seuil_max = p.sr_901_022.art_2.centre_rural_habitants_max
        return services * (habitants >= seuil_min) * (habitants <= seuil_max)


class rpol_est_petit_centre_urbain(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune est un petit centre urbain (Art. 2 let. b)"
    reference = "SR 901.022 Art. 2 let. b"

    def formula(person, period, parameters):
        p = parameters(period)
        habitants = person('rpol_nombre_habitants', period)
        actives = person('rpol_nombre_personnes_actives', period)
        distance = person('rpol_distance_centre_plus_important', period)
        services = person('rpol_services_centraux_regionaux', period)
        seuil_hab = p.sr_901_022.art_2.petit_centre_habitants_min
        seuil_act = p.sr_901_022.art_2.petit_centre_actives_min
        seuil_dist = p.sr_901_022.art_2.distance_min_centre_km
        return services * (habitants >= seuil_hab) * (actives >= seuil_act) * (distance >= seuil_dist)


class rpol_est_centre_urbain_moyen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune est un centre urbain moyen (Art. 2 let. c)"
    reference = "SR 901.022 Art. 2 let. c"

    def formula(person, period, parameters):
        p = parameters(period)
        habitants = person('rpol_nombre_habitants', period)
        actives = person('rpol_nombre_personnes_actives', period)
        distance = person('rpol_distance_centre_plus_important', period)
        services = person('rpol_services_centraux_regionaux', period)
        seuil = p.sr_901_022.art_2.centre_moyen_habitants_actives_min
        seuil_dist = p.sr_901_022.art_2.distance_min_centre_km
        return services * ((habitants >= seuil) + (actives >= seuil) > 0) * (distance >= seuil_dist)


class rpol_est_grand_centre_urbain(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune est un grand centre urbain (Art. 2 let. e)"
    reference = "SR 901.022 Art. 2 let. e"

    def formula(person, period, parameters):
        p = parameters(period)
        habitants = person('rpol_nombre_habitants', period)
        actives = person('rpol_nombre_personnes_actives', period)
        seuil = p.sr_901_022.art_2.grand_centre_habitants_actives_min
        return (habitants >= seuil) + (actives >= seuil) > 0


class rpol_est_centre_metropolitain(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune est un centre metropolitain (Art. 2 let. f)"
    reference = "SR 901.022 Art. 2 let. f"

    def formula(person, period, parameters):
        p = parameters(period)
        habitants = person('rpol_nombre_habitants', period)
        actives = person('rpol_nombre_personnes_actives', period)
        seuil = p.sr_901_022.art_2.centre_metropolitain_habitants_actives_min
        return (habitants >= seuil) + (actives >= seuil) > 0
