"""SR 743.01 Art. 9

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Plangenehmigung.
Voraussetzungen fuer die Erteilung der Plangenehmigung:
grundlegende Anforderungen erfuellt, keine wesentlichen oeffentlichen
Interessen entgegenstehend, Konzessionsvoraussetzungen erfuellt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_grundlegende_anforderungen_und_vorschriften(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob grundlegende Anforderungen und massgebende Vorschriften erfuellt sind"
    reference = "SR 743.01 Art. 9 Abs. 3 Bst. a"


class seilbahn_keine_wesentlichen_oeffentlichen_interessen_entgegen(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob keine wesentlichen oeffentlichen Interessen (Raumplanung, Umweltschutz) entgegenstehen"
    reference = "SR 743.01 Art. 9 Abs. 3 Bst. b"


class seilbahn_konzessionsvoraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Voraussetzungen zur Erteilung der Personenbefoerderungskonzession erfuellt sind"
    reference = "SR 743.01 Art. 9 Abs. 3 Bst. c"


class seilbahn_plangenehmigung_erteilt(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Plangenehmigung erteilt wird"
    reference = "SR 743.01 Art. 9 Abs. 3"

    def formula(organisation, period, parameters):
        anforderungen = organisation('seilbahn_grundlegende_anforderungen_und_vorschriften', period)
        oeffentliche_interessen = organisation('seilbahn_keine_wesentlichen_oeffentlichen_interessen_entgegen', period)
        konzession = organisation('seilbahn_konzessionsvoraussetzungen_erfuellt', period)
        return anforderungen * oeffentliche_interessen * konzession
