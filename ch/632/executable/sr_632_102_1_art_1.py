"""SR 632.102.1 Art. 1

Generated from: ch/632/de/632.102.1.md
Customs rates for certain textile pre- and intermediate materials whose rates
differ from the general tariff are set out in Annex 1.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class textile_material_has_suspended_tariff(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether textile pre/intermediate material has a suspended (reduced) customs tariff"
    reference = "SR 632.102.1 Art. 1"

    def formula(person, period, parameters):
        is_textile_material = person("is_textile_pre_or_intermediate_material", period)
        in_annex_1 = person("listed_in_tariff_annex_1", period)
        return is_textile_material * in_annex_1
