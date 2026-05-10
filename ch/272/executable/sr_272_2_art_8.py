"""SR 272.2 Art. 8

Generated from: ch/272/de/272.2.md

Anmeldung zu einer oeffentlich zugaenglichen Prozesshandlung:
Anmeldung mindestens 3 Tage vorher. Gericht informiert spaetestens
1 Arbeitstag vorher.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anmeldefrist_oeffentlich_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestanmeldefrist fuer oeffentlich zugaengliche Prozesshandlung in Tagen (3 Tage)"
    reference = "SR 272.2 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return 3


class informationsfrist_gericht_arbeitstage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer Information durch das Gericht in Arbeitstagen vor der Prozesshandlung (1 Tag)"
    reference = "SR 272.2 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        return 1


class anmeldung_rechtzeitig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anmeldung mindestens 3 Tage vor der Prozesshandlung erfolgt ist"
    reference = "SR 272.2 Art. 8 Abs. 1"
