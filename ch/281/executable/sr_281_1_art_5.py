"""SR 281.1 Art. 5

Generated from: ch/281/de/281.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schaden_durch_beamte_widerrechtlich_verursacht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schaden wurde durch Beamte/Angestellte bei Erfüllung ihrer SchKG-Aufgaben widerrechtlich verursacht"
    reference = "SR 281.1 Art. 5 Abs. 1"


class kanton_haftet_fuer_schaden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kanton haftet für den widerrechtlich verursachten Schaden"
    reference = "SR 281.1 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return person('schaden_durch_beamte_widerrechtlich_verursacht', period)


class anspruch_gegen_fehlbaren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Geschädigter hat direkt gegenüber dem Fehlbaren einen Anspruch"
    reference = "SR 281.1 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        # Der Geschädigte hat gegenüber dem Fehlbaren keinen Anspruch
        return person.filled_array(False)
