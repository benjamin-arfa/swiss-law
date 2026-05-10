"""SR 446.11 Art. 15

Generated from: ch/446/de/446.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_regelmaessiges_angebot_politische_partizipation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein regelmaessiges Angebot zur politischen Partizipation auf Bundesebene"
    reference = "SR 446.11 Art. 15 Bst. a"


class ist_einmaliges_projekt_politische_partizipation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein einmaliges, hoechstens 3 Jahre dauerndes Projekt zur politischen Partizipation"
    reference = "SR 446.11 Art. 15 Bst. b"

    def formula(person, period, parameters):
        einmalig = person('projekt_ist_einmalig', period)
        dauer = person('projekt_dauer_jahre', period)
        return einmalig * (dauer <= 3)


class ist_projekt_politische_partizipation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Qualifiziert als Projekt zur Foerderung der politischen Partizipation nach Art. 10 KJFG"
    reference = "SR 446.11 Art. 15"

    def formula(person, period, parameters):
        regelmaessig = person('ist_regelmaessiges_angebot_politische_partizipation', period)
        einmalig = person('ist_einmaliges_projekt_politische_partizipation', period)
        return regelmaessig + einmalig >= 1
