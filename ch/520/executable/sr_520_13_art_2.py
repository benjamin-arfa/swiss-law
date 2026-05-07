"""SR 520.13 Art. 2

Generated from: ch/520/de/520.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class meteoschweiz_koordination_wetterversorgung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "MeteoSchweiz sorgt fuer die Koordination der Wetterversorgung in besonderen und ausserordentlichen Lagen"
    reference = "SR 520.13 Art. 2 Abs. 1"


class meteoschweiz_koordination_beschaffung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "MeteoSchweiz koordiniert die Beschaffung von Erfassungs-, Uebertragungs- und Auswertesystemen"
    reference = "SR 520.13 Art. 2 Abs. 2"
