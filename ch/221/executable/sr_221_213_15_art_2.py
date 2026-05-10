"""SR 221.213.15 Art. 2

Generated from: ch/221/de/221.213.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rahmenmietvertrag_schriftliche_form(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rahmenmietvertrag in schriftlicher Form abgefasst"
    reference = "SR 221.213.15 Art. 2"


class rahmenmietvertrag_in_amtssprachen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rahmenmietvertrag in den Amtssprachen des örtlichen Geltungsbereichs abgefasst"
    reference = "SR 221.213.15 Art. 2"


class rahmenmietvertrag_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rahmenmietvertrag ist gültig (Formerfordernisse erfüllt)"
    reference = "SR 221.213.15 Art. 2"

    def formula(person, period, parameters):
        schriftlich = person('rahmenmietvertrag_schriftliche_form', period)
        amtssprachen = person('rahmenmietvertrag_in_amtssprachen', period)
        return schriftlich * amtssprachen
