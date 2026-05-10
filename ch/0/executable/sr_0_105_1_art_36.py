"""SR 0.105.1 Art. 36

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class prevention_sub_committee_member_compliance(Variable):
    value_type = bool
    entity = Person
    label = "Compliance with local laws and regulations for Prevention Sub-Committee members (Art. 36 SR 0.105.1)"

    def formula(person, period, parameters):
        local_laws_complied = parameters(period).members_conduct.local_laws_respected
        no_improper_measure_taken = parameters(period).members_conduct.no_improper_measure_taken

        return local_laws_complied & no_improper_measure_taken
