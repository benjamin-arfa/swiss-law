"""SR 916.402 Art. 18 – Finanzierung (Veterinärwesen)

Generated from: ch/916/de/916.402.md

Ungedeckte Kosten der Weiter- und Fortbildung werden von Bund und
Kantonen je zur Hälfte getragen. Der Kostenanteil der einzelnen Kantone
bemisst sich zu gleichen Teilen nach Bevölkerungszahl und
Grossvieheinheiten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

BUND_ANTEIL = 0.5
KANTONE_ANTEIL = 0.5
BEVOELKERUNG_GEWICHT = 0.5
GROSSVIEHEINHEITEN_GEWICHT = 0.5


class ungedeckte_kosten_weiterbildung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ungedeckte Kosten der Weiter- und Fortbildung (CHF)"
    reference = "SR 916.402 Art. 18 Abs. 2"


class kanton_bevoelkerung_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Kantonsbevölkerung an Gesamtbevölkerung (0-1)"
    reference = "SR 916.402 Art. 18 Abs. 3"


class kanton_grossvieheinheiten_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Grossvieheinheiten des Kantons an Gesamtzahl (0-1)"
    reference = "SR 916.402 Art. 18 Abs. 3"


class bundesanteil_weiterbildungskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bundesanteil an ungedeckten Weiterbildungskosten (CHF)"
    reference = "SR 916.402 Art. 18 Abs. 2"

    def formula(person, period, parameters):
        kosten = person('ungedeckte_kosten_weiterbildung', period)
        return kosten * BUND_ANTEIL


class kantonsanteil_weiterbildungskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil eines einzelnen Kantons an ungedeckten Weiterbildungskosten (CHF)"
    reference = "SR 916.402 Art. 18 Abs. 3"

    def formula(person, period, parameters):
        kosten = person('ungedeckte_kosten_weiterbildung', period)
        bev_anteil = person('kanton_bevoelkerung_anteil', period)
        gve_anteil = person('kanton_grossvieheinheiten_anteil', period)

        total_kantone = kosten * KANTONE_ANTEIL

        # Abs. 3: Zu gleichen Teilen nach Bevölkerung und Grossvieheinheiten
        kantons_schluessel = (
            bev_anteil * BEVOELKERUNG_GEWICHT
            + gve_anteil * GROSSVIEHEINHEITEN_GEWICHT
        )
        return total_kantone * kantons_schluessel
