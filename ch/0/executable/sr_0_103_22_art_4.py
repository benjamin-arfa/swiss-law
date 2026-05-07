"""SR 0.103.22 Art. 4

Generated from: ch/0/de/0.103.22.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import Variable
from openfisca_core.periods import YEAR


class protocol_state_commitments(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Protocol State commitments post ratification (Art. 4 SR 0.103.22)"

    def formula(country, period, parameters):
        has_protocol_declaration = country("has_protocol_declaration", period)
        made_contrariety_declaration = country("made_contrariety_declaration", period)
        return (~has_protocol_declaration) | made_contrariety_declaration
