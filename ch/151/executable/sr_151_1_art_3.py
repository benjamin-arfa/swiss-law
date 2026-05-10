"""SR 151.1 Art. 3

Generated from: ch/151/de/151.1.md

Diskriminierungsverbot: Arbeitnehmerinnen und Arbeitnehmer duerfen
aufgrund ihres Geschlechts weder direkt noch indirekt benachteiligt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class benachteiligung_wegen_geschlecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Benachteiligung aufgrund des Geschlechts vorliegt"
    reference = "SR 151.1 Art. 3 Abs. 1"


class benachteiligung_wegen_zivilstand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Benachteiligung unter Berufung auf den Zivilstand vorliegt"
    reference = "SR 151.1 Art. 3 Abs. 1"


class benachteiligung_wegen_schwangerschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Benachteiligung wegen Schwangerschaft vorliegt"
    reference = "SR 151.1 Art. 3 Abs. 1"


class massnahme_zur_gleichstellung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Massnahme zur Verwirklichung der tatsaechlichen Gleichstellung vorliegt"
    reference = "SR 151.1 Art. 3 Abs. 3"


class diskriminierung_nach_glg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Diskriminierung nach Art. 3 GlG vorliegt"
    reference = "SR 151.1 Art. 3"

    def formula(person, period, parameters):
        geschlecht = person('benachteiligung_wegen_geschlecht', period)
        zivilstand = person('benachteiligung_wegen_zivilstand', period)
        schwangerschaft = person('benachteiligung_wegen_schwangerschaft', period)
        massnahme = person('massnahme_zur_gleichstellung', period)
        benachteiligung = geschlecht + zivilstand + schwangerschaft > 0
        return benachteiligung * (1 - massnahme)
