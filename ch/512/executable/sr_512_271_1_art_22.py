"""SR 512.271.1 Art. 22 – Flugstunden

Generated from: ch/512/de/512.271.1.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class flugstunden_anpassung_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anpassung der Flugstunden in Prozent (max. ±25%)"
    reference = "SR 512.271.1 Art. 22"
    default_value = 0.0


class flugstunden_nach_anpassung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Effektive minimale Flugstunden nach Anpassung durch Luftwaffe"
    reference = "SR 512.271.1 Art. 22"

    def formula(person, period, parameters):
        basis = person('minimale_flugstunden', period)
        anpassung = person('flugstunden_anpassung_prozent', period)

        # Anpassung höchstens ±25%
        anpassung_begrenzt = max_(min_(anpassung, 25.0), -25.0)

        return basis * (1.0 + anpassung_begrenzt / 100.0)
