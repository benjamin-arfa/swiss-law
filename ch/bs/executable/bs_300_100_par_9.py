"""BS 300.100 § 9

Generated from: ch/bs/de/300.100.md

§ 9 Grundsatz (Spitalexterne Pflege): The canton provides outpatient care
in cooperation with private institutions. It promotes home care, outreach
services, and day/night care for BS residents who cannot perform activities
themselves due to health or age. Contributions per social insurance law.
The Regierungsrat sets conditions and amounts for homemaking and day/night care.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bs_gesundheitlich_oder_altersbedingt_eingeschraenkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Aus gesundheitlichen oder altersbedingten Gruenden eingeschraenkt (BS 300.100 § 9 Abs. 2)"
    reference = "BS 300.100 § 9 Abs. 2"


class bs_spitalexterne_pflege_beitrag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Beitraege an spitalexterne Pflege (BS 300.100 § 9)"
    reference = "BS 300.100 § 9 Abs. 3"

    def formula(person, period, parameters):
        wohnsitz = person('bs_wohnsitz_bs', period.this_year)
        eingeschraenkt = person('bs_gesundheitlich_oder_altersbedingt_eingeschraenkt', period)
        return wohnsitz * eingeschraenkt
