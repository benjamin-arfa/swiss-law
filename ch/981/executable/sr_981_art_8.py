"""SR 981 Art. 8

Generated from: ch/de/981.md

Appeals procedure: no party status or right of appeal for applicants
regarding other persons' claims; EDA has right of appeal; exclusion
of unreasonableness plea.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuchsteller_keine_parteistellung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Gesuchsteller bei der Beurteilung von Begehren anderer Personen keine Parteistellung hat"
    reference = "SR 981 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return True


class gesuchsteller_kein_beschwerderecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Gesuchsteller bei der Beurteilung von Begehren anderer Personen kein Beschwerderecht hat"
    reference = "SR 981 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return True


class eda_beschwerdeberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das EDA zur Beschwerde berechtigt ist"
    reference = "SR 981 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        return True


class ruege_unangemessenheit_ausgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Ruege der Unangemessenheit ausgeschlossen ist"
    reference = "SR 981 Art. 8 Abs. 3"

    def formula(person, period, parameters):
        return True
