"""SR 812.21 Art. 4

Generated from: ch/812/de/812.21.md

Art. 4: Begriffe - Key definitions including Orphan Drug threshold:
- Orphan Drug: disease affecting max 5 per 10,000 persons in Switzerland
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hmg_ist_orphan_drug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Arzneimittel qualifiziert als wichtiges Arzneimittel für seltene Krankheiten (Orphan Drug)"
    reference = "SR 812.21 Art. 4 Abs. 1 Bst. adecies"


class hmg_krankheit_praevalenz_pro_10000(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prävalenz der Erkrankung pro 10'000 Personen in der Schweiz"
    reference = "SR 812.21 Art. 4 Abs. 1 Bst. adecies Ziff. 1"


class hmg_orphan_status_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Orphan-Drug-Status von einem Land mit vergleichbarer Arzneimittelkontrolle anerkannt"
    reference = "SR 812.21 Art. 4 Abs. 1 Bst. adecies Ziff. 2"


class hmg_orphan_drug_berechtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Berechtigung zum Orphan-Drug-Status nach Art. 4 HMG"
    reference = "SR 812.21 Art. 4 Abs. 1 Bst. adecies"

    def formula(person, period, parameters):
        praevalenz = person('hmg_krankheit_praevalenz_pro_10000', period)
        status_ausland = person('hmg_orphan_status_ausland', period)

        p = parameters(period).sr_812_21

        # Either: prevalence <= 5/10000 in Switzerland, or recognized abroad
        praevalenz_ok = praevalenz <= p.orphan_drug_max_praevalenz
        return praevalenz_ok + status_ausland > 0
