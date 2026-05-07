"""SR 514.544.1 Art. 3

Generated from: ch/514/de/514.544.1.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class waffenhandelspruefung_theorie_dauer_minuten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der theoretischen Pruefung in Minuten (Art. 3 Abs. 1 SR 514.544.1)"
    reference = "SR 514.544.1 Art. 3"

    def formula(person, period, parameters):
        # Die theoretische Pruefung dauert eine Stunde
        return 60
