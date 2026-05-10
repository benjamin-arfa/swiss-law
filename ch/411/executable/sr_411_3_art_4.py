"""SR 411.3 Art. 4

Generated from: ch/411/de/411.3.md

Hoehe der Beitraege und Bemessung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class anrechenbare_betriebskosten_jahr_1(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Betriebskosten des 1. vorangegangenen Rechnungsjahrs"
    reference = "SR 411.3 Art. 4 Abs. 2 Bst. a"


class anrechenbare_betriebskosten_jahr_2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Betriebskosten des 2. vorangegangenen Rechnungsjahrs"
    reference = "SR 411.3 Art. 4 Abs. 2 Bst. a"


class anrechenbare_betriebskosten_jahr_3(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Betriebskosten des 3. vorangegangenen Rechnungsjahrs"
    reference = "SR 411.3 Art. 4 Abs. 2 Bst. a"


class anrechenbare_betriebskosten_jahr_4(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Betriebskosten des 4. vorangegangenen Rechnungsjahrs"
    reference = "SR 411.3 Art. 4 Abs. 2 Bst. a"


class anzahl_schueler_art1(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Schueler/innen, die Kinder von Angestellten nach Art. 1 Abs. 2 Bst. a sind"
    reference = "SR 411.3 Art. 4 Abs. 2 Bst. b"


class gesamtschuelerschaft(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtzahl der Schueler/innen an der ECLF"
    reference = "SR 411.3 Art. 4 Abs. 2 Bst. b"


# --- Computed variables ---

class durchschnitt_anrechenbare_betriebskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Durchschnitt der anrechenbaren Betriebskosten der 4 vorangegangenen Jahre"
    reference = "SR 411.3 Art. 4 Abs. 2 Bst. a"

    def formula(person, period):
        k1 = person('anrechenbare_betriebskosten_jahr_1', period)
        k2 = person('anrechenbare_betriebskosten_jahr_2', period)
        k3 = person('anrechenbare_betriebskosten_jahr_3', period)
        k4 = person('anrechenbare_betriebskosten_jahr_4', period)
        return (k1 + k2 + k3 + k4) / 4


class anteil_art1_schueler(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Art.1-Schueler an der Gesamtschuelerschaft"
    reference = "SR 411.3 Art. 4 Abs. 2 Bst. b"

    def formula(person, period):
        art1 = person('anzahl_schueler_art1', period)
        gesamt = person('gesamtschuelerschaft', period)
        return where(gesamt > 0, art1 / gesamt, 0.0)


class maximaler_bundesbeitrag_eclf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Bundesbeitrag (25% der anrechenbaren Betriebskosten)"
    reference = "SR 411.3 Art. 4 Abs. 1"

    def formula(person, period):
        durchschnitt = person('durchschnitt_anrechenbare_betriebskosten', period)
        return durchschnitt * 0.25


class bundesbeitrag_eclf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Berechneter Bundesbeitrag an die ECLF"
    reference = "SR 411.3 Art. 4"

    def formula(person, period):
        max_beitrag = person('maximaler_bundesbeitrag_eclf', period)
        anteil = person('anteil_art1_schueler', period)
        # Beitrag bemisst sich nach dem Anteil der Art.1-Schueler
        return max_beitrag * anteil
