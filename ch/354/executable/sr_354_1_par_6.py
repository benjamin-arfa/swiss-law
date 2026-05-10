"""SR 354.1 § 6

Generated from: ch/354/de/354.1.md
Transport escort costs with specific fee amounts.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class begleitung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Transportbegleitung ist notwendig (Gefaehrlichkeit, Zustand der Person)"
    reference = "SR 354.1 § 6 Abs. 1"


class transport_distanz_bahn_km(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Distanz des Transports per Bahn oder Auto in Kilometern"
    reference = "SR 354.1 § 6 Abs. 3 Ziff. 1"


class transport_distanz_fuss_km(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Distanz des Transports zu Fuss in Kilometern"
    reference = "SR 354.1 § 6 Abs. 3 Ziff. 1"


class begleiter_ruecktransport(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Begleiter muss Person an Ausgangsort zurueckbringen oder andere Person mitnehmen"
    reference = "SR 354.1 § 6 Abs. 3 Ziff. 1"


class begleiter_hauptmahlzeiten_auswaerts(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Hauptmahlzeiten die der Begleiter auswaerts einnehmen muss (0, 1 oder 2)"
    reference = "SR 354.1 § 6 Abs. 3 Ziff. 1"


class begleiter_nachtquartier(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nachtquartier fuer Transportbegleiter erforderlich"
    reference = "SR 354.1 § 6 Abs. 3 Ziff. 2"


class transportgebuehr_begleitung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Transportgebuehr fuer die Begleitung (Hinreise) in CHF"
    reference = "SR 354.1 § 6 Abs. 3 Ziff. 1"

    def formula(person, period):
        bahn_km = person('transport_distanz_bahn_km', period)
        fuss_km = person('transport_distanz_fuss_km', period)
        ruecktransport = person('begleiter_ruecktransport', period)
        mahlzeiten = person('begleiter_hauptmahlzeiten_auswaerts', period)

        # 20 Rp fuer die ersten 30 km Bahn/Auto, 10 Rp fuer jeden weiteren km
        bahn_gebuehr = where(
            bahn_km <= 30,
            bahn_km * 0.20,
            30 * 0.20 + (bahn_km - 30) * 0.10
        )

        # 60 Rp pro km zu Fuss
        fuss_gebuehr = fuss_km * 0.60

        gebuehr = bahn_gebuehr + fuss_gebuehr

        # Minimum 4 CHF, Maximum 24 CHF (Standardfall)
        gebuehr = max_(gebuehr, 4.0)
        gebuehr = min_(gebuehr, 24.0)

        # Bei Ruecktransport: erhoehtes Minimum
        # 6 CHF Minimum bei 1 Hauptmahlzeit, 9.75 CHF bei 2 Hauptmahlzeiten
        min_rueck = where(
            mahlzeiten >= 2, 9.75,
            where(mahlzeiten >= 1, 6.0, 6.0)
        )
        gebuehr = where(ruecktransport, max_(gebuehr, min_rueck), gebuehr)

        return gebuehr


class nachtquartier_entschaedigung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Entschaedigung fuer Nachtquartier des Transportbegleiters in CHF"
    reference = "SR 354.1 § 6 Abs. 3 Ziff. 2"

    def formula(person, period):
        nachtquartier = person('begleiter_nachtquartier', period)
        return where(nachtquartier, 12.0, 0.0)


class gesamtkosten_begleitung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtkosten der Transportbegleitung in CHF (Transportgebuehr + Nachtquartier + Fahrkosten)"
    reference = "SR 354.1 § 6 Abs. 3"

    def formula(person, period):
        transportgebuehr = person('transportgebuehr_begleitung', period)
        nachtquartier = person('nachtquartier_entschaedigung', period)
        # Note: Fahrkosten (Ziff. 3) = halber Preis Billette 2. oder 1. Klasse
        # are external inputs not encoded here as they depend on rail pricing
        return transportgebuehr + nachtquartier
