"""SR 743.01 Art. 2

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Geltungsbereich.
Gilt fuer alle Seilbahnen zur Personenbefoerderung. Ausgenommen sind
Bergbau-Seilbahnen, nicht ortsfeste Seilbahnen, Jahrmarktgeraete,
militaerische Seilbahnen und Aufzuege.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_personenbefoerderung(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Anlage eine Seilbahn zur Personenbefoerderung ist"
    reference = "SR 743.01 Art. 2 Abs. 1"


class seilbahn_bergbau(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Seilbahn im Bergbau eingesetzt wird"
    reference = "SR 743.01 Art. 2 Abs. 2 Bst. a"


class seilbahn_nicht_ortsfest(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Seilbahn nicht ortsfest ist"
    reference = "SR 743.01 Art. 2 Abs. 2 Bst. b"


class seilbahn_jahrmarktgeraet(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob es sich um ein Jahrmarktgeraet oder Vergnuegungsparkanlage handelt"
    reference = "SR 743.01 Art. 2 Abs. 2 Bst. c"


class seilbahn_militaerisch(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob es sich um eine militaerische Seilbahn handelt"
    reference = "SR 743.01 Art. 2 Abs. 2 Bst. d"


class seilbahn_aufzug(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob es sich um einen Aufzug handelt"
    reference = "SR 743.01 Art. 2 Abs. 2 Bst. e"


class seilbahn_sebg_anwendbar(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob das Seilbahngesetz auf die Anlage anwendbar ist"
    reference = "SR 743.01 Art. 2"

    def formula(organisation, period, parameters):
        import numpy as np
        personenbefoerderung = organisation('seilbahn_personenbefoerderung', period)
        bergbau = organisation('seilbahn_bergbau', period)
        nicht_ortsfest = organisation('seilbahn_nicht_ortsfest', period)
        jahrmarkt = organisation('seilbahn_jahrmarktgeraet', period)
        militaerisch = organisation('seilbahn_militaerisch', period)
        aufzug = organisation('seilbahn_aufzug', period)
        ausnahme = bergbau + nicht_ortsfest + jahrmarkt + militaerisch + aufzug
        return personenbefoerderung * np.logical_not(ausnahme > 0)
