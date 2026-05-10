"""SR 453.0 Art. 57

Generated from: ch/453/de/453.0.md
Archivierung und Loeschung - Daten zu Bewilligungen nicht geloescht; abgelehnte nach 30 Jahren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuch_bewilligt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesuch wurde bewilligt (erteilte Bewilligung)"
    reference = "SR 453.0 Art. 57 Abs. 2"


class gesuch_abgelehnt_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der Ablehnung des Gesuchs"
    reference = "SR 453.0 Art. 57 Abs. 2"


class daten_zu_loeschen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten sind zu loeschen"
    reference = "SR 453.0 Art. 57 Abs. 2"

    def formula(person, period, parameters):
        bewilligt = person('gesuch_bewilligt', period)
        abgelehnt_jahr = person('gesuch_abgelehnt_jahr', period)
        aktuelles_jahr = period.start.year

        # Bewilligte Gesuche: Daten werden NICHT geloescht
        # Abgelehnte Gesuche: nach 30 Jahren loeschen
        return not_(bewilligt) * ((aktuelles_jahr - abgelehnt_jahr) > 30)
