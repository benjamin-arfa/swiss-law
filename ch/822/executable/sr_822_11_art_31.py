"""SR 822.11 Art. 31 - Mindestalter

Generated from: ch/de/822/822.11.md

Minimum working age:
- Art. 30 Abs. 1: 15 years minimum age for employment
- Art. 30 Abs. 2: 13 years for light work (with restrictions)
- Art. 31: special protection for workers under 18 (young workers)
  including prohibition of dangerous work and health examinations
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_arbeitnehmer(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter des Arbeitnehmers in Jahren"
    reference = "SR 822.11 Art. 30"


class mindestalter_beschaeftigung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestalter fuer die Beschaeftigung (15 Jahre)"
    reference = "SR 822.11 Art. 30 Abs. 1"

    def formula(person, period, parameters):
        return 15


class mindestalter_leichte_arbeit(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestalter fuer leichte Arbeiten (13 Jahre)"
    reference = "SR 822.11 Art. 30 Abs. 2"

    def formula(person, period, parameters):
        return 13


class ist_jugendlicher_arbeitnehmer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen jugendlichen Arbeitnehmer (unter 18) handelt"
    reference = "SR 822.11 Art. 29 Abs. 1"

    def formula(person, period, parameters):
        return person('alter_arbeitnehmer', period) < 18


class beschaeftigung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Beschaeftigung altersgemaess zulaessig ist"
    reference = "SR 822.11 Art. 30"

    def formula(person, period, parameters):
        alter = person('alter_arbeitnehmer', period)
        return alter >= 15
