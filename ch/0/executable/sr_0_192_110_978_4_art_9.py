"""SR 0.192.110.978.4 Art. 9

Generated from: ch/0/de/0.192.110.978.4.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class intelsat_privileges_exemptions_immunities_exclusion(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Exclusion from INTELSAT treaty privileges, exemptions, and immunities (Art. 9 SR 0.192.110.978.4)"

    def formula(person, period, parameters):
        # Contracting party representative
        contracting_party_representative = person("intelsat_contracting_party_representative", period)
        
        # Governors' Council representative
        governors_council_representative = person("intelsat_governors_council_representative", period)

        # INTELSAT General Director
        intelsat_general_director = person("intelsat_general_director", period)

        # Participant in arbitration proceedings
        arbitration_proceedings_participant = person("intelsat_arbitration_proceedings_participant", period)

        return (contracting_party_representative | governors_council_representative | \
                intelsat_general_director | arbitration_proceedings_participant)
