"""SR 837.0 Art. 22

Generated from: ch/837/de/837.0.md

Art. 22: Hoehe des Taggeldes (Daily allowance amount)
- Abs. 1: A full daily allowance is 80% of the insured income. The insured
  person also receives a supplement corresponding to the family allowances
  under Art. 3(1) FamZG, provided those allowances are not paid during
  unemployment and no employed person already claims them for the same child.
- Abs. 2: A daily allowance of 70% of insured income applies to persons who:
  a. have no support obligations for children under 25
  b. would receive a full daily allowance exceeding CHF 140
  c. do not receive a disability pension corresponding to at least 40% IV degree
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alv_bezieht_iv_rente_40_prozent(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bezieht eine Invalidenrente mit mindestens 40% Invaliditaetsgrad"
    reference = "SR 837.0 Art. 22 Abs. 2 Bst. c"


class alv_taggeld_satz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anwendbarer Taggeldsatz (0.80 oder 0.70)"
    reference = "SR 837.0 Art. 22 Abs. 1-2"

    def formula(person, period, parameters):
        unterhalt = person('alv_unterhaltspflicht_kinder_unter_25', period)
        iv_rente = person('alv_bezieht_iv_rente_40_prozent', period)
        verdienst = person('alv_versicherter_verdienst', period.this_year)
        p = parameters(period).alv

        volles_taggeld = verdienst / 260 * p.taggeld_satz_voll  # approx 260 working days

        # Reduced rate applies only if ALL three conditions are met:
        # a) no child support, b) full daily allowance > threshold, c) no IV pension >= 40%
        reduziert = (
            (unterhalt == False)
            * (volles_taggeld > p.taggeld_schwelle_reduktion)
            * (iv_rente == False)
        )

        return where(reduziert, p.taggeld_satz_reduziert, p.taggeld_satz_voll)


class alv_familienzulagen_zuschlag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Zuschlag fuer Familienzulagen waehrend Arbeitslosigkeit (CHF/Tag)"
    reference = "SR 837.0 Art. 22 Abs. 1"


class alv_taggeld_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoehe des Taggeldes (CHF pro Tag)"
    reference = "SR 837.0 Art. 22"

    def formula(person, period, parameters):
        verdienst = person('alv_versicherter_verdienst', period.this_year)
        satz = person('alv_taggeld_satz', period)
        zuschlag = person('alv_familienzulagen_zuschlag', period)

        # Daily rate = annual insured income / 260 working days * applicable rate + supplement
        taggeld = verdienst / 260 * satz + zuschlag
        return taggeld
