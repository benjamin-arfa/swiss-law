"""SR 453.2 Art. 9

Generated from: ch/453/de/453.2.md
Voranmeldung - 3 Arbeitstage vor Einfuhr.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class arbeitstage_vor_einfuhr(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Arbeitstage zwischen Voranmeldung und geplanter Einfuhr"
    reference = "SR 453.2 Art. 9 Abs. 1"


class voranmeldefrist_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Voranmeldefrist (mind. 3 Arbeitstage) eingehalten"
    reference = "SR 453.2 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        tage = person('arbeitstage_vor_einfuhr', period)
        return tage >= 3
