"""SR 122.1 Art. 4

Generated from: ch/122/de/122.1.md

Referendum, Inkrafttreten und Geltungsdauer: The law is subject to optional
referendum. The Federal Council determines the entry into force. The law
expires five years after entry into force.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_122_1_untersteht_fakultativem_referendum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Gesetz untersteht dem fakultativen Referendum"
    reference = "SR 122.1 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return True


class sr_122_1_geltungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Geltungsdauer des Gesetzes in Jahren ab Inkrafttreten"
    reference = "SR 122.1 Art. 4 Abs. 3"

    def formula(person, period, parameters):
        return 5
