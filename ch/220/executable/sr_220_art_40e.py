"""SR 220 Art. 40e

Generated from: ch/de/220.md

Widerrufsrecht bei Haustuergeschaeften - Form und Frist: Die Widerrufsfrist
betraegt 14 Tage und beginnt, sobald der Kunde den Vertrag beantragt oder
angenommen hat und von den Angaben nach Art. 40d Kenntnis erhalten hat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class tage_seit_vertragsschluss_und_kenntnis(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tage seit Vertragsschluss und Kenntnis der Widerrufsangaben"
    reference = "SR 220 Art. 40e Abs. 2"


class kann_haustuergeschaeft_widerrufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Kunde das Haustuergeschaeft noch widerrufen kann"
    reference = "SR 220 Art. 40e"

    def formula(person, period, parameters):
        ist_haustuergeschaeft = person('ist_haustuergeschaeft', period)
        tage = person('tage_seit_vertragsschluss_und_kenntnis', period)
        widerrufsfrist = parameters(period).or_haustuergeschaeft.widerrufsfrist_tage

        hat_verhandlungen_gewuenscht = person('hat_verhandlungen_ausdruecklich_gewuenscht', period)
        war_markt_oder_messe = person('erklaerung_an_markt_oder_messestand', period)

        # Art. 40c: Kein Widerrufsrecht wenn Verhandlungen gewuenscht oder
        # Erklaerung an Markt/Messe
        kein_widerrufsrecht = (hat_verhandlungen_gewuenscht + war_markt_oder_messe) > 0

        return ist_haustuergeschaeft * not_(kein_widerrufsrecht) * (tage <= widerrufsfrist)


class hat_verhandlungen_ausdruecklich_gewuenscht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Kunde die Vertragsverhandlungen ausdruecklich gewuenscht hat"
    reference = "SR 220 Art. 40c lit. a"


class erklaerung_an_markt_oder_messestand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Erklaerung an einem Markt- oder Messestand abgegeben wurde"
    reference = "SR 220 Art. 40c lit. b"
