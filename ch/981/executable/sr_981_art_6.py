"""SR 981 Art. 6

Generated from: ch/de/981.md

Applicable law: the Commission executes compensation agreements
according to the agreements themselves, federal law, and general
principles of international law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vollzug_nach_abkommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission die Abkommen nach deren Bestimmungen vollzieht"
    reference = "SR 981 Art. 6"

    def formula(person, period, parameters):
        return True


class vollzug_nach_bundesrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission die Abkommen nach den Vorschriften des Bundesrechts vollzieht"
    reference = "SR 981 Art. 6"

    def formula(person, period, parameters):
        return True


class vollzug_nach_voelkerrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission die allgemeinen Grundsaetze des Voelkerrechts anwendet"
    reference = "SR 981 Art. 6"

    def formula(person, period, parameters):
        return True
