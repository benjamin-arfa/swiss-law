"""SR 730.022.2 Art. 1

Generated from: ch/730/fr/730.022.2.md

Art. 1 - Energy efficiency categories for passenger vehicles (2022):
Categories A-G based on primary energy gasoline equivalents (l/100km).
  A: <= 5.35
  B: > 5.35 to <= 6.10
  C: > 6.10 to <= 6.60
  D: > 6.60 to <= 7.30
  E: > 7.30 to <= 8.29
  F: > 8.29 to <= 10.14
  G: > 10.14
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class oee_vvt_equivalent_essence_primaire(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Primary energy gasoline equivalent consumption (l/100km)"
    reference = "SR 730.022.2 Art. 1"


class oee_vvt_categorie_efficacite(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Energy efficiency category (A-G) based on primary energy gasoline equivalent"
    reference = "SR 730.022.2 Art. 1"
    max_length = 1

    def formula(person, period, parameters):
        eq = person('oee_vvt_equivalent_essence_primaire', period)
        p = parameters(period).sr_730_022_2

        # Categories based on primary energy gasoline equivalents
        return where(eq <= p.categorie_a_max, 'A',
               where(eq <= p.categorie_b_max, 'B',
               where(eq <= p.categorie_c_max, 'C',
               where(eq <= p.categorie_d_max, 'D',
               where(eq <= p.categorie_e_max, 'E',
               where(eq <= p.categorie_f_max, 'F',
                     'G'))))))
