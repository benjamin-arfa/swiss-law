"""SR 131.214 Art. 9

Generated from: ch/131/de/131.214.md

Steuerhoheit: Die Landeskirchen oder ihre Kirchgemeinden sind befugt,
im Rahmen der kantonalen Gesetzgebung Steuern zu erheben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_landeskirche_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation eine anerkannte Landeskirche im Kanton Uri ist"
    reference = "SR 131.214 Art. 7"


class kirchensteuer_befugnis_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Landeskirche oder Kirchgemeinde befugt ist, Steuern zu erheben"
    reference = "SR 131.214 Art. 9"

    def formula(person, period, parameters):
        return person('ist_landeskirche_uri', period)
