"""SR 0.105 Art. 29

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class social_security_contract_amendment efektion_year(Variable):
    value_type = date
    entity = Person
    definition_period = YEAR
    label = "Year the AHV contract amendment became effective (Art. 29 SR 0.105)"

    def formula(person, period, parameters):
        amendment_date = parameters(period).social_security.contract_amendment.effective_date
        return amendment_date if period.year >= amendment_date.year else None
