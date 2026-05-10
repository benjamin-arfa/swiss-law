"""SR 441.1 Art. 15

Generated from: ch/441/de/441.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kompetenz_zweite_landessprache_ende_obligatorische_schulzeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schüler verfügen am Ende der obligatorischen Schulzeit über Kompetenzen in mindestens einer zweiten Landessprache und einer weiteren Fremdsprache"
    reference = "SR 441.1, Art. 15 Abs. 3"

    def formula(self, period, parameters):
        hat_zweite_landessprache = self.person('hat_kompetenz_zweite_landessprache', period)
        hat_weitere_fremdsprache = self.person('hat_kompetenz_weitere_fremdsprache', period)
        return hat_zweite_landessprache * hat_weitere_fremdsprache


class hat_kompetenz_zweite_landessprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Kompetenzen in einer zweiten Landessprache"
    reference = "SR 441.1, Art. 15 Abs. 3"


class hat_kompetenz_weitere_fremdsprache(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Kompetenzen in einer weiteren Fremdsprache"
    reference = "SR 441.1, Art. 15 Abs. 3"
