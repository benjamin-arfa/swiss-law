"""SR 642.11 Art. 13

Generated from: ch/642/de/642.11.md

Art. 13 Haftung und Mithaftung fuer die Steuer (Tax liability and joint liability):
1. Spouses living in legally and factually undissolved marriage are jointly
   liable for the total tax. Each spouse is only liable for their share if
   one is insolvent. They are also jointly liable for the part of the total
   tax attributable to children's income.
2. In case of legal or factual separation, joint liability ceases, including
   for all outstanding tax debts.
3. The following are jointly liable with the taxpayer:
   a. children under parental authority, up to their share of the total tax;
   b. partners residing in Switzerland, up to their partnership shares, for
      taxes of partners residing abroad;
   c. buyers and sellers of Swiss real estate, up to 3% of the purchase price,
      for taxes owed by the dealer/broker without Swiss tax domicile;
   d. persons liquidating businesses or selling Swiss real estate or secured
      claims, up to the net proceeds, if the taxpayer has no Swiss domicile.
4. Estate administrators and executors are jointly liable with the successor,
   up to the amount corresponding to the tax based on the estate value at
   the time of death. Liability ceases if due diligence is proven.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ifd_solidarhaftung_ehegatten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Solidarhaftung der Ehegatten fuer die Gesamtsteuer besteht"
    reference = "SR 642.11 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        verheiratet = person('ist_verheiratet_zusammenlebend', period)
        # Art. 13 Abs. 2: bei Trennung entfaellt die Solidarhaftung
        return verheiratet


class ifd_ehegatte_zahlungsunfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Ehegatte zahlungsunfaehig ist"
    reference = "SR 642.11 Art. 13 Abs. 1"


class ifd_anteil_gesamtsteuer_person(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Person an der Gesamtsteuer (CHF)"
    reference = "SR 642.11 Art. 13 Abs. 1"


class ifd_gesamtsteuer_ehepaar(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtsteuer des Ehepaars (CHF)"
    reference = "SR 642.11 Art. 13 Abs. 1"


class ifd_haftungsbetrag_ehegatte(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Haftungsbetrag des Ehegatten (CHF)"
    reference = "SR 642.11 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        solidarhaftung = person('ifd_solidarhaftung_ehegatten', period)
        zahlungsunfaehig = person('ifd_ehegatte_zahlungsunfaehig', period)
        anteil = person('ifd_anteil_gesamtsteuer_person', period)
        gesamt = person('ifd_gesamtsteuer_ehepaar', period)

        # Normally jointly liable for the full amount
        # If one spouse is insolvent, each only liable for their own share
        return where(solidarhaftung,
                     where(zahlungsunfaehig, anteil, gesamt),
                     anteil)


class ifd_kaufpreis_liegenschaft(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kaufpreis der in der Schweiz gelegenen Liegenschaft (CHF)"
    reference = "SR 642.11 Art. 13 Abs. 3 Bst. c"


class ifd_mithaftung_liegenschaft(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mithaftungsbetrag bei Liegenschaftshandel (max. 3% des Kaufpreises, CHF)"
    reference = "SR 642.11 Art. 13 Abs. 3 Bst. c"

    def formula(person, period, parameters):
        kaufpreis = person('ifd_kaufpreis_liegenschaft', period)
        p = parameters(period).sr_642_11
        return kaufpreis * p.liability_real_estate_rate
