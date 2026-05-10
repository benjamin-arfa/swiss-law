"""SR 810.211 Art. 8

Generated from: ch/810/de/810.211.md

Art. 8: Dauer der vorbereitenden medizinischen Massnahmen.

Vorbereitende medizinische Massnahmen duerfen nach dem Tod der
Patientin oder des Patienten waehrend laengstens 72 Stunden
durchgefuehrt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stunden_seit_tod(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Stunden seit dem Tod der Patientin oder des Patienten"
    reference = "SR 810.211 Art. 8"


class vorbereitende_massnahmen_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vorbereitende medizinische Massnahmen sind noch zulaessig (max. 72 Stunden nach Tod)"
    reference = "SR 810.211 Art. 8"

    def formula(person, period, parameters):
        stunden = person('stunden_seit_tod', period)
        max_stunden = parameters(period).sr_810_211.art_8.max_stunden_vorbereitende_massnahmen
        return stunden <= max_stunden
