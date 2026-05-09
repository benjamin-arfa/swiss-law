"""SR 810.211 Art. 10

Generated from: ch/810/de/810.211.md

Art. 10: Abklaerung betreffend Freiwilligkeit und Unentgeltlichkeit
der Lebendspende.

Abs. 1: Einer lebenden Person duerfen Organe, Gewebe oder Zellen nur
entnommen werden, wenn eine unabhaengige und erfahrene Fachperson
sich vergewissert hat, dass die Spende freiwillig und unentgeltlich
erfolgt.

Abs. 2: Die Fachperson muss die Abklaerung dokumentieren und die
Unterlagen getrennt von der Krankengeschichte waehrend 10 Jahren
aufbewahren.

Abs. 3: Wird die Person als Spender/in abgelehnt, hat sie das Recht,
eine Zweitmeinung einzuholen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class unabhaengige_fachperson_geprueft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Unabhaengige Fachperson hat Freiwilligkeit und Unentgeltlichkeit geprueft"
    reference = "SR 810.211 Art. 10 Abs. 1"


class spende_freiwillig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Die Spende erfolgt freiwillig"
    reference = "SR 810.211 Art. 10 Abs. 1"


class spende_unentgeltlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Die Spende erfolgt unentgeltlich"
    reference = "SR 810.211 Art. 10 Abs. 1"


class abklaerung_dokumentiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Abklaerung ist dokumentiert und getrennt von Krankengeschichte aufbewahrt"
    reference = "SR 810.211 Art. 10 Abs. 2"


class entnahme_lebendspende_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Entnahme bei lebender Person ist zulaessig (Art. 10 Abs. 1)"
    reference = "SR 810.211 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        fachperson = person('unabhaengige_fachperson_geprueft', period)
        freiwillig = person('spende_freiwillig', period)
        unentgeltlich = person('spende_unentgeltlich', period)
        return fachperson * freiwillig * unentgeltlich


class recht_auf_zweitmeinung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person hat nach Ablehnung als Spender/in das Recht auf eine Zweitmeinung"
    reference = "SR 810.211 Art. 10 Abs. 3"

    def formula(person, period, parameters):
        # Recht besteht immer wenn als Spender/in abgelehnt
        return person('als_spender_abgelehnt', period)


class als_spender_abgelehnt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person wurde als Lebendspender/in abgelehnt"
    reference = "SR 810.211 Art. 10 Abs. 3"
