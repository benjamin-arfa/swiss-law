"""SR 311.0 Art. 43

Generated from: ch/fr/311/311.0.md

Art. 43: Sursis partiel (Teilbedingte Freiheitsstrafe)
- Abs. 1: Partial suspension for imprisonment of 1-3 years.
- Abs. 2: Firm part must not exceed half the sentence.
- Abs. 3: Both firm and suspended parts must be at least 6 months.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_teilbedingte_strafe_gesamt_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamtdauer der teilbedingten Freiheitsstrafe in Monaten"
    reference = "SR 311.0 Art. 43 Abs. 1"


class stgb_teilbedingte_strafe_unbedingter_teil_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Unbedingter Teil der teilbedingten Strafe in Monaten"
    reference = "SR 311.0 Art. 43 Abs. 2"


class stgb_teilbedingte_strafe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die teilbedingte Strafe den gesetzlichen Anforderungen entspricht"
    reference = "SR 311.0 Art. 43"

    def formula(person, period, parameters):
        gesamt = person('stgb_teilbedingte_strafe_gesamt_monate', period)
        unbedingt = person('stgb_teilbedingte_strafe_unbedingter_teil_monate', period)
        bedingt = gesamt - unbedingt

        # Total must be 12-36 months
        gesamt_ok = (gesamt >= 12) * (gesamt <= 36)
        # Firm part must not exceed half
        haelfte_ok = unbedingt <= gesamt / 2
        # Both parts at least 6 months
        min_ok = (unbedingt >= 6) * (bedingt >= 6)

        return gesamt_ok * haelfte_ok * min_ok
