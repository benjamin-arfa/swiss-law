"""SR 152.31 Art. 15

Generated from: ch/152/de/152.31.md

Fee waiver or reduction: fees waived if collection costs exceed fee amount;
fees below 100 CHF not charged; disability-related costs excluded;
media professionals receive 50% reduction.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gebuehr_betrag_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Berechneter Gebuehrenbetrag in CHF"
    reference = "SR 152.31 Art. 15"


class kosten_gebuehrenerhebung_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kosten der Gebuehrenerhebung in CHF"
    reference = "SR 152.31 Art. 15 Abs. 1"


class gebuehr_unter_mindestbetrag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Gebuehr unter dem Mindestbetrag von 100 CHF liegt"
    reference = "SR 152.31 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        return person('gebuehr_betrag_chf', period) < 100


class gebuehr_wird_nicht_erhoben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob auf die Erhebung der Gebuehr verzichtet wird"
    reference = "SR 152.31 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        unter_mindest = person('gebuehr_unter_mindestbetrag', period)
        kosten = person('kosten_gebuehrenerhebung_chf', period)
        betrag = person('gebuehr_betrag_chf', period)
        kosten_uebersteigen = kosten > betrag
        return unter_mindest + kosten_uebersteigen > 0


class zugangsgesuch_abgelehnt_oder_teilweise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Zugangsgesuch abgelehnt oder nur teilweise gewaehrt wurde"
    reference = "SR 152.31 Art. 15 Abs. 3"


class gebuehr_reduktion_medien_prozent(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Gebuehrenreduktion fuer Medienschaffende in Prozent"
    reference = "SR 152.31 Art. 15 Abs. 4"

    def formula(person, period, parameters):
        return where(person('ist_medienschaffende_person', period), 50, 0)


class gebuehr_mindestbetrag_chf(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestbetrag unter dem keine Gebuehr erhoben wird in CHF"
    reference = "SR 152.31 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        return 100
