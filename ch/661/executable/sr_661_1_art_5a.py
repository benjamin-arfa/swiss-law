"""SR 661.1 Art. 5a

Generated from: ch/661/de/661.1.md

Art. 5a Anrechnung von Schutzdienstleistungen (Credit for civil protection service):
1. Civil protection service members receive a 4% reduction of the substitute
   levy per day of paid service in the levy year.
2. Service days before the start of the obligation are also credited.
3. If 100% reduction is reached and creditable days remain, they carry over
   to the following year.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wpev_schutzdiensttage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Number of paid civil protection service days in the levy year"
    reference = "SR 661.1 Art. 5a Abs. 1"


class wpev_uebertragene_schutzdiensttage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Civil protection service days carried over from previous year"
    reference = "SR 661.1 Art. 5a Abs. 3"


class wpev_schutzdienst_ermaessigung_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Percentage reduction of substitute levy due to civil protection service (max 100%)"
    reference = "SR 661.1 Art. 5a Abs. 1"

    def formula(person, period, parameters):
        tage = person('wpev_schutzdiensttage', period)
        uebertrag = person('wpev_uebertragene_schutzdiensttage', period)
        satz_pro_tag = parameters(period).sr_661_1.schutzdienst_ermaessigung_pro_tag
        total_tage = tage + uebertrag
        return min_(total_tage * satz_pro_tag, 1.0)


class wpev_verbleibende_schutzdiensttage_uebertrag(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Remaining civil protection days to carry over to next year (after 100% reached)"
    reference = "SR 661.1 Art. 5a Abs. 3"

    def formula(person, period, parameters):
        tage = person('wpev_schutzdiensttage', period)
        uebertrag = person('wpev_uebertragene_schutzdiensttage', period)
        satz_pro_tag = parameters(period).sr_661_1.schutzdienst_ermaessigung_pro_tag
        total_tage = tage + uebertrag
        tage_fuer_100 = 25  # 100% / 4% = 25 days
        return max_(total_tage - tage_fuer_100, 0)
