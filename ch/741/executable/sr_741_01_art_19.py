"""SR 741.01 Art. 19 - Radfahrer

Generated from: ch/de/741/741.01.md

Cycling rules:
- Children under 6 may only cycle on main roads under supervision
  of a person at least 16 years old
- Prohibition of cycling for persons with illness/addiction
- Min 1 month cycling ban for dangerous/drunk cycling
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alter_radfahrer(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter des Radfahrers in Jahren"
    reference = "SR 741.01 Art. 19 Abs. 1"


class radfahrt_auf_hauptstrasse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob auf einer Hauptstrasse Rad gefahren wird"
    reference = "SR 741.01 Art. 19 Abs. 1"


class begleitung_durch_person_ueber_16(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Begleitung durch eine mindestens 16-jaehrige Person vorhanden"
    reference = "SR 741.01 Art. 19 Abs. 1"


class kind_darf_hauptstrasse_befahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Kind die Hauptstrasse mit dem Rad befahren darf"
    reference = "SR 741.01 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter_radfahrer', period.this_year)
        hauptstrasse = person('radfahrt_auf_hauptstrasse', period)
        begleitung = person('begleitung_durch_person_ueber_16', period)
        # Under 6 on main road: only with supervision
        unter_6 = alter < 6
        return (1 - hauptstrasse) + (1 - unter_6) + (unter_6 * begleitung) > 0


class fahrverbot_rad_mindestdauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Mindestdauer eines Fahrverbots fuer Radfahrer in Monaten"
    reference = "SR 741.01 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        return 1
