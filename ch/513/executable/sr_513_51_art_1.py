"""SR 513.51 Art. 1

Generated from: ch/513/de/513.51.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class srk_anerkannt_als_nationale_rotkreuzgesellschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SRK ist als einzige nationale Rotkreuzgesellschaft anerkannt (Art. 1 SR 513.51)"
    reference = "SR 513.51 Art. 1"

    def formula(person, period, parameters):
        # Das SRK ist als einzige nationale Rotkreuzgesellschaft anerkannt
        # und verpflichtet, im Kriegsfall den Sanitaetsdienst der Armee zu unterstuetzen.
        return True
