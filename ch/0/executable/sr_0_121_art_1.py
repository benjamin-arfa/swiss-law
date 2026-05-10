"""SR 0.121 Art. I

Generated from: ch/0/de/0.121.md

Antarctica shall be used for peaceful purposes only. All measures of a
military nature are prohibited. Military personnel or equipment may be
used for scientific research or other peaceful purposes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antarktis_friedliche_nutzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Antarktis nur fuer friedliche Zwecke genutzt wird"
    reference = "SR 0.121 Art. I Abs. 1"


class antarktis_militaerische_massnahmen_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Massnahmen militaerischer Art in der Antarktis verboten sind"
    reference = "SR 0.121 Art. I Abs. 1"

    def formula(person, period, parameters):
        return 1


class antarktis_militaer_fuer_forschung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob militaerisches Personal oder Material fuer wissenschaftliche Forschung eingesetzt wird"
    reference = "SR 0.121 Art. I Abs. 2"
