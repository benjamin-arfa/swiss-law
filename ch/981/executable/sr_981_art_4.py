"""SR 981 Art. 4

Generated from: ch/de/981.md

Execution of compensation agreements: Federal Council may commission
the Commission or other authorities with the execution.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kommission_vollzug_beauftragt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat die Kommission mit dem Vollzug von Entschaedigungsabkommen beauftragt hat"
    reference = "SR 981 Art. 4 Abs. 1"


class andere_behoerden_vollzug_beauftragt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat andere Behoerden mit dem Vollzug beauftragt hat wegen besonderer Umstaende"
    reference = "SR 981 Art. 4 Abs. 2"
