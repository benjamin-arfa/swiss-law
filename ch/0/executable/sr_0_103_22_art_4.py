"""SR 0.103.22 Art. 4

Generated from: ch/0/de/0.103.22.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class protocol_state_commitments(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Protocol State commitments post ratification (Art. 4 SR 0.103.22)"

    def formula(country, period, parameters):
        has_protocol_declaration = country("has_protocol_declaration", period)
        made_contrariety_declaration = country("made_contrariety_declaration", period)
        return (~has_protocol_declaration) | made_contrariety_declaration
