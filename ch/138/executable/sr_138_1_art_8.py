"""SR 138.1 Art. 8

Generated from: ch/138/de/138.1.md

Referendum und Inkrafttreten: The law is subject to optional referendum.
The Federal Council determines entry into force.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class sr_138_1_untersteht_fakultativem_referendum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Bundesgesetz ueber die Mitwirkung der Kantone untersteht dem fakultativen Referendum"
    reference = "SR 138.1 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return True
