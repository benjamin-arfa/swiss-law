"""BS 300.100 § 7a

Generated from: ch/bs/de/300.100.md

§ 7a Tagesklinische Angebote: The canton promotes day-clinic offerings to
avoid inpatient treatment. It may pay contributions for costs not covered
by social insurance. The Grosse Rat approves expenditures via framework
spending approval. The Regierungsrat sets conditions and contribution levels.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bs_wohnsitz_bs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Wohnsitz im Kanton Basel-Stadt"
    reference = "BS 300.100 § 7a Abs. 1"


class bs_tagesklinik_beitrag_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Beitrag an tagesklinische Angebote (BS 300.100 § 7a)"
    reference = "BS 300.100 § 7a Abs. 1-2"

    def formula(person, period, parameters):
        wohnsitz = person('bs_wohnsitz_bs', period.this_year)
        # Contributions for residents of BS for day-clinic costs not covered by insurance
        return wohnsitz
