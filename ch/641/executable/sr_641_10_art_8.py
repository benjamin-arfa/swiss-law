"""SR 641.10 Art. 8

Generated from: ch/641/de/641.10.md

Art. 8 Beteiligungsrechte (Emission levy rate):
1. The levy on participation rights is 1% and is calculated:
   a. on creation/increase: from the amount flowing to the company, but at least
      the nominal value
   b. on contributions: from the contribution amount
   c. on majority transfer: from the net assets at time of transfer, but at least
      the nominal value of all existing participation rights
3. Assets and rights are valued at market value at time of contribution.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class stg_gegenleistung_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Amount flowing to the company as consideration for participation rights (CHF)"
    reference = "SR 641.10 Art. 8 Abs. 1 Bst. a"


class stg_nennwert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Nominal value of the participation rights (CHF)"
    reference = "SR 641.10 Art. 8 Abs. 1 Bst. a"


class stg_zuschuss_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Amount of shareholder contribution (Zuschuss) (CHF)"
    reference = "SR 641.10 Art. 8 Abs. 1 Bst. b"


class stg_reinvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Net assets of the company at time of majority transfer (CHF)"
    reference = "SR 641.10 Art. 8 Abs. 1 Bst. c"


class stg_nennwert_alle_beteiligungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Total nominal value of all existing participation rights (CHF)"
    reference = "SR 641.10 Art. 8 Abs. 1 Bst. c"


class stg_emissionsabgabe_bemessungsgrundlage(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Tax base for the emission levy (CHF)"
    reference = "SR 641.10 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        begruendung = person('stg_beteiligungsrechte_begruendung', period)
        zuschuss = person('stg_zuschuss_ohne_kapitalerhoehung', period)
        handwechsel = person('stg_handwechsel_mehrheit_liquidiert', period)

        gegenleistung = person('stg_gegenleistung_betrag', period)
        nennwert = person('stg_nennwert', period)
        zuschuss_betrag = person('stg_zuschuss_betrag', period)
        reinvermoegen = person('stg_reinvermoegen', period)
        nennwert_alle = person('stg_nennwert_alle_beteiligungen', period)

        # a. Creation/increase: max(consideration, nominal value)
        basis_begruendung = max_(gegenleistung, nennwert)
        # b. Contributions: contribution amount
        basis_zuschuss = zuschuss_betrag
        # c. Majority transfer: max(net assets, total nominal value)
        basis_handwechsel = max_(reinvermoegen, nennwert_alle)

        return (begruendung * basis_begruendung
                + zuschuss * basis_zuschuss
                + handwechsel * basis_handwechsel)


class stg_emissionsabgabe_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Emission levy amount (CHF) = 1% of tax base"
    reference = "SR 641.10 Art. 8"

    def formula(person, period, parameters):
        bemessungsgrundlage = person('stg_emissionsabgabe_bemessungsgrundlage', period)
        befreit = person('stg_emissionsabgabe_befreit', period)
        satz = parameters(period).sr_641_10.emissionsabgabe_satz

        return where(befreit, 0, bemessungsgrundlage * satz)
