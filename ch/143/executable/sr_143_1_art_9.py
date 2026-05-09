"""SR 143.1 Art. 9 - Gebuehr (Fees)

Generated from: ch/143/de/143.1.md

The Federal Council regulates fee obligations, affected persons, and fee amounts.
Fees must be family-friendly (Art. 9 Abs. 2).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ausweis_gebuehrenpflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob fuer den Ausweis eine Gebuehr erhoben wird"
    reference = "SR 143.1 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return True


class ausweis_gebuehr_ist_familienfreundlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gebuehrenhoehe familienfreundlich sein muss"
    reference = "SR 143.1 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        # Gesetzliche Anforderung seit 1. Maerz 2010
        return True
