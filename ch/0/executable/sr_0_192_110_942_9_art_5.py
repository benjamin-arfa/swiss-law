"""SR 0.192.110.942.9 Art. 5

Generated from: ch/0/de/0.192.110.942.9.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class center_customs_exemption(Variable):
    value_type = bool
    entity = Center
    definition_period = IMPORT
    label = "Customs exemption for official goods (SR 0.192.110.942.9 Art. 5)"

    def formula(center, period, parameters):
        activity_necessary_goods = [good for good in period.goods if good.is_necessary_for_official_activity]
        represents_reimbursement = any(representing_service in activity_necessary_goods for representing_service in period.goods)

        return not represents_reimbursement
