"""SR 0.142.116.829 Art. 5

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class switzerland_re_admits_person(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY  # Relevant for every day, not a yearly or monthly decision
    label = "Switzerland re-admit person (Art. 5 SR 0.142.116.829)"

    def formula(person, period, parameters):
        has_valid_swiss_visa = person("has_valid_swiss_visa", period)
        has_valid_swiss_residence_permit = person("has_valid_swiss_residence_permit", period)
        has_reentered_switzerland_illegally = person("has_reentered_switzerland_illegally", period)

        has_transited_swi = person("has_transited_swi", period)
        has_serbian_visa_before_entry = person("has_serbian_visa_before_entry", period)
        has_serbian_residence_permit_by_fraud = person("has_serbian_residence_permit_by_fraud", period)
        doesnt_meet_serbian_visa_conditions = person("doesnt_meet_serbian_visa_conditions", period)

        # Implementing Art 5 para 1
        return (person("has_valid_swiss_visa", period) | person("has_valid_swiss_residence_permit", period)) & \
               ((person("has_reentered_switzerland_illegally", period)) |

        # Implementing Art 5 para 2
               (has_transited_swi | has_serbian_visa_before_entry) & \
               (
                ((not has_serbian_visa_before_entry) | has_valid_swiss_residence_permit | 
                 person("has_serbian_residence_permit_by_fraud", period) | 
                 doesnt_meet_serbian_visa_conditions)))
