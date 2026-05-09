"""SR 198.1 Art. 2

Generated from: ch/198/de/198.1.md

Umweltvertraeglichkeitspruefung: Anyone wishing to carry out an activity
in the Antarctic must ensure at their own expense that the environmental
impact assessment prescribed by Article 8 of the Protocol is carried out
beforehand.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class plant_taetigkeit_in_antarktis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person plant eine Taetigkeit in der Antarktis"
    reference = "SR 198.1 Art. 2"


class uvp_antarktis_durchgefuehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Umweltvertraeglichkeitspruefung nach Art. 8 des Protokolls wurde durchgefuehrt"
    reference = "SR 198.1 Art. 2"


class uvp_antarktis_pflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist verpflichtet, eine Umweltvertraeglichkeitspruefung durchzufuehren"
    reference = "SR 198.1 Art. 2"

    def formula(person, period, parameters):
        plant = person('plant_taetigkeit_in_antarktis', period)
        return plant


class uvp_kosten_selbst_tragen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kosten der UVP sind auf eigene Kosten zu tragen"
    reference = "SR 198.1 Art. 2"

    def formula(person, period, parameters):
        return person('uvp_antarktis_pflicht', period)
