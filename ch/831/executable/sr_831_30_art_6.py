"""SR 831.30 Art. 6

Generated from: ch/831/de/831.30.md

Art. 6: Mindestalter
Persons with entitlement to a helplessness allowance only have a right to
supplementary benefits once they have reached the age of 18.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der Person in Jahren"
    reference = "SR 831.30 Art. 6"


class el_bezieht_hilflosenentschaedigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person bezieht eine Hilflosenentschaedigung"
    reference = "SR 831.30 Art. 6"


class el_mindestalter_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestalter fuer EL bei Hilflosenentschaedigung erfuellt (18 Jahre)"
    reference = "SR 831.30 Art. 6"

    def formula(person, period, parameters):
        alter = person('el_alter', period)
        bezieht_he = person('el_bezieht_hilflosenentschaedigung', period)

        # If person receives helplessness allowance, must be >= 18
        # If no helplessness allowance, this condition does not apply (always True)
        return not_(bezieht_he) + (bezieht_he * (alter >= 18))
