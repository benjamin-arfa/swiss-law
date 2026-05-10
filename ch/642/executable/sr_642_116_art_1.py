"""SR 642.116 Art. 1

Generated from: ch/642/de/642.116.md

Art. 1: Energy-saving and environmental protection investments
(Dem Energiesparen und dem Umweltschutz dienende Investitionen)

Investments serving energy saving and environmental protection are
expenditures for measures contributing to rational energy use or
renewable energy use. These relate to the replacement of outdated and
first-time installation of new building components in existing buildings.

If measures are subsidized by public entities, only the costs borne by
the taxpayer can be deducted.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class liegenschaft_energiespar_investition_brutto(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Brutto-Investitionskosten fuer Energiespar- und Umweltschutzmassnahmen (CHF)"
    reference = "SR 642.116 Art. 1 Abs. 1"


class liegenschaft_energiespar_subvention(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Oeffentliche Subventionen fuer Energiespar- und Umweltschutzmassnahmen (CHF)"
    reference = "SR 642.116 Art. 1 Abs. 2"
    default_value = 0


class liegenschaft_energiespar_investition_abzug(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abziehbare Investitionskosten fuer Energiesparen und Umweltschutz (CHF)"
    reference = "SR 642.116 Art. 1"

    def formula(person, period, parameters):
        brutto = person('liegenschaft_energiespar_investition_brutto', period)
        subvention = person('liegenschaft_energiespar_subvention', period)
        # Art. 1 Abs. 2: only costs borne by the taxpayer are deductible
        return max_(brutto - subvention, 0)
