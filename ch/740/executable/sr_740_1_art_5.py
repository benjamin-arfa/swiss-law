"""SR 740.1 Art. 5 - Befristete Erhoehung der Gesamttransitabgabe

Generated from: ch/740/de/740.1.md

Der Bundesrat kann den Hoechstsatz der Gesamttransitabgabe fuer eine
alpenquerende Fahrt um hoechstens 12,5 % erhoehen, wenn die
Kapazitaetsauslastung unter 66 % liegt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# Input variables

class kapazitaetsauslastung_schienegueterverkehr(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Kapazitaetsauslastung des alpenquerenden Schienegueterverkehrs (Anteil 0-1)"
    reference = "SR 740.1 Art. 5 Abs. 1"


class preise_eisenbahnverkehrsunternehmen_wettbewerbsfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Die Preise der Eisenbahnverkehrsunternehmen sind wettbewerbsfaehig"
    reference = "SR 740.1 Art. 5 Abs. 1"


class wochen_unter_schwelle(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl aufeinanderfolgende Wochen mit Kapazitaetsauslastung unter 66 %"
    reference = "SR 740.1 Art. 5 Abs. 1"


class gesamttransitabgabe_hoechstsatz(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Aktueller Hoechstsatz der Gesamttransitabgabe fuer eine alpenquerende Fahrt (CHF)"
    reference = "SR 740.1 Art. 5 Abs. 1"


# Computed variables

class erhoehung_transitabgabe_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Befristete Erhoehung der Gesamttransitabgabe ist zulaessig"
    reference = "SR 740.1 Art. 5 Abs. 1"

    def formula(self, period, parameters):
        auslastung = self('kapazitaetsauslastung_schienegueterverkehr', period)
        wettbewerbsfaehig = self('preise_eisenbahnverkehrsunternehmen_wettbewerbsfaehig', period)
        wochen = self('wochen_unter_schwelle', period)
        return (auslastung < 0.66) * wettbewerbsfaehig * (wochen >= 10)


class maximale_erhoehung_transitabgabe(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Maximale Erhoehung der Gesamttransitabgabe (CHF)"
    reference = "SR 740.1 Art. 5 Abs. 1"

    def formula(self, period, parameters):
        hoechstsatz = self('gesamttransitabgabe_hoechstsatz', period)
        zulaessig = self('erhoehung_transitabgabe_zulaessig', period)
        return zulaessig * hoechstsatz * 0.125
