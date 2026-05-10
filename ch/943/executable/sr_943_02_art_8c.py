"""SR 943.02 Art. 8c

Generated from: ch/943/de/943.02.md

Verletzung der Auskunftspflicht:
- Busse bei Nichterfüllung oder nicht richtiger Erfüllung der
  Auskunftspflicht nach Art. 8b
- Wettbewerbskommission verfolgt und beurteilt nach VStrR (SR 313.0)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verletzt_auskunftspflicht_bgbm(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Auskunftspflicht nach BGBM Art. 8b nicht oder nicht richtig erfüllt wird"
    reference = "SR 943.02 Art. 8c Abs. 1"


class strafbar_auskunftspflicht_bgbm(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Verletzung der Auskunftspflicht strafbar ist (Busse)"
    reference = "SR 943.02 Art. 8c Abs. 1"

    def formula(person, period, parameters):
        return person('verletzt_auskunftspflicht_bgbm', period)
