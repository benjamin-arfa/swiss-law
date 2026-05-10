"""SR 641.51 Art. 13

Generated from: ch/641/de/641.51.md

Automobilsteuer - Steuersatz:
Die Steuer betraegt 4 Prozent.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class astg_steuerbarer_wert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Steuerbarer Wert des Automobils (CHF)"
    reference = "SR 641.51 Art. 13"


class astg_steuerbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der Automobilsteuer (CHF) = 4% des steuerbaren Wertes"
    reference = "SR 641.51 Art. 13"

    def formula(person, period, parameters):
        wert = person('astg_steuerbarer_wert', period)
        befreit = person('astg_steuerbefreit', period)
        satz = parameters(period).sr_641_51.steuersatz
        return where(befreit, 0, wert * satz)
