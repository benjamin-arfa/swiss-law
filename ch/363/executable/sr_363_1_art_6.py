"""SR 363.1 Art. 6

Generated from: ch/363/de/363.1.md

Aufbewahrung und Vernichtung des Analysematerials.
Aufbewahrungsfrist: 15 Jahre nach Eingang der Probe.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class spur_dna_eingang_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des Eingangs der Spurenprobe im Labor"
    reference = "SR 363.1 Art. 6 Abs. 2"


class spur_straftat_unverjaehrbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Straftat ist unverjaehrbar"
    reference = "SR 363.1 Art. 6 Abs. 2"


class spur_verlaengerung_verfolgungsverjaehrung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsfrist wurde bis zum Ablauf der Verfolgungsverjaehrung verlaengert"
    reference = "SR 363.1 Art. 6 Abs. 2"


class spur_dna_aufbewahrungsfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer die aus der Spur extrahierte DNA (Jahre)"
    reference = "SR 363.1 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        # Standard: 15 Jahre, Ausnahme: unverjaehrbare Straftaten (unbegrenzt)
        unverjaehrbar = person('spur_straftat_unverjaehrbar', period)
        # Fuer unverjaehrbare Straftaten: 999 als Platzhalter fuer unbegrenzt
        return where(unverjaehrbar, 999, 15)
