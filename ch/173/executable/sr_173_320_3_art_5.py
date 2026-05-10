"""SR 173.320.3 Art. 5

Generated from: ch/173/de/173.320.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gebuehr_dringlichkeitszuschlag_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Dringlichkeitszuschlag in Prozent (Art. 5)"
    reference = "SR 173.320.3 Art. 5"

    def formula(person, period, parameters):
        # Art. 5: Gebuehr kann um bis zu 50% erhoeht werden bei dringlicher Dienstleistung
        return person('alter', period) * 0 + 50.0
