"""SR 512.271.1 Art. 10 – Kürzung der Entschädigung

Generated from: ch/512/de/512.271.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class trainingsunterbruch_ueberschritten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zulässiger Trainingsunterbruch wurde unentschuldigt überschritten"
    reference = "SR 512.271.1 Art. 10 Abs. 2"
    default_value = False


class trainingspflicht_wochen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Trainingspflicht in Wochen pro Jahr"
    reference = "SR 512.271.1 Art. 10 Abs. 2"
    default_value = 0


class kuerzung_anteil_entschaedigung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kürzungsanteil der Entschädigung bei Überschreitung des Trainingsunterbruchs"
    reference = "SR 512.271.1 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        ueberschritten = person('trainingsunterbruch_ueberschritten', period)
        pflicht = person('trainingspflicht_wochen', period)

        # Art. 10 Abs. 2:
        # Piloten 4-Wochen-Pflicht: 1/12
        # Piloten 6-Wochen-Pflicht: 1/8
        # Piloten 8-Wochen-Pflicht: 1/6
        # Bordoperateure: 1/6
        # Fallschirmaufklärer: 1/6
        # Drohnenoperateure: 1/6
        anteil = where(pflicht == 4, 1.0 / 12.0,
                 where(pflicht == 6, 1.0 / 8.0,
                 where(pflicht >= 8, 1.0 / 6.0, 0.0)))

        return where(ueberschritten, anteil, 0.0)
