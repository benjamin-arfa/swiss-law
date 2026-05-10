"""SR 642.11 Art. 18b

Generated from: ch/642/de/642.11.md

Art. 18b Teilbesteuerung der Einkuenfte aus Beteiligungen des Geschaeftsvermoegens
(Partial taxation of income from business asset participations):
1. Dividends, profit shares, liquidation surpluses and pecuniary benefits from
   shares, GmbH shares, cooperative shares and participation certificates, as
   well as gains from the sale of such participation rights, are taxable at
   70% (after deduction of attributable expenses), provided these participation
   rights represent at least 10% of the share or cooperative capital.
2. Partial taxation on capital gains is only granted if the sold participation
   rights were owned by the taxpayer or the unincorporated business for at
   least one year.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ifd_beteiligungsquote_geschaeftsvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beteiligungsquote am Grund-/Stammkapital (Anteil, z.B. 0.10 = 10%)"
    reference = "SR 642.11 Art. 18b Abs. 1"


class ifd_einkuenfte_beteiligung_brutto(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Brutto-Einkuenfte aus Beteiligungen des Geschaeftsvermoegens (Dividenden, Gewinnanteile etc., CHF)"
    reference = "SR 642.11 Art. 18b Abs. 1"


class ifd_zurechenbarer_aufwand_beteiligung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zurechenbarer Aufwand fuer die Beteiligungseinkuenfte (CHF)"
    reference = "SR 642.11 Art. 18b Abs. 1"


class ifd_veraeusserungsgewinn_beteiligung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewinn aus der Veraeusserung von Beteiligungsrechten (CHF)"
    reference = "SR 642.11 Art. 18b Abs. 2"


class ifd_haltedauer_beteiligung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Haltedauer der veraeusserten Beteiligungsrechte in Jahren"
    reference = "SR 642.11 Art. 18b Abs. 2"


class ifd_steuerbare_beteiligungseinkuenfte(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerbare Einkuenfte aus Beteiligungen nach Teilbesteuerung (CHF)"
    reference = "SR 642.11 Art. 18b"

    def formula(person, period, parameters):
        quote = person('ifd_beteiligungsquote_geschaeftsvermoegen', period)
        brutto = person('ifd_einkuenfte_beteiligung_brutto', period)
        aufwand = person('ifd_zurechenbarer_aufwand_beteiligung', period)
        veraeusserung = person('ifd_veraeusserungsgewinn_beteiligung', period)
        haltedauer = person('ifd_haltedauer_beteiligung_jahre', period)

        p = parameters(period).sr_642_11

        # Art. 18b Abs. 1: Teilbesteuerung bei >= 10% Beteiligung
        qualifiziert = quote >= p.partial_tax_min_participation

        # Dividenden etc.: 70% steuerbar nach Abzug des zurechenbaren Aufwands
        netto_dividenden = max_(brutto - aufwand, 0)
        steuerbar_dividenden = where(qualifiziert,
                                     netto_dividenden * p.partial_tax_rate,
                                     netto_dividenden)

        # Art. 18b Abs. 2: Veraeusserungsgewinne nur bei >= 1 Jahr Haltedauer
        teilbesteuerung_veraeusserung = qualifiziert * (haltedauer >= 1)
        steuerbar_veraeusserung = where(teilbesteuerung_veraeusserung,
                                        veraeusserung * p.partial_tax_rate,
                                        veraeusserung)

        return steuerbar_dividenden + steuerbar_veraeusserung
