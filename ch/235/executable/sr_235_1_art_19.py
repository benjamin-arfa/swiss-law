"""SR 235.1 Art. 19

Generated from: ch/235/de/235.1.md

Bekanntgabe von Personendaten durch Bundesorgane.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_empfaenger_benoetigt_daten_gesetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten sind fuer den Empfaenger zur Erfuellung seiner gesetzlichen Aufgabe unentbehrlich"
    reference = "SR 235.1 Art. 19 Abs. 1 lit. a"


class dsg_betroffene_hat_eingewilligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Betroffene Person hat im Einzelfall eingewilligt"
    reference = "SR 235.1 Art. 19 Abs. 1 lit. b"


class dsg_bekanntgabe_bundesorgan_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bekanntgabe von Personendaten durch Bundesorgan ist zulaessig"
    reference = "SR 235.1 Art. 19"

    def formula(person, period, parameters):
        rechtsgrundlage = person('dsg_gesetzliche_grundlage_vorhanden', period)
        empfaenger = person('dsg_empfaenger_benoetigt_daten_gesetzlich', period)
        eingewilligt = person('dsg_betroffene_hat_eingewilligt', period)
        zugaenglich = person('dsg_daten_allgemein_zugaenglich_gemacht', period)
        return (rechtsgrundlage + empfaenger + eingewilligt + zugaenglich) > 0
