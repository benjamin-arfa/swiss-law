"""SR 241 Art. 8

Generated from: ch/de/241.md

Use of unfair general terms and conditions that, in violation
of good faith, create a significant and unjustified imbalance
to the detriment of consumers.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class missbraeuchliche_agb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob missbraeuchliche AGB zum Nachteil der Konsumenten verwendet werden"
    reference = "SR 241 Art. 8"
