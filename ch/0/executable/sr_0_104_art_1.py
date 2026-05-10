"""SR 0.104 Art. 1

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class racial_discrimination(Variable):
    value_type = bool
    label = "Racial discrimination (Art. 1 CERD)"

    def formula_1(person, period, parameters):
        purpose = person("discriminatory_purpose", period)
        effect = person("discriminatory_effect", period)
        exclusion = person("exclusion", period)
        restriction = person("restriction", period)
        preference = person("preference", period)

        return (purpose | effect | exclusion | restriction | preference)

    def formula(person, period, parameters):
        legal_basis = person("legal_basis", period)
        equality_of_treatment = person("equality_of_treatment", period)
        equality_before_law = person("equality_before_law", period)
        public_life_fields = person("public_life_fields", period)

        racial_discrimination = self.formula_1(person, period, parameters)

        non_targeting_sondermassnahmen = person("non_targeting_sondermassnahmen", period)

        return racial_discrimination & (not non_targeting_sondermassnahmen)
