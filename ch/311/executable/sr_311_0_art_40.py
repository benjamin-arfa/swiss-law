"""SR 311.0 Art. 40

Generated from: ch/fr/311/311.0.md

Art. 40: Peine privative de liberte - Duree
- Abs. 1: Min 3 days (shorter if conversion from unpaid fine/monetary penalty).
- Abs. 2: Max 20 years; life imprisonment when expressly provided by law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_freiheitsstrafe_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauer der Freiheitsstrafe in Tagen"
    reference = "SR 311.0 Art. 40"


class stgb_freiheitsstrafe_aus_umwandlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob die Freiheitsstrafe aus Umwandlung einer Geldstrafe oder Busse stammt"
    reference = "SR 311.0 Art. 40 Abs. 1"


class stgb_lebenslange_strafe_gesetzlich_vorgesehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob fuer die Straftat lebenslange Freiheitsstrafe gesetzlich vorgesehen ist"
    reference = "SR 311.0 Art. 40 Abs. 2"


class stgb_freiheitsstrafe_dauer_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Freiheitsstrafe innerhalb der gesetzlichen Grenzen liegt"
    reference = "SR 311.0 Art. 40"

    def formula(person, period, parameters):
        tage = person('stgb_freiheitsstrafe_tage', period)
        umwandlung = person('stgb_freiheitsstrafe_aus_umwandlung', period)
        lebenslang = person('stgb_lebenslange_strafe_gesetzlich_vorgesehen', period)

        # Minimum: 3 days (or less if converted from fine)
        min_tage = where(umwandlung, 1, 3)
        # Maximum: 20 years = 7300 days (life = uncapped)
        max_tage = where(lebenslang, 99999, 7300)

        return (tage >= min_tage) * (tage <= max_tage)
