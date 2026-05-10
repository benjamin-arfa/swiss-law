"""SR 211.111.1 Art. 7

Generated from: ch/211/de/211.111.1.md

Sterilisation dauernd Urteilsunfaehiger: Grundsaetzlich ausgeschlossen,
ausnahmsweise zulaessig unter kumulativen Bedingungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_dauernd_urteilsunfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person dauernd urteilsunfaehig ist"
    reference = "SR 211.111.1 Art. 7 Abs. 1"


class sterilisation_im_interesse_der_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sterilisation nach den gesamten Umstaenden im Interesse der betroffenen Person vorgenommen wird"
    reference = "SR 211.111.1 Art. 7 Abs. 2 lit. a"


class keine_geeignete_alternative_verhuetung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zeugung nicht durch andere Verhuetungsmethoden oder freiwillige Sterilisation des Partners verhindert werden kann"
    reference = "SR 211.111.1 Art. 7 Abs. 2 lit. b"


class zeugung_und_geburt_zu_rechnen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob mit der Zeugung und der Geburt eines Kindes zu rechnen ist"
    reference = "SR 211.111.1 Art. 7 Abs. 2 lit. c"


class trennung_vom_kind_unvermeidlich_oder_gesundheitsgefaehrdung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob nach Geburt die Trennung vom Kind unvermeidlich waere oder die Schwangerschaft die Gesundheit erheblich gefaehrden wuerde"
    reference = "SR 211.111.1 Art. 7 Abs. 2 lit. d"


class keine_aussicht_auf_urteilsfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob keine Aussicht besteht, dass die Person jemals die Urteilsfaehigkeit erlangt"
    reference = "SR 211.111.1 Art. 7 Abs. 2 lit. e"


class operationsmethode_mit_refertilisierungsaussicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Operationsmethode mit der groessten Refertilisierungsaussicht gewaehlt wird"
    reference = "SR 211.111.1 Art. 7 Abs. 2 lit. f"


class sterilisation_dauernd_urteilsunfaehiger_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sterilisation einer dauernd urteilsunfaehigen Person ausnahmsweise zulaessig ist"
    reference = "SR 211.111.1 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        ueber_16 = person('alter', period) >= 16
        dauernd = person('ist_dauernd_urteilsunfaehig', period)
        interesse = person('sterilisation_im_interesse_der_person', period)
        keine_alternative = person('keine_geeignete_alternative_verhuetung', period)
        zeugung = person('zeugung_und_geburt_zu_rechnen', period)
        trennung = person('trennung_vom_kind_unvermeidlich_oder_gesundheitsgefaehrdung', period)
        keine_aussicht = person('keine_aussicht_auf_urteilsfaehigkeit', period)
        methode = person('operationsmethode_mit_refertilisierungsaussicht', period)
        behoerde = person('zustimmung_erwachsenenschutzbehoerde', period)
        # Alle Bedingungen muessen kumulativ erfuellt sein
        return ueber_16 * dauernd * interesse * keine_alternative * zeugung * trennung * keine_aussicht * methode * behoerde
