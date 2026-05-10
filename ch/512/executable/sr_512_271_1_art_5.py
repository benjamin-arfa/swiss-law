"""SR 512.271.1 Art. 5 – Trainingsunterbruch

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


class flugdienst_kategorie(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Kategorie im militärischen Flugdienst (z.B. kampfflugzeug, helikopter, propeller, bordoperateur, drohne, fallschirmaufklaerer)"
    reference = "SR 512.271.1 Art. 5"
    default_value = ""


class maximaler_trainingsunterbruch_wochen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximal zulässiger Trainingsunterbruch in Kalenderwochen"
    reference = "SR 512.271.1 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        kat = person('flugdienst_kategorie', period)

        # Art. 5 Abs. 1:
        # a. Kampfflugzeuge: 6 Wochen
        # b. Helikopter: 8 Wochen
        # c. Propellerflugzeuge: 8 Wochen
        # d. Bordoperateure: 8 Wochen
        # e. Drohnenoperateure: 8 Wochen
        # f. Fallschirmaufklärer: 12 Wochen
        return (
            where(kat == 'kampfflugzeug', 6,
            where(kat == 'helikopter', 8,
            where(kat == 'propeller', 8,
            where(kat == 'bordoperateur', 8,
            where(kat == 'drohne', 8,
            where(kat == 'fallschirmaufklaerer', 12, 0))))))
        )
