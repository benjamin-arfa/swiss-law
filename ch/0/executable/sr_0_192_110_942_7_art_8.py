"""SR 0.192.110.942.7 Art. 8

Generated from: ch/0/de/0.192.110.942.7.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class customs_duty_exemption(Variable):
    value_type = bool
    entity = CustomsDeclaration
    label = "Customs duty exemption (Art. 8 Protocoll on Free Trade Agreements)"

    def formula(c, period, parameters):
        shipped_for = c('shipped_for', period)
        recipient = c('recipient', period)
        shipment_code = c('shipment_code', period)
        reason_code = c('reason_code', period)
        org_types = [parameters(period).trade.free_trade_agreement.organizations, parameters(period).trade.free_trade_agreement.govt, parameters(period).trade.free_trade_agreement.individuals]

        return (shipped_for in org_types) & {'custom_code': shipment_code, 'reason': reason_code}.values()
