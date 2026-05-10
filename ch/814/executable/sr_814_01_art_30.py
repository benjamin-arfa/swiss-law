"""SR 814.01 Art. 30

Generated from: ch/fr/814/814.01.md

Art. 30: Principes pour les dechets (Abfallgrundsaetze)
- Abs. 1: Waste production shall be limited as far as possible.
- Abs. 2: Waste shall be recycled/valorized as far as possible.
- Abs. 3: Waste shall be disposed of in an environmentally sound manner,
  and as far as possible domestically.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class usg_abfallmenge_tonnen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Abfallmenge in Tonnen"
    reference = "SR 814.01 Art. 30 Abs. 1"


class usg_abfall_verwertungsquote(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil des verwerteten Abfalls (0 bis 1)"
    reference = "SR 814.01 Art. 30 Abs. 2"


class usg_abfall_inlandentsorgung_anteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Inlandentsorgung (0 bis 1)"
    reference = "SR 814.01 Art. 30 Abs. 3"


class usg_abfall_umweltgerecht_entsorgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = True
    label = "Ob die Abfaelle umweltgerecht entsorgt werden"
    reference = "SR 814.01 Art. 30 Abs. 3"
