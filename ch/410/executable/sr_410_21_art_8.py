"""SR 410.21 Art. 8

Generated from: ch/410/de/410.21.md

Finanzierung - Bund und Kantone je zur Haelfte.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesamtkosten_bildungszusammenarbeit(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtkosten der Grundlagen-/Entwicklungsarbeiten und gemeinsamen Institutionen"
    reference = "SR 410.21 Art. 8 Abs. 1"


class anteil_bund_bildungszusammenarbeit(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil des Bundes an den Kosten der Bildungszusammenarbeit"
    reference = "SR 410.21 Art. 8 Abs. 1"

    def formula(person, period):
        kosten = person('gesamtkosten_bildungszusammenarbeit', period)
        # Bund und Kantone beteiligen sich je zur Haelfte
        return kosten * 0.50


class anteil_kantone_bildungszusammenarbeit(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Kantone an den Kosten der Bildungszusammenarbeit"
    reference = "SR 410.21 Art. 8 Abs. 1"

    def formula(person, period):
        kosten = person('gesamtkosten_bildungszusammenarbeit', period)
        # Bund und Kantone beteiligen sich je zur Haelfte
        return kosten * 0.50
