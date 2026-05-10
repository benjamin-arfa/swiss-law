"""SR 901.022 Art. 6

Generated from: ch/901/fr/901.022.md

Art. 6: Conditions d'octroi d'un allegement fiscal.

Abs. 1: Conditions: canton accorde aussi un allegement + le projet cree/reoriente
des emplois + importance regionale.

Abs. 2: Entreprise de services proches de la production: minimum 10 emplois.

Abs. 4: Pas d'allegement si diminution nette d'emplois dans l'entreprise/groupe.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rpol_canton_accorde_allegement(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le canton accorde aussi un allegement fiscal au projet"
    reference = "SR 901.022 Art. 6 al. 1 let. a"


class rpol_emplois_crees(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre d'emplois crees ou reorientes par le projet"
    reference = "SR 901.022 Art. 6 al. 1 let. b"


class rpol_importance_regionale(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le projet presente une importance particuliere pour l'economie regionale"
    reference = "SR 901.022 Art. 6 al. 1 let. b ch. 2"


class rpol_entreprise_services(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'entreprise est une entreprise de services proches de la production"
    reference = "SR 901.022 Art. 6 al. 2"


class rpol_diminution_nette_emplois(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le projet entraine une diminution nette du nombre d'emplois"
    reference = "SR 901.022 Art. 6 al. 4"


class rpol_allegement_fiscal_eligible(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le projet est eligible a un allegement fiscal (Art. 6)"
    reference = "SR 901.022 Art. 6"

    def formula(person, period, parameters):
        p = parameters(period)
        canton_ok = person('rpol_canton_accorde_allegement', period)
        emplois = person('rpol_emplois_crees', period)
        importance = person('rpol_importance_regionale', period)
        services = person('rpol_entreprise_services', period)
        diminution = person('rpol_diminution_nette_emplois', period)
        zone_ok = person('rpol_commune_eligible_zone', period)

        seuil_emplois_services = p.sr_901_022.art_6.emplois_min_services

        # Condition emplois pour entreprise de services
        emplois_ok = where(services, emplois >= seuil_emplois_services, emplois > 0)

        return zone_ok * canton_ok * emplois_ok * importance * not_(diminution)
