"""SR 958.2 Art. 6

Generated from: ch/958/fr/958.2.md

Entrée en vigueur et durée de validité.
The ordinance enters into force on 30 Nov 2018 at 20:00 and is valid until 31 Dec 2025.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_958_2_en_vigueur(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "SR 958.2 is in force for the given period"
    reference = "SR 958.2 Art. 6"

    def formula_2018(organisation, period, parameters):
        # In force from 30 Nov 2018
        return 1

    def formula_2026(organisation, period, parameters):
        # Valid until 31 Dec 2025 (extended from original 31 Dec 2021)
        return 0
