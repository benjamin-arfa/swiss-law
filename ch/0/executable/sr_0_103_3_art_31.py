"""SR 0.103.3 Art. 31

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class international_procedure_status(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Status in international procedure of treaty-violation (Art. 31 SR 0.103.3)"

    def formula(person, period, parameters):
        procedure_accepted = parameters(period).international_treaties.received_communication
        already_pending = parameters(period).international_treaties.already_pending
        remedies_exhausted = parameters(period).international_treaties.remedies_exhausted
        return (procedure_accepted | not procedures_accepted & not already_pending & remedies_exhausted)
