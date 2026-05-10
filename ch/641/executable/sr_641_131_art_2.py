"""SR 641.131 Art. 2

Generated from: ch/641/de/641.131.md

Entry into force: 1 April 1993.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_641_131_inkrafttreten(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum des Inkrafttretens der Verordnung SR 641.131"
    reference = "SR 641.131 Art. 2"
    default_value = "1993-04-01"
