"""SR 810.211 Art. 5

Generated from: ch/810/de/810.211.md

Art. 5: Entscheid der naechsten Angehoerigen bei Organspende.

Abs. 1: Zum Entscheid befugt ist, wer mit der verstorbenen Person am
engsten verbunden war und das 16. Altersjahr vollendet hat.

Abs. 2: Rangfolge der naechsten Angehoerigen (bei regelmaessigem
persoenlichen Kontakt bis zum Tod):
  a. Ehegatte, eingetragene/r Partner/in, Lebenspartner/in
  b. Kinder
  c. Eltern und Geschwister
  d. Grosseltern und Grosskinder
  e. andere nahestehende Personen

Abs. 3: Bei mehreren Angehoerigen gleicher Stufe ist die Entnahme
zulaessig wenn:
  a. alle innerhalb angemessener Zeit erreichbaren zustimmen
  b. von nicht erreichbaren kein Widerspruch bekannt wird
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alter_mindestens_16(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person hat das 16. Altersjahr vollendet"
    reference = "SR 810.211 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter', period)
        return alter >= 16


class ist_engste_bezugsperson(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person war mit der verstorbenen Person am engsten verbunden"
    reference = "SR 810.211 Art. 5 Abs. 1"


class angehoerigen_rang(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Rang der naechsten Angehoerigen (1=Ehegatte, 2=Kinder, 3=Eltern/Geschwister, 4=Grosseltern/Grosskinder, 5=andere)"
    reference = "SR 810.211 Art. 5 Abs. 2"


class entscheid_befugt_organspende(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist zum Entscheid ueber Organspende befugt (Art. 5 Abs. 1)"
    reference = "SR 810.211 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        alter_ok = person('alter_mindestens_16', period)
        engste = person('ist_engste_bezugsperson', period)
        return alter_ok * engste


class alle_erreichbaren_stimmen_zu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Alle innerhalb angemessener Zeit erreichbaren Angehoerigen stimmen der Entnahme zu"
    reference = "SR 810.211 Art. 5 Abs. 3 lit. a"


class kein_widerspruch_nicht_erreichbarer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Von nicht erreichbaren Angehoerigen ist kein Widerspruch bekannt"
    reference = "SR 810.211 Art. 5 Abs. 3 lit. b"


class organentnahme_zulaessig_mehrere_angehoerige(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organentnahme ist bei mehreren naechsten Angehoerigen zulaessig (Art. 5 Abs. 3)"
    reference = "SR 810.211 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        zustimmung = person('alle_erreichbaren_stimmen_zu', period)
        kein_widerspruch = person('kein_widerspruch_nicht_erreichbarer', period)
        return zustimmung * kein_widerspruch
