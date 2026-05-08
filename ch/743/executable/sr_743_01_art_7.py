"""SR 743.01 Art. 7

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Enteignungsrecht.
Seilbahnbetreiber haben Enteignungsrecht sofern die Anlage
der Nutzungsplanung entspricht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_anlage_nutzungsplankonform(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Seilbahnanlage der Nutzungsplanung entspricht"
    reference = "SR 743.01 Art. 7 Abs. 1"


class seilbahn_enteignungsrecht(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob dem Seilbahnbetreiber das Enteignungsrecht zusteht"
    reference = "SR 743.01 Art. 7 Abs. 1"

    def formula(organisation, period, parameters):
        nutzungsplan = organisation('seilbahn_anlage_nutzungsplankonform', period)
        sebg_anwendbar = organisation('seilbahn_sebg_anwendbar', period)
        return sebg_anwendbar * nutzungsplan
