"""SR 901.022 Art. 3

Generated from: ch/901/fr/901.022.md

Art. 3: Zone d'application pour allegements fiscaux.

Abs. 1: Criteres: la commune doit etre un centre petit/moyen/rural/suburbain
et appartenir aux regions structurellement faibles.

Abs. 2: Les zones d'application ne peuvent pas representer ensemble plus
de 10% de la population suisse.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class rpol_region_structurellement_faible(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune appartient a une region structurellement faible"
    reference = "SR 901.022 Art. 3 al. 1 let. b"


class rpol_dans_espace_suburbain(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune fait partie de l'espace suburbain d'un centre petit ou moyen"
    reference = "SR 901.022 Art. 2 let. d / Art. 3 al. 1 let. a ch. 1"


class rpol_commune_eligible_zone(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La commune remplit les criteres pour la zone d'application (Art. 3 al. 1)"
    reference = "SR 901.022 Art. 3 al. 1"

    def formula(person, period, parameters):
        petit_centre = person('rpol_est_petit_centre_urbain', period)
        centre_moyen = person('rpol_est_centre_urbain_moyen', period)
        suburbain = person('rpol_dans_espace_suburbain', period)
        centre_rural = person('rpol_est_centre_rural', period)
        faible = person('rpol_region_structurellement_faible', period)
        # Type a: petit/moyen centre ou suburbain, ou centre rural, ou petit centre avec services
        type_ok = (petit_centre + centre_moyen + suburbain + centre_rural) > 0
        return type_ok * faible


class rpol_population_zone_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Part maximale de la population suisse dans les zones d'application"
    reference = "SR 901.022 Art. 3 al. 2"

    def formula(person, period, parameters):
        p = parameters(period)
        return p.sr_901_022.art_3.population_zone_max_pct
