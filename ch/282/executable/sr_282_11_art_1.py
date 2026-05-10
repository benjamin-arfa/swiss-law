"""SR 282.11 Art. 1 - Anwendungsbereich

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class schuldner_ist_gemeinde_oder_koerperschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Schuldner ist eine Gemeinde oder andere Koerperschaft des kantonalen oeffentlichen Rechts"
    reference = "SR 282.11 Art. 1 Abs. 1"


class schuldner_ist_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Schuldner ist ein Kanton"
    reference = "SR 282.11 Art. 1 Abs. 2"


# Computed variables

class gesetz_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Gesetz ueber die Schuldbetreibung gegen Gemeinden ist anwendbar"
    reference = "SR 282.11 Art. 1"

    def formula(self, period, parameters):
        gemeinde = self('schuldner_ist_gemeinde_oder_koerperschaft', period)
        kanton = self('schuldner_ist_kanton', period)
        # Anwendbar auf Gemeinden und Koerperschaften, nicht auf Kantone
        return gemeinde * (1 - kanton)
