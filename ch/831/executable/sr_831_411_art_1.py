"""SR 831.411 Art. 1

Generated from: ch/831/de/831.411.md

Art. 1: Zulaessige Verwendungszwecke - Permitted uses for pension assets.

Abs. 1: Pension assets may be used for:
a. Acquisition and construction of residential property
b. Participation in residential property
c. Repayment of mortgage loans

Abs. 2: The insured person may use pension assets for only one property
at a time.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wefv_erwerb_wohneigentum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mittel werden fuer Erwerb/Erstellung von Wohneigentum verwendet"
    reference = "SR 831.411 Art. 1 Abs. 1 Bst. a"


class wefv_beteiligung_wohneigentum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mittel werden fuer Beteiligungen am Wohneigentum verwendet"
    reference = "SR 831.411 Art. 1 Abs. 1 Bst. b"


class wefv_rueckzahlung_hypothek(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Mittel werden fuer Rueckzahlung von Hypothekardarlehen verwendet"
    reference = "SR 831.411 Art. 1 Abs. 1 Bst. c"


class wefv_verwendungszweck_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Verwendungszweck ist zulaessig (Art. 1 WEFV)"
    reference = "SR 831.411 Art. 1"

    def formula(person, period, parameters):
        erwerb = person('wefv_erwerb_wohneigentum', period)
        beteiligung = person('wefv_beteiligung_wohneigentum', period)
        hypothek = person('wefv_rueckzahlung_hypothek', period)
        return (erwerb + beteiligung + hypothek) > 0
