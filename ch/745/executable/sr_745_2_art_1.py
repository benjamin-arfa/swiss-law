"""SR 745.2 Art. 1

Generated from: ch/745/de/745.2.md

Bundesgesetz ueber die Sicherheitsorgane der Transportunternehmen im
oeffentlichen Verkehr (BGST) - Gegenstand und Geltungsbereich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class unterliegt_bgst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen unterliegt dem Bundesgesetz ueber die Sicherheitsorgane der Transportunternehmen (BGST, SR 745.2)"
    reference = "SR 745.2 Art. 1"

    def formula(person, period, parameters):
        return person('hat_personenbefoerderungskonzession', period)
