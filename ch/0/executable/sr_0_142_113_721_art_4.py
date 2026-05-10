"""SR 0.142.113.721 Art. 4

Generated from: ch/0/de/0.142.113.721.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class protection_of_citizens(Variable):
    value_type = bool
    entity = Person
    default_value = False
    label = "Protection and access to justice for citizens (Art. 4 SR 0.142.113.721)"

    def formula(person, period, parameters):
        resided_in_ch = person("resides_in_switzerland", period)
        return resided_in_ch
