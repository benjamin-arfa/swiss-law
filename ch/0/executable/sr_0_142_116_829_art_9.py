"""SR 0.142.116.829 Art. 9

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

import datetime

class art9_evidence_basis(Variable):
    value_type = str
    entity = Person
    definition_period = MONTH
    label = "Evidence basis for return transfer of third-state nationals (Art. 9 SR 0.142.116.829)"

    def formula(person, period, parameters):
        age = (period.date - person('birth_date', period)).days / 365.25
        current_datetime = datetime.datetime.now()
        application_date = person('application_date', period)

        # Implement logic to check presence, residence and application date to determine if valid evidence exists as described in Art.9
        # Based on this information, the correct evidence basis can be determined
        # Here is the very general outline of the steps needed based on conditions described
        if current_datetime.year >= 2003 and (person('resides_in_switzerland', period) | person('works_in_switzerland', period)):
            # Implement Art. 3 and 5 relevant conditions to apply according to evidence from paragraphs 1 or 2
            # Given that the logic from the text has to be applied under specific context: implement a boolean condition to decide according to paragraphs 1 or 2 that a valid documented evidence (documente certifiés) can be provided - e.g. with specific diplomatic document in place - by checking if a certified document based on a protocol from the years 2003 to 2006 (Art. 4 des Durchführungsprotokolls) is provided - and if so which type of document was provided, then
            evidence_basis = "document certifié Art. 4 DP"
        elif current_datetime.year >= 2003:
            # in case of no certified document from 2003-2006 and no certified document as defined in 4 above implement another set of checks, similar to above, to decide if the specific type of non-certified evidence can be applied according to paragraphs 4 or 5, based on year range and specific conditions (e.g. only valid for one citizen group)

            evidence_basis = "other evidence basis specified in para 4 or 5"
        # in case of lack of proof according to paragraphs above and based on paragraph 6 implement another set of actions to verify nationality, and decide the evidence_basis
        else:
            evidence_basis = "failing to meet specific conditions - nationality verification initiated according to Art. 9 para. 6"

        return evidence_basis
