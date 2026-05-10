"""SR 171.13 Art. 8

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_praesidiumsmitglieder_im_buero(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Präsidiumsmitglieder im Büro des Nationalrates"
    reference = "SR 171.13 Art. 8 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        return 3


class anzahl_stimmenzaehler_im_buero(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Stimmenzählerinnen oder Stimmenzähler im Büro"
    reference = "SR 171.13 Art. 8 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        return 4


class praesident_hat_stichentscheid_buero(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Präsident stimmt im Büro mit und hat bei Stimmengleichheit den Stichentscheid"
    reference = "SR 171.13 Art. 8 Abs. 4"

    def formula(person, period, parameters):
        return True
