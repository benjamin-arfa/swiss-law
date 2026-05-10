"""SR 810.211 Art. 15a

Generated from: ch/810/de/810.211.md

Art. 15a: Meldung von Lebendspenden an das BAG.

Abs. 1: Wer einer lebenden Person Organe entnimmt, muss dem BAG
folgende Daten melden:
  a. Geburtsjahr, Geschlecht, Blutgruppe, Nationalitaet von Spender/in
     und Empfaenger/in
  b. Wohnsitzland; bei weniger als 3 Monaten Wohnsitz CH auch
     vorhergehendes Wohnsitzland
  c. Beziehung zwischen Spender/in und Empfaenger/in
  d. Welches Organ wann entnommen wurde
  e. Ob und wann das Organ transplantiert wurde
  f. Einverstaendnis mit Gesundheitsnachverfolgung

Abs. 2: Meldefrist: spaetestens 1 Woche nach der Entnahme.

Abs. 3: Meldung erfolgt via SOAS (Swiss Organ Allocation System).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class organ_lebendspende_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einer lebenden Person wurde ein Organ entnommen"
    reference = "SR 810.211 Art. 15a Abs. 1"


class tage_seit_entnahme(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tage seit der Organentnahme"
    reference = "SR 810.211 Art. 15a Abs. 2"


class meldung_bag_erfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Meldung der Lebendspende an das BAG ist erfolgt"
    reference = "SR 810.211 Art. 15a Abs. 2"


class meldepflicht_bag_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Meldefrist von 1 Woche nach Entnahme an BAG ist eingehalten (Art. 15a Abs. 2)"
    reference = "SR 810.211 Art. 15a Abs. 2"

    def formula(person, period, parameters):
        entnahme = person('organ_lebendspende_erfolgt', period)
        meldung = person('meldung_bag_erfolgt', period)
        tage = person('tage_seit_entnahme', period)
        max_tage = parameters(period).sr_810_211.art_15a.meldefrist_tage
        fristgerecht = tage <= max_tage
        return entnahme * meldung * fristgerecht


class wohnsitz_ch_weniger_als_3_monate(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Wohnsitz in der Schweiz seit weniger als 3 Monaten begruendet"
    reference = "SR 810.211 Art. 15a Abs. 1 lit. b"


class vorhergehendes_wohnsitzland_meldepflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Vorhergehendes Wohnsitzland muss gemeldet werden (Wohnsitz CH < 3 Monate)"
    reference = "SR 810.211 Art. 15a Abs. 1 lit. b"

    def formula(person, period, parameters):
        return person('wohnsitz_ch_weniger_als_3_monate', period)
