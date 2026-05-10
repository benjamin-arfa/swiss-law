"""SR 151.1 Art. 8 - Procedure en cas de discrimination a l'embauche

Generated from: ch/151/fr/151.1.md

Procedural rules for hiring discrimination:
- Right to request written justification from employer
- 3-month peremptory deadline to bring indemnity claim from notification of refusal
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class leg_date_refus_embauche_communique(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Date a laquelle le refus d'embauche a ete communique"
    reference = "SR 151.1 Art. 8 al. 2"


class leg_date_action_indemnite(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Date de l'action en justice pour indemnite d'embauche"
    reference = "SR 151.1 Art. 8 al. 2"


class leg_jours_depuis_refus(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours ecoules entre le refus d'embauche et l'action en justice"
    reference = "SR 151.1 Art. 8 al. 2"


class leg_delai_action_embauche_respecte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le delai de 3 mois pour agir en justice apres refus d'embauche est respecte"
    reference = "SR 151.1 Art. 8 al. 2"

    def formula(person, period, parameters):
        jours = person('leg_jours_depuis_refus', period)
        # 3 mois ~ 90 jours (approximation; le calcul exact depend du calendrier)
        return jours <= 90
