"""SR 642.11 Art. 20

Generated from: ch/642/de/642.11.md

Art. 20 Bewegliches Vermoegen (Movable property income):
1. Taxable are income from movable property, in particular:
   a. Interest from deposits, including paid-out returns from redeemable
      single-premium capital insurance (tax-free if for retirement provision:
      payout after age 60, contract >= 5 years, started before age 66);
   b. Income from sale/repayment of bonds with predominantly single-rate
      interest (zero-coupon bonds, discount bonds);
   c. Dividends, profit shares, liquidation surpluses and monetary benefits
      from participations of all kinds (including bonus shares);
   d. Income from rental, lease, usufruct of movable property or exploitable rights;
   e. Income from shares in collective investment schemes (exceeding direct
      real estate income);
   f. Income from intangible assets.
1bis. Dividends etc. from participations >= 10% of capital are taxable
     at 70% (Teilbesteuerung).
2. Proceeds from subscription rights are not taxable if private property.
3. Return of capital contribution reserves (after 31.12.1996) treated
   like return of share capital. Abs. 4-8 contain special rules for
   listed companies and capital bands.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class einkommen_zinsen_guthaben(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zinsen aus Guthaben (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. a"


class einkommen_kapitalversicherung_einmalpraemie(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausbezahlte Ertraege aus rueckkaufsfaehigen Kapitalversicherungen mit Einmalpraemie (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. a"


class kapitalversicherung_dient_vorsorge(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kapitalversicherung dient der Vorsorge (Auszahlung ab 60, Vertrag >= 5 Jahre, vor 66 begruendet)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. a"


class einkommen_kapitalversicherung_steuerbar(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbarer Ertrag aus Kapitalversicherungen mit Einmalpraemie (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        ertrag = person('einkommen_kapitalversicherung_einmalpraemie', period)
        dient_vorsorge = person('kapitalversicherung_dient_vorsorge', period)
        # Steuerfrei wenn der Vorsorge dienend
        return where(dient_vorsorge, 0, ertrag)


class einkommen_obligationen_einmalverzinsung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus Veraeusserung/Rueckzahlung von Obligationen mit ueberwiegender Einmalverzinsung (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. b"


class einkommen_dividenden_beteiligungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Dividenden, Gewinnanteile, Liquidationsueberschuesse und geldwerte Vorteile aus Beteiligungen (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. c"


class beteiligung_anteil_mindestens_10_prozent(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beteiligungsrechte >= 10% des Grund- oder Stammkapitals"
    reference = "SR 642.11 Art. 20 Abs. 1bis"


class einkommen_dividenden_steuerbar(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbarer Betrag aus Dividenden/Beteiligungen nach Teilbesteuerung (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. c, Abs. 1bis"

    def formula(person, period, parameters):
        dividenden = person('einkommen_dividenden_beteiligungen', period)
        qualifiziert = person('beteiligung_anteil_mindestens_10_prozent', period)
        # Abs. 1bis: bei >= 10% Beteiligung nur 70% steuerbar
        return where(qualifiziert, dividenden * 0.70, dividenden)


class einkommen_vermietung_bewegliche_sachen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus Vermietung/Verpachtung/Nutzniessung beweglicher Sachen oder nutzbarer Rechte (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. d"


class einkommen_kollektive_kapitalanlagen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus Anteilen an kollektiven Kapitalanlagen (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. e"


class einkommen_immaterielle_gueter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkuenfte aus immateriellen Guetern (CHF)"
    reference = "SR 642.11 Art. 20 Abs. 1 Bst. f"


class rueckzahlung_kapitaleinlagereserven(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Rueckzahlung von Kapitaleinlagereserven (CHF, steuerfrei nach Abs. 3)"
    reference = "SR 642.11 Art. 20 Abs. 3"


class einkommen_bewegliches_vermoegen_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamte steuerbare Einkuenfte aus beweglichem Vermoegen (CHF)"
    reference = "SR 642.11 Art. 20"

    def formula(person, period, parameters):
        zinsen = person('einkommen_zinsen_guthaben', period)
        kapitalversicherung = person('einkommen_kapitalversicherung_steuerbar', period)
        obligationen = person('einkommen_obligationen_einmalverzinsung', period)
        dividenden = person('einkommen_dividenden_steuerbar', period)
        vermietung_bew = person('einkommen_vermietung_bewegliche_sachen', period)
        kollektiv = person('einkommen_kollektive_kapitalanlagen', period)
        immateriell = person('einkommen_immaterielle_gueter', period)

        return (zinsen + kapitalversicherung + obligationen + dividenden +
                vermietung_bew + kollektiv + immateriell)
