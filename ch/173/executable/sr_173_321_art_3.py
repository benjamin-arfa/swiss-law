"""SR 173.321 Art. 3

Generated from: ch/173/de/173.321.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class max_vollzeitstellen_bvger_uebergang(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Vollzeitstellen BVGer uebergangsweise bis 31.12.2029 (Art. 3)"
    reference = "SR 173.321 Art. 3"

    def formula(person, period, parameters):
        # Art. 3: Bis 31.12.2029 max. 70 Stellen, danach 65
        jahr = period.start.year
        return where(jahr <= 2029, 70, 65)
