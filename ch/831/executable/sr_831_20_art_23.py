"""SR 831.20 Art. 23

Generated from: ch/831/de/831.20.md

Art. 23: Grundentschaedigung - Basic compensation for daily allowance:
- Abs. 1: The basic compensation is 80% of the last earned income without
  health limitations, but not more than 80% of the maximum daily allowance
  per Art. 24 Abs. 1.
- Abs. 1bis: For reintegration measures (Art. 8a), it is 80% of the income
  immediately before the measure, capped at 80% of the max daily allowance.
- Abs. 3: Basis is the average income subject to AHV contributions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_letztes_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Letztes Erwerbseinkommen ohne gesundheitliche Einschraenkung (CHF/Jahr)"
    reference = "SR 831.20 Art. 23 Abs. 1"


class iv_erwerbseinkommen_vor_massnahme(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erwerbseinkommen unmittelbar vor Beginn der Wiedereingliederungsmassnahme (CHF/Jahr)"
    reference = "SR 831.20 Art. 23 Abs. 1bis"


class iv_hoechstbetrag_taggeld(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = (
        "Hoechstbetrag des Taggeldes nach Art. 24 Abs. 1 "
        "(entspricht Hoechstbetrag versicherter Tagesverdienst UVG)"
    )
    reference = "SR 831.20 Art. 24 Abs. 1"


class iv_ist_wiedereingliederung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Massnahme ist eine Wiedereingliederung nach Art. 8a IVG"
    reference = "SR 831.20 Art. 23 Abs. 1bis"


class iv_grundentschaedigung_taggeld(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Grundentschaedigung des IV-Taggeldes (Art. 23 IVG, CHF/Tag)"
    reference = "SR 831.20 Art. 23"

    def formula(person, period, parameters):
        letztes_einkommen = person('iv_letztes_erwerbseinkommen', period.this_year)
        einkommen_vor_massnahme = person('iv_erwerbseinkommen_vor_massnahme', period.this_year)
        hoechstbetrag = person('iv_hoechstbetrag_taggeld', period.this_year)
        wiedereingliederung = person('iv_ist_wiedereingliederung', period)

        # Convert annual income to daily (/ 365)
        tageseinkommen = where(
            wiedereingliederung,
            einkommen_vor_massnahme / 365,
            letztes_einkommen / 365
        )

        # 80% of income, capped at 80% of max daily allowance
        grundentschaedigung = min_(tageseinkommen * 0.80, hoechstbetrag * 0.80)
        return grundentschaedigung
