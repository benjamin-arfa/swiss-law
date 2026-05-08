"""SR 837.0 Art. 9

Generated from: ch/837/de/837.0.md

Art. 9: Rahmenfristen (Framework periods)
- Abs. 1: Both the benefit claim period and the contribution period have
  two-year framework periods, unless the law provides otherwise.
- Abs. 2: The framework for benefit claims begins on the first day all
  eligibility conditions are met.
- Abs. 3: The framework for contributions begins two years before that day.
- Abs. 4: If the benefit framework expires and the insured person claims
  again, new two-year frameworks begin.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alv_rahmenfrist_leistungsbezug_beginn(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Beginn der Rahmenfrist fuer den Leistungsbezug (Datum)"
    reference = "SR 837.0 Art. 9 Abs. 2"


class alv_rahmenfrist_beitragszeit_beginn(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Beginn der Rahmenfrist fuer die Beitragszeit (Datum)"
    reference = "SR 837.0 Art. 9 Abs. 3"


class alv_rahmenfrist_dauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer der Rahmenfrist in Monaten (regulaer 24)"
    reference = "SR 837.0 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        # Default framework period is 24 months
        # Extensions possible under Art. 9a (self-employment) and Art. 9b (child-rearing)
        return parameters(period).alv.rahmenfrist_leistungsbezug_monate
