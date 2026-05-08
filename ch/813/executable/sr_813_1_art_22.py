"""SR 813.1 Art. 22

Generated from: ch/813/de/813.1.md

Ruecknahme- und Rueckgabepflicht: Wer gefaehrliche Stoffe abgibt, ist zur
Ruecknahme von nicht gewerblichen Verwendern verpflichtet. Kleinmengen kostenlos.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gibt_gefaehrliche_stoffe_ab(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person gefaehrliche Stoffe oder Zubereitungen abgibt"
    reference = "SR 813.1 Art. 22 Abs. 1"


class ist_nicht_gewerblicher_verwender(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person nicht gewerbliche Verwenderin oder Verwender ist"
    reference = "SR 813.1 Art. 22 Abs. 1"


class ist_kleinmenge(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um Kleinmengen handelt"
    reference = "SR 813.1 Art. 22 Abs. 1"


class ruecknahmepflicht_gefaehrliche_stoffe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person zur Ruecknahme gefaehrlicher Stoffe verpflichtet ist"
    reference = "SR 813.1 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        return person('gibt_gefaehrliche_stoffe_ab', period)


class rueckgabe_kostenlos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Rueckgabe kostenlos sein muss"
    reference = "SR 813.1 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_kleinmenge', period) * person('ist_nicht_gewerblicher_verwender', period)
