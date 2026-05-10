"""SR 322.1 Art. 4a

Generated from: ch/322/de/322.1.md

Untersuchungsrichter: Leitet die vorlaeufige Beweisaufnahme und die
Voruntersuchung. Fuehrung ohne Einmischung der militaerischen Vorgesetzten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_untersuchungsrichter_militaer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Untersuchungsrichter in der Militaerjustiz ist"
    reference = "SR 322.1 Art. 4a"


class leitet_vorlaeufige_beweisaufnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person die vorlaeufige Beweisaufnahme leitet"
    reference = "SR 322.1 Art. 4a Abs. 1"

    def formula_2018(person, period, parameters):
        return person('ist_untersuchungsrichter_militaer', period)


class leitet_voruntersuchung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person die Voruntersuchung leitet"
    reference = "SR 322.1 Art. 4a Abs. 1"

    def formula_2018(person, period, parameters):
        return person('ist_untersuchungsrichter_militaer', period)


class untersuchung_ohne_einmischung_vorgesetzter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Untersuchung ohne Einmischung militaerischer Vorgesetzter gefuehrt wird"
    reference = "SR 322.1 Art. 4a Abs. 2"

    def formula_2018(person, period, parameters):
        """Unabhaengigkeit der Untersuchung ist stets gewaehrleistet."""
        return person('ist_untersuchungsrichter_militaer', period)
