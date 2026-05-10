"""SR 0.101.09 Art. 6

Generated from: ch/0/de/0.101.09.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class cjeu_jurisdiction_recognition(
    Variable, label="Jurisdiction of the Court of Justice of the European Union"
):
    def formula(
        apportionment,
        period,
        parameters,
        variables,
        subject_role,
    ):
        recognizes_cjeu_jurisdiction = parameters(period).recognizes_cjeu_jurisdiction
        has_issued_declaration = variables(period).has_issued_declaration

        if recognizes_cjeu_jurisdiction and has_issued_declaration:
            return 1
        else:
            return 0
