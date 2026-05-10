"""SR 979.1 Art. 2

Generated from: ch/979/de/979.1.md

Art. 2 Voelkerrechtliche Vertraege:
1. The Federal Council is authorized to conclude international treaties on
   capital increases for IBRD, IDA, and IFC within approved credits.
2. Before subscribing to capital increases, the Federal Council informs
   the Federal Assembly.
3. Participation in IMF capital increases requires approval of the
   Federal Assembly.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bw_kapitalerhoehung_ibrd_ida_ifc(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Kapitalerhoehung bei IBRD, IDA oder IFC stattfindet"
    reference = "SR 979.1 Art. 2 Abs. 1"


class bw_kapitalerhoehung_iwf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Kapitalerhoehung beim Internationalen Waehrungsfonds stattfindet"
    reference = "SR 979.1 Art. 2 Abs. 3"


class bw_genehmigung_bundesversammlung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Genehmigung der Bundesversammlung fuer die Kapitalerhoehung erforderlich ist"
    reference = "SR 979.1 Art. 2 Abs. 3"

    def formula(person, period, parameters):
        return person('bw_kapitalerhoehung_iwf', period)
