"""SR 0.121 Art. III

Generated from: ch/0/de/0.121.md

International cooperation in scientific investigation: exchange of
information, scientific personnel, and observations/results.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antarktis_informationsaustausch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Informationen ueber wissenschaftliche Programme in der Antarktis ausgetauscht werden"
    reference = "SR 0.121 Art. III Abs. 1 Bst. a"


class antarktis_personalaustausch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob wissenschaftliches Personal zwischen Expeditionen und Stationen ausgetauscht wird"
    reference = "SR 0.121 Art. III Abs. 1 Bst. b"


class antarktis_ergebnisse_verfuegbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob wissenschaftliche Ergebnisse ausgetauscht und frei zur Verfuegung gestellt werden"
    reference = "SR 0.121 Art. III Abs. 1 Bst. c"
