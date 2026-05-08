"""SR 743.01 Art. 12

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Anhoerung, Publikation und Auflage.
Kantonale Stellungnahme: 3 Monate. Oeffentliche Auflage: 30 Tage.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_kantonale_stellungnahmefrist_monate(Variable):
    value_type = int
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Frist fuer kantonale Stellungnahme in Monaten"
    reference = "SR 743.01 Art. 12 Abs. 1"

    def formula(organisation, period, parameters):
        return 3


class seilbahn_oeffentliche_auflagefrist_tage(Variable):
    value_type = int
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Frist fuer oeffentliche Auflage in Tagen"
    reference = "SR 743.01 Art. 12 Abs. 2"

    def formula(organisation, period, parameters):
        return 30
