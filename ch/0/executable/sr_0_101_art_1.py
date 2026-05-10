"""SR 0.101 Art. 1

Generated from: ch/0/de/0.101.md

Obligation to respect human rights: The High Contracting Parties shall
secure to everyone within their jurisdiction the rights and freedoms
defined in Section I of the Convention.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_hoheitsgewalt_unterstellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person der Hoheitsgewalt einer Vertragspartei der EMRK untersteht"
    reference = "SR 0.101 Art. 1"


class emrk_rechte_und_freiheiten_gesichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Person die in Abschnitt I EMRK bestimmten Rechte und Freiheiten zugesichert sind"
    reference = "SR 0.101 Art. 1"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)
