"""SR 672.201 Art. 5 — Dividenden mit Steuerermässigung

Art. 5: Dividenden, für die bei den Gewinnsteuern eine besondere
Steuerermässigung (Art. 69 DBG, Art. 28 Abs. 1 StHG) gewährt wird,
gelten für die Anwendung dieser Verordnung als nicht besteuerte Erträge.

Generated from: ch/672/de/672.201.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dividenden_mit_beteiligungsabzug(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Dividenden mit Beteiligungsabzug/Steuerermässigung (Art. 69 DBG, Art. 28 Abs. 1 StHG)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_5"
    default_value = 0


class dividenden_gelten_als_nicht_besteuert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dividenden gelten als nicht besteuerte Erträge wegen Steuerermässigung (SR 672.201 Art. 5)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_5"

    def formula(person, period, parameters):
        # Art. 5: Dividenden mit besonderer Steuerermässigung (Beteiligungsabzug)
        # gelten als nicht besteuerte Erträge — keine Anrechnung möglich.
        return person('dividenden_mit_beteiligungsabzug', period) > 0
