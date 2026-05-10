"""SR 531.211.36 Art. 8

Generated from: ch/531/de/531.211.36.md
Penal provisions: Violations of this ordinance are punished
under Art. 49 LVG (SR 531).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class subject_to_stockpile_penal_provisions(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether violations of stockpile ordinance are subject to penalties under Art. 49 LVG"
    reference = "SR 531.211.36 Art. 8"

    def formula(person, period, parameters):
        violated = person("violated_stockpile_ordinance", period)
        return violated
