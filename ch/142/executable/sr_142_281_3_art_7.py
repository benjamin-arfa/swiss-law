"""SR 142.281.3 Art. 7

Generated from: ch/142/de/142.281.3.md

Berechnungsformel fuer die Platzkostenpauschale bei Neubauten:
1. Fuer jeden Bereich: Bereichsquadratmeter * Bereichspreis
2. Summe aller Produkte
3. Summe + prozentualer Anteil Umgebungsarbeiten + prozentualer Anteil
   Ausstattungskosten + Sicherheitszuschlag
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class summe_bereichskosten_neubau(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Summe der Bereichskosten pro Haftplatz bei Neubau (CHF)"
    reference = "SR 142.281.3 Art. 7"

    def formula(person, period, parameters):
        # Schritt 1+2: Fuer jeden Bereich Flaeche * Preis, dann addieren
        return (
            person('bereich_sicherheit_flaeche', period) * 5300
            + person('bereich_verwaltung_flaeche', period) * 5300
            + person('bereich_migrationsbehoerden_flaeche', period) * 5300
            + person('bereich_personal_flaeche', period) * 5100
            + person('bereich_insassenwesen_flaeche', period) * 5100
            + person('bereich_aufnahme_austritt_flaeche', period) * 5100
            + person('bereich_transport_flaeche', period) * 5100
            + person('bereich_wohnen_flaeche', period) * 6700
            + person('bereich_beschaeftigung_flaeche', period) * 3600
            + person('bereich_hauswirtschaft_flaeche', period) * 6700
        )


class platzkostenpauschale_neubau(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Platzkostenpauschale pro Haftplatz bei Neubau (CHF)"
    reference = "SR 142.281.3 Art. 7"

    def formula(person, period, parameters):
        summe = person('summe_bereichskosten_neubau', period)
        zuschlag_umgebung = person('zuschlag_umgebungsarbeiten_prozent', period) / 100
        zuschlag_ausstattung = person('zuschlag_ausstattungskosten_prozent', period) / 100
        sicherheit = person('sicherheitszuschlag_pro_haftplatz', period)

        # Schritt 3: Summe + Umgebung + Ausstattung + Sicherheitszuschlag
        return summe * (1 + zuschlag_umgebung + zuschlag_ausstattung) + sicherheit
