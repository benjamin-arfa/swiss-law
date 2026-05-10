"""SR 196.1 Art. 27

Generated from: ch/196/de/196.1.md

Widerhandlungen in Geschaeftsbetrieben: Der Geschaeftsbetrieb kann anstelle
der strafbaren Personen verurteilt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ermittlung_strafbarer_personen_unverhaeltnismaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Ermittlung der strafbaren Personen unverhaeltnismaessige Untersuchungsmassnahmen erfordern wuerde"
    reference = "SR 196.1 Art. 27 lit. a"


class busse_hoechstens_50000(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob fuer die Widerhandlung eine Busse von hoechstens 50'000 CHF in Betracht faellt"
    reference = "SR 196.1 Art. 27 lit. b"


class geschaeftsbetrieb_kann_verurteilt_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Geschaeftsbetrieb anstelle der strafbaren Personen verurteilt werden kann"
    reference = "SR 196.1 Art. 27"

    def formula(person, period, parameters):
        unverhaeltnismaessig = person('ermittlung_strafbarer_personen_unverhaeltnismaessig', period)
        busse_limit = person('busse_hoechstens_50000', period)
        return unverhaeltnismaessig * busse_limit
