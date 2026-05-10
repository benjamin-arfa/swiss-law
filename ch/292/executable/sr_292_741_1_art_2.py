"""SR 292.741.1 Art. 2

Generated from: ch/292/de/292.741.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class frist_beschwerde_gegen_einsprache_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in Tagen für verwaltungsgerichtliche Beschwerde gegen die Einsprache"
    reference = "SR 292.741.1 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return 30


class arrest_faellt_dahin_ohne_beschwerde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Arrest fällt dahin wenn keine Beschwerde erhoben oder diese abgewiesen wird"
    reference = "SR 292.741.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return True
