"""SR 642.116.2 Art. 1

Generated from: ch/642/de/642.116.2.md

Art. 1: Deductible costs (Abziehbare Kosten)

Abs. 1 - Deductible costs include:
a. Maintenance costs:
   1. Repair/renovation expenses (non-value-increasing)
   2. Contributions to repair/renewal fund of condominium associations
   3. Operating costs (waste, sewage, street lighting/cleaning,
      property taxes as object taxes, janitor compensation, etc.)
b. Insurance premiums (fire, water damage, glass, liability)
c. Administration costs (postage, phone, ads, debt collection, etc.
   - actual expenses only, no compensation for owner's own work)

Abs. 2 - Non-deductible maintenance costs:
b. One-time contributions (road, sidewalk, utility connections, etc.)
c. Heating and hot water operating costs (energy costs)
d. Water fees (generally non-deductible)

Abs. 3 - Water fees are deductible if the owner bears them for
rented properties and does not pass them to tenants.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class liegenschaft_unterhaltskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abziehbare Unterhaltskosten der Liegenschaft (Reparaturen, Renovationen, Betriebskosten) (CHF)"
    reference = "SR 642.116.2 Art. 1 Abs. 1 Bst. a"


class liegenschaft_versicherungspraemien(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abziehbare Sachversicherungspraemien der Liegenschaft (CHF)"
    reference = "SR 642.116.2 Art. 1 Abs. 1 Bst. b"


class liegenschaft_verwaltungskosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abziehbare Verwaltungskosten der Liegenschaft (CHF)"
    reference = "SR 642.116.2 Art. 1 Abs. 1 Bst. c"


class liegenschaft_wasserzinsen_vermietet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wasserzinsen fuer vermietete Objekte, die der Eigentuemer selber traegt (CHF)"
    reference = "SR 642.116.2 Art. 1 Abs. 3"
    default_value = 0


class liegenschaft_tatsaechliche_kosten_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total abziehbare tatsaechliche Liegenschaftskosten (CHF)"
    reference = "SR 642.116.2 Art. 1"

    def formula(person, period, parameters):
        unterhalt = person('liegenschaft_unterhaltskosten', period)
        versicherung = person('liegenschaft_versicherungspraemien', period)
        verwaltung = person('liegenschaft_verwaltungskosten', period)
        wasserzinsen = person('liegenschaft_wasserzinsen_vermietet', period)
        return unterhalt + versicherung + verwaltung + wasserzinsen
