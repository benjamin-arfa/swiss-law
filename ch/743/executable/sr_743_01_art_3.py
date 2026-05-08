"""SR 743.01 Art. 3

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Grundsaetze.
Seilbahnen mit Bundeskonzession brauchen Plangenehmigung und Betriebsbewilligung
vom BAV. Andere Seilbahnen (z.B. Skilifte) brauchen kantonale Bewilligung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_regelmaessige_gewerbsmaessige_befoerderung(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Seilbahn fuer regelmaessige gewerbsmaessige Personenbefoerderung bestimmt ist"
    reference = "SR 743.01 Art. 3 Abs. 1"


class seilbahn_personenbefoerderungskonzession_erforderlich(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob eine Personenbefoerderungskonzession nach PBG erforderlich ist"
    reference = "SR 743.01 Art. 3 Abs. 1"


class seilbahn_bundeskonzession(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Seilbahn eine Bundeskonzession benoetigt (Plangenehmigung + Betriebsbewilligung vom BAV)"
    reference = "SR 743.01 Art. 3 Abs. 1"

    def formula(organisation, period, parameters):
        regelmaessig = organisation('seilbahn_regelmaessige_gewerbsmaessige_befoerderung', period)
        konzession = organisation('seilbahn_personenbefoerderungskonzession_erforderlich', period)
        return regelmaessig * konzession


class seilbahn_kantonale_bewilligung_erforderlich(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Seilbahn eine kantonale Bewilligung benoetigt (kein Bundeskonzession)"
    reference = "SR 743.01 Art. 3 Abs. 2"

    def formula(organisation, period, parameters):
        import numpy as np
        bundeskonzession = organisation('seilbahn_bundeskonzession', period)
        sebg_anwendbar = organisation('seilbahn_sebg_anwendbar', period)
        return sebg_anwendbar * np.logical_not(bundeskonzession)
