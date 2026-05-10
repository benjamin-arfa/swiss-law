"""SR 0.103.3 Art. 12

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class disappearance_investigation_status(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Disappearance investigation status (SR 0.103.3 Art. 12)"

    def formula(person, period, parameters):
        complaint_filed = person("complaint_filed", period)

        if complaint_filed:
            sufficient_evidence = person("sufficient_evidence", period)
            return sufficient_evidence
        else:
            return False

class sufficient_evidence(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sufficient evidence for disappearance investigation (SR 0.103.3 Art. 12)"

    def formula(person, period, parameters):
        disappearance_reported = person("disappearance_reported", period)
        investigation_conducted = person("investigation_conducted", period)

        return disappearance_reported & investigation_conducted

class investigation_covering_protection_measures(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Investigation covering protection measures (SR 0.103.3 Art. 12)"

    def formula(person, period, parameters):
        investigation_ongoing = person("investigation_ongoing", period)
        protection_measures_in_place = person("protection_measures_in_place", period)

        return investigation_ongoing & protection_measures_in_place
