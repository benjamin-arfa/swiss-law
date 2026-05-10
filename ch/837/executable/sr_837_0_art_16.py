"""SR 837.0 Art. 16

Generated from: ch/837/de/837.0.md

Art. 16: Zumutbare Arbeit (Reasonable work)

Abs. 1: The insured person must, as a rule, accept any work immediately.
Abs. 2 Bst. i: Work is unreasonable if it pays less than 70% of the
insured income, unless the person receives compensation payments (Art. 24).
With approval of the tripartite commission, the cantonal office may
exceptionally declare work paying less than 70% as reasonable.
Abs. 3bis: Art. 2 Bst. b does not apply to persons under 30.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alv_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der versicherten Person in Jahren"
    reference = "SR 837.0 Art. 16 Abs. 3bis"


class alv_angebotener_lohn(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Angebotener Lohn fuer vermittelte Stelle (CHF/Monat)"
    reference = "SR 837.0 Art. 16 Abs. 2 Bst. i"


class alv_arbeitsweg_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitsweg in Stunden (einfach)"
    reference = "SR 837.0 Art. 16 Abs. 2 Bst. f"


class alv_arbeit_lohnmaessig_zumutbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit ist lohnmaessig zumutbar (>= 70% des versicherten Verdienstes)"
    reference = "SR 837.0 Art. 16 Abs. 2 Bst. i"

    def formula(person, period, parameters):
        import numpy as np
        verdienst = person('alv_versicherter_verdienst', period.this_year)
        angebotener_lohn = person('alv_angebotener_lohn', period)

        # Monthly insured income (annual / 12)
        versicherter_monatslohn = verdienst / 12.0

        # Work is reasonable if offered wage >= 70% of insured monthly income
        mindestlohn = versicherter_monatslohn * 0.70
        return angebotener_lohn >= mindestlohn


class alv_arbeit_wegmaessig_zumutbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeit ist wegmaessig zumutbar (Arbeitsweg <= 2 Stunden je Weg)"
    reference = "SR 837.0 Art. 16 Abs. 2 Bst. f"

    def formula(person, period, parameters):
        arbeitsweg = person('alv_arbeitsweg_stunden', period)
        # Unreasonable if commute > 2 hours one way
        return arbeitsweg <= 2.0


class alv_fachliche_zumutbarkeit_ausnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person unter 30: fachliche Zumutbarkeit (Art. 16 Abs. 2 Bst. b) nicht anwendbar"
    reference = "SR 837.0 Art. 16 Abs. 3bis"

    def formula(person, period, parameters):
        alter = person('alv_alter', period.this_year)
        # Abs. 3bis: Art. 16 Abs. 2 Bst. b does not apply to persons under 30
        return alter <= 30
