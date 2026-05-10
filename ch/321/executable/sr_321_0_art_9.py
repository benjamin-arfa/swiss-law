"""SR 321.0 Art. 9

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_zum_tatzeitpunkt_mstg(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person zum Zeitpunkt der Tat (in Jahren)"
    reference = "SR 321.0 Art. 9"


class jugendstrafrecht_anwendbar_mstg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Jugendstrafgesetz (JStG) ist anwendbar (Person unter 18 Jahre zum Tatzeitpunkt)"
    reference = "SR 321.0 Art. 9"

    def formula(person, period, parameters):
        alter = person('alter_zum_tatzeitpunkt_mstg', period)
        return alter < 18
