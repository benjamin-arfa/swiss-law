"""SR 152.21 Art. 15

Generated from: ch/152/de/152.21.md

Fees: basic services (finding archive material, granting access) are free.
Additional services and reproductions are charged at cost.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_grunddienst_einsichtnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um einen Grunddienst der Einsichtnahme handelt (Ermitteln, Gewaehren)"
    reference = "SR 152.21 Art. 15 Abs. 1"


class grunddienst_unentgeltlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Grunddienst unentgeltlich ist"
    reference = "SR 152.21 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_grunddienst_einsichtnahme', period)


class zusaetzliche_dienstleistung_oder_reproduktion(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine zusaetzliche Dienstleistung oder Reproduktion verlangt wird"
    reference = "SR 152.21 Art. 15 Abs. 2"


class kosten_nach_aufwand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Kosten nach Aufwand in Rechnung gestellt werden"
    reference = "SR 152.21 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        return person('zusaetzliche_dienstleistung_oder_reproduktion', period)
