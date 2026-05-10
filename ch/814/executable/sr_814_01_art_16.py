"""SR 814.01 Art. 16

Generated from: ch/814/de/814.01.md

Sanierungspflicht: Anlagen, die den Vorschriften nicht genuegen,
muessen saniert werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anlage_genuegt_vorschriften_nicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Anlage den Vorschriften des USG oder anderer Umweltgesetze nicht genuegt"
    reference = "SR 814.01 Art. 16 Abs. 1"


class ist_dringender_fall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein dringender Fall vorliegt (vorsorgliche Sanierung oder Stilllegung)"
    reference = "SR 814.01 Art. 16 Abs. 4"


class sanierungspflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Anlage saniert werden muss"
    reference = "SR 814.01 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        return person('anlage_genuegt_vorschriften_nicht', period)


class stilllegung_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Behoerden die Stilllegung der Anlage verfuegen koennen"
    reference = "SR 814.01 Art. 16 Abs. 4"

    def formula(person, period, parameters):
        nicht_konform = person('anlage_genuegt_vorschriften_nicht', period)
        dringend = person('ist_dringender_fall', period)
        return nicht_konform * dringend
