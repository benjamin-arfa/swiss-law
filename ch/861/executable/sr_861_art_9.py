"""SR 861 Art. 9

Generated from: ch/de/861.md

The Federal Council issues the implementing provisions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kbfhg_ausfuehrungsbestimmungen_bundesrat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat die Ausfuehrungsbestimmungen zum KBFHG erlaesst"
    reference = "SR 861 Art. 9"
