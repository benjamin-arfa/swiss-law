"""SR 419.1 Art. 10

Generated from: ch/419/de/419.1.md

Voraussetzungen fuer die Ausrichtung von Finanzhilfen durch den Bund.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class oeffentliches_interesse_an_weiterbildung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Oeffentliches Interesse an der Weiterbildung besteht"
    reference = "SR 419.1 Art. 10 Abs. 1 Bst. a"


class angebot_ohne_finanzhilfe_nicht_ausreichend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebot kommt ohne Finanzhilfen nicht oder nicht ausreichend zustande"
    reference = "SR 419.1 Art. 10 Abs. 1 Bst. b"


class ziele_und_kriterien_festgelegt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ziele und Kriterien der staatlichen Unterstuetzung sind festgelegt"
    reference = "SR 419.1 Art. 10 Abs. 1 Bst. c"


class grundsaetze_weiterbildungsgesetz_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Grundsaetze des Weiterbildungsgesetzes sind eingehalten"
    reference = "SR 419.1 Art. 10 Abs. 1 Bst. d"


class wirksamkeit_regelmaessig_ueberprueft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wirksamkeit der Finanzhilfe wird regelmaessig ueberprueft"
    reference = "SR 419.1 Art. 10 Abs. 1 Bst. e"


# --- Computed variables ---

class finanzhilfe_weiterbildung_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen fuer Finanzhilfen an Weiterbildung erfuellt"
    reference = "SR 419.1 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('oeffentliches_interesse_an_weiterbildung', period) *
            person('angebot_ohne_finanzhilfe_nicht_ausreichend', period) *
            person('ziele_und_kriterien_festgelegt', period) *
            person('grundsaetze_weiterbildungsgesetz_eingehalten', period) *
            person('wirksamkeit_regelmaessig_ueberprueft', period)
        )
