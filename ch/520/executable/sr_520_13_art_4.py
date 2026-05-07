"""SR 520.13 Art. 4

Generated from: ch/520/de/520.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 4: MeteoSchweiz provides technical training support for military weather
# service formations. This is a procedural/organizational provision.


class meteoschweiz_fachausbildung_armee(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "MeteoSchweiz unterstuetzt die Armee bei der fachtechnischen Ausbildung der Formationen des militaerischen Wetterdienstes"
    reference = "SR 520.13 Art. 4"
