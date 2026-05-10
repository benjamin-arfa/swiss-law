"""SR 112 Art. 8

Generated from: ch/de/112.md

Discharge: Upon performance, Bern is fully discharged from all
obligations under the 1848 federal decrees regarding seat contributions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bern_entbunden_von_bundessitzpflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gemeinde Bern von allen Bundessitzleistungen entbunden ist"
    reference = "SR 112 Art. 8"
