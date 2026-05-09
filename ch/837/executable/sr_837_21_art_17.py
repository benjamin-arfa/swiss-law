"""SR 837.21 Art. 17 - Ermittlung des Erwerbseinkommens (Determining employment income)

Annual employment income is calculated by deducting proven acquisition costs
and income-dependent mandatory social insurance contributions from gross
employment income.

Generated from: ch/837/de/837.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class uelv_bruttoerwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bruttoerwerbseinkommen in CHF pro Jahr (Art. 17 UeLV)"
    reference = "SR 837.21 Art. 17"


class uelv_gewinnungskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausgewiesene Gewinnungskosten in CHF pro Jahr (Art. 17 UeLV)"
    reference = "SR 837.21 Art. 17"


class uelv_sozialversicherungsbeitraege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkommensabhaengige obligatorische Sozialversicherungsbeitraege in CHF (Art. 17 UeLV)"
    reference = "SR 837.21 Art. 17"


class uelv_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliches Erwerbseinkommen fuer UeL-Berechnung in CHF (Art. 17 UeLV)"
    reference = "SR 837.21 Art. 17"

    def formula(person, period, parameters):
        brutto = person('uelv_bruttoerwerbseinkommen', period)
        kosten = person('uelv_gewinnungskosten', period)
        sv_beitraege = person('uelv_sozialversicherungsbeitraege', period)
        return max_(brutto - kosten - sv_beitraege, 0)
