"""SR 641.10 Art. 10

Generated from: ch/641/de/641.10.md

Art. 10 Abgabepflicht (Liable parties):
1. For participation rights: the company or cooperative is liable for the levy.
   For majority transfers (Art. 5 Abs. 2 Bst. b): the seller is jointly liable.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stg_gesellschaft_abgabepflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the company/cooperative is liable for the emission levy"
    reference = "SR 641.10 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        return person('stg_emissionsabgabe_tatbestand', period)


class stg_veraeusserer_solidarhaftung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the seller is jointly liable (in case of majority transfer)"
    reference = "SR 641.10 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        return person('stg_handwechsel_mehrheit_liquidiert', period)
