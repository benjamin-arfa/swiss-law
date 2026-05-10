"""SR 221.214.111 Art. 1

Generated from: ch/221/de/221.214.111.md

Maximum interest rate for consumer credits:
- Cash credits, financing contracts, leasing contracts: max 10%
- Overdraft credits on current accounts or credit/customer card
  accounts with credit option: max 12%
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kkg_kreditart_barkredit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Barkredit (Art. 9 KKG) handelt"
    reference = "SR 221.214.111 Art. 1 Abs. 1"


class kkg_kreditart_finanzierung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Vertrag zur Finanzierung des Erwerbs von Waren oder Dienstleistungen (Art. 10 KKG) handelt"
    reference = "SR 221.214.111 Art. 1 Abs. 1"


class kkg_kreditart_leasing(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Leasingvertrag (Art. 11 KKG) handelt"
    reference = "SR 221.214.111 Art. 1 Abs. 1"


class kkg_kreditart_ueberziehungskredit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Ueberziehungskredit auf laufendem Konto oder Kreditkartenkonto (Art. 12 KKG) handelt"
    reference = "SR 221.214.111 Art. 1 Abs. 2"


class kkg_vereinbarter_zinssatz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Der vereinbarte Zinssatz des Konsumkredits in Prozent"
    reference = "SR 221.214.111 Art. 1"


class kkg_hoechstzinssatz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Der geltende Hoechstzinssatz fuer den Konsumkredit in Prozent"
    reference = "SR 221.214.111 Art. 1"

    def formula_2026_01(person, period, parameters):
        ueberziehung = person('kkg_kreditart_ueberziehungskredit', period)
        return where(ueberziehung, 12.0, 10.0)


class kkg_zinssatz_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der vereinbarte Zinssatz den Hoechstzinssatz nicht uebersteigt"
    reference = "SR 221.214.111 Art. 1"

    def formula(person, period, parameters):
        vereinbart = person('kkg_vereinbarter_zinssatz', period)
        hoechst = person('kkg_hoechstzinssatz', period)
        return vereinbart <= hoechst
