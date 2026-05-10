"""SR 354.1 § 5

Generated from: ch/354/de/354.1.md
Billing rules for police transport costs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transportand_kann_kosten_tragen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Transportand ist in der Lage, Kosten ganz oder teilweise zu bezahlen"
    reference = "SR 354.1 § 5 Abs. 4"


class eigenanteil_transportand(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Betrag den der Transportand selbst bezahlen kann in CHF"
    reference = "SR 354.1 § 5 Abs. 4"


class bundesrechnung_abzug(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Abzug bei Rechnungsstellung an Bund (Kat. II) wegen Eigenzahlung des Transportanden in CHF"
    reference = "SR 354.1 § 5 Abs. 4"

    def formula(person, period):
        kategorie = person('transportkategorie', period)
        kann_zahlen = person('transportand_kann_kosten_tragen', period)
        eigenanteil = person('eigenanteil_transportand', period)
        # Nur bei Kategorie II (Abschiebung ins Ausland, Bund traegt Kosten)
        # und nur wenn Transportand nicht als Arrestant gefuehrt wird
        nicht_arrestant = person('ist_nicht_arrestant', period)
        return where(
            (kategorie == 2) * kann_zahlen * nicht_arrestant,
            eigenanteil,
            0.0
        )


class ist_nicht_arrestant(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Transportand wird nicht als Arrestant gefuehrt"
    reference = "SR 354.1 § 5 Abs. 4"
    default_value = True
