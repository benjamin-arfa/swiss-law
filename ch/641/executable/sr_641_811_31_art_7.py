"""SR 641.811.31 Art. 7

Generated from: ch/641/de/641.811.31.md

Entry into force: 1 January 2001.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_641_811_31_inkrafttreten(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum des Inkrafttretens der Verordnung SR 641.811.31"
    reference = "SR 641.811.31 Art. 7"
    default_value = "2001-01-01"
