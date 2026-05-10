"""SR 171.13 Art. 24

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class frist_versand_vorberatung_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in Tagen für den Versand der Ergebnisse der Vorberatung an Ratsmitglieder vor der Behandlung"
    reference = "SR 171.13 Art. 24 Abs. 1"

    def formula(person, period, parameters):
        return 14
