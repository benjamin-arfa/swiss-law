"""SR 813.1 Art. 24

Generated from: ch/813/de/813.1.md

Vorschriften ueber persoenliche und fachliche Voraussetzungen fuer den Umgang
mit besonders gefaehrlichen Stoffen. Bewilligungspflicht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class stoff_hat_besonders_gefaehrliche_eigenschaften(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Stoff besonders gefaehrliche Eigenschaften oder Merkmale aufweist"
    reference = "SR 813.1 Art. 24 Abs. 1"


class hat_erforderliche_sachkenntnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person die erforderlichen Sachkenntnisse fuer den Umgang erlangt hat"
    reference = "SR 813.1 Art. 24 Abs. 2"


class bewilligungspflicht_gefaehrliche_stoffe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Bewilligungspflicht fuer den Umgang mit Stoffen besteht"
    reference = "SR 813.1 Art. 24 Abs. 1"

    def formula(person, period, parameters):
        return person('stoff_hat_besonders_gefaehrliche_eigenschaften', period)


class darf_mit_gefaehrlichen_stoffen_umgehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person mit besonders gefaehrlichen Stoffen umgehen darf"
    reference = "SR 813.1 Art. 24"

    def formula(person, period, parameters):
        braucht_bewilligung = person('bewilligungspflicht_gefaehrliche_stoffe', period)
        hat_kenntnisse = person('hat_erforderliche_sachkenntnisse', period)
        # Darf umgehen wenn: keine Bewilligungspflicht ODER hat Sachkenntnisse
        return (1 - braucht_bewilligung) + braucht_bewilligung * hat_kenntnisse > 0
