"""SR 251 Art. 4

Generated from: ch/de/251.md

Definitions: competition agreements, market-dominant enterprises,
relatively market-powerful enterprises, and mergers.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_wettbewerbsabrede(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Wettbewerbsabrede vorliegt (erzwingbare oder abgestimmte Verhaltensweise)"
    reference = "SR 251 Art. 4 Abs. 1"


class ist_marktbeherrschend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen marktbeherrschend ist"
    reference = "SR 251 Art. 4 Abs. 2"


class ist_relativ_marktmaechtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen relativ marktmaechtig ist"
    reference = "SR 251 Art. 4 Abs. 2bis"


class ist_unternehmenszusammenschluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Unternehmenszusammenschluss vorliegt"
    reference = "SR 251 Art. 4 Abs. 3"
