"""SR 705 Art. 13 - Ruecksichtnahme auf Velowege (Federal Consideration)

Generated from: ch/de/705.md
Federal agencies must consider planned bicycle networks in their tasks:
high-quality planning, conditions on concessions/permits, conditions on subsidies,
and replacement when networks must be removed.
Costs are charged to the relevant project budget or subsidized at the same rate.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class bund_veloweg_kosten_subventioniert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veloweg-Kosten werden zum gleichen Beitragssatz wie uebrige Objektkosten subventioniert"
    reference = "SR 705 Art. 13 Abs. 2"

    def formula(person, period, parameters):
        return True
