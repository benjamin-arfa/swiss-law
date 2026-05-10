"""SR 172.220.111.3 Art. 60c - Conge pour prise en charge d'enfants gravement malades

Generated from: ch/172/fr/172.220.111.3.md

Leave for care of seriously ill/injured children:
- Up to 14 weeks paid leave (full salary + social allowances)
- Must be taken within 18-month framework period from first day of absence
- Child must meet ALL four criteria:
  a) major change in physical or psychological state
  b) outcome unpredictable or likely permanent/worsening/fatal
  c) increased need for parental care
  d) at least one parent must interrupt work
- Each case of illness/accident gives only one entitlement
- Relapse after long symptom-free period = new case
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class opers_enfant_gravement_atteint(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'enfant est gravement atteint dans sa sante (4 criteres cumulatifs)"
    reference = "SR 172.220.111.3 Art. 60c al. 2"


class opers_mois_depuis_debut_prise_charge(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Mois ecoules depuis le premier jour d'absence pour prise en charge"
    reference = "SR 172.220.111.3 Art. 60c al. 3"


class opers_semaines_prise_charge_utilisees(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de semaines de conge de prise en charge deja utilisees"
    reference = "SR 172.220.111.3 Art. 60c al. 1"


class opers_conge_prise_charge_semaines_restantes(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Nombre de semaines de conge de prise en charge restantes"
    reference = "SR 172.220.111.3 Art. 60c"

    def formula(person, period, parameters):
        enfant_atteint = person('opers_enfant_gravement_atteint', period.this_year)
        mois = person('opers_mois_depuis_debut_prise_charge', period)
        utilisees = person('opers_semaines_prise_charge_utilisees', period.this_year)

        # Maximum 14 semaines dans un delai-cadre de 18 mois
        dans_delai = mois <= 18
        restantes = max_(14 - utilisees, 0)

        return where(enfant_atteint * dans_delai, restantes, 0)
