"""SR 824.0 Art. 11

Generated from: ch/824/de/824.0.md

Art. 11: End of civilian service obligation:
- Not previously in army: 12 years after year following admission
- Previously in army: end of year they would have been discharged from military
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zdg_war_in_armee_eingeteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "War in die Armee eingeteilt vor Zulassung zum Zivildienst"
    reference = "SR 824.0 Art. 11 Abs. 2"


class zdg_jahr_zulassung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr der rechtskräftigen Zulassung zum Zivildienst"
    reference = "SR 824.0 Art. 11 Abs. 2 Bst. a"


class zdg_jahr_entlassung_militaer(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr, in dem die Person aus der Militärdienstpflicht entlassen worden wäre"
    reference = "SR 824.0 Art. 11 Abs. 2 Bst. b"


class zdg_ende_zivildienstpflicht_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des Endes der Zivildienstpflicht"
    reference = "SR 824.0 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        war_armee = person('zdg_war_in_armee_eingeteilt', period)
        jahr_zulassung = person('zdg_jahr_zulassung', period)
        jahr_entlassung_mil = person('zdg_jahr_entlassung_militaer', period)

        # Not in army: 12 years after year following admission
        ende_ohne_armee = jahr_zulassung + 1 + 12

        # Was in army: end of the year they would have been discharged
        ende_mit_armee = jahr_entlassung_mil

        return where(war_armee, ende_mit_armee, ende_ohne_armee)
