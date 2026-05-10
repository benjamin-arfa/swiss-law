"""SR 831.30 Art. 13

Generated from: ch/831/de/831.30.md

Art. 13: Finanzierung - Financing of annual supplementary benefits:
- Abs. 1: 5/8 by the Confederation, 3/8 by the cantons.
- Abs. 2: For persons in homes/hospitals, the Confederation bears 5/8 of
  the EL insofar as the sum of general living costs (Art. 10(1)(a)(1)),
  CHF 13,200 for rent, and recognized expenses (Art. 10(3)) are not
  covered by countable income. The cantons bear the rest.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_bundesanteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bundesanteil an der jaehrlichen Ergaenzungsleistung (Art. 13 Abs. 1 ELG)"
    reference = "SR 831.30 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        el = person('el_jaehrliche_el_berechnet', period)
        return el * (5.0 / 8.0)


class el_kantonsanteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kantonsanteil an der jaehrlichen Ergaenzungsleistung (Art. 13 Abs. 1 ELG)"
    reference = "SR 831.30 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        el = person('el_jaehrliche_el_berechnet', period)
        return el * (3.0 / 8.0)
