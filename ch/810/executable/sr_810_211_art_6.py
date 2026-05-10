"""SR 810.211 Art. 6

Generated from: ch/810/de/810.211.md

Art. 6: Vertrauensperson.

Abs. 1: Wer das 16. Lebensjahr vollendet hat, kann eine
Vertrauensperson bestimmen.

Abs. 2: Hat die verstorbene Person mehrere Vertrauenspersonen
bestimmt, so ist die Entnahme zulaessig, wenn:
  a. alle innerhalb angemessener Zeit erreichbaren zustimmen
  b. von nicht erreichbaren Vertrauenspersonen kein Widerspruch
     bekannt wird
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kann_vertrauensperson_bestimmen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person kann eine Vertrauensperson fuer Organspende-Entscheid bestimmen (mind. 16 Jahre)"
    reference = "SR 810.211 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter', period)
        return alter >= 16


class anzahl_vertrauenspersonen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl bestimmter Vertrauenspersonen"
    reference = "SR 810.211 Art. 6 Abs. 2"


class alle_erreichbaren_vertrauenspersonen_stimmen_zu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Alle innerhalb angemessener Zeit erreichbaren Vertrauenspersonen stimmen zu"
    reference = "SR 810.211 Art. 6 Abs. 2 lit. a"


class kein_widerspruch_nicht_erreichbarer_vertrauenspersonen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Von nicht erreichbaren Vertrauenspersonen ist kein Widerspruch bekannt"
    reference = "SR 810.211 Art. 6 Abs. 2 lit. b"


class organentnahme_zulaessig_vertrauenspersonen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Organentnahme ist mit Zustimmung der Vertrauenspersonen zulaessig (Art. 6 Abs. 2)"
    reference = "SR 810.211 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        zustimmung = person('alle_erreichbaren_vertrauenspersonen_stimmen_zu', period)
        kein_widerspruch = person('kein_widerspruch_nicht_erreichbarer_vertrauenspersonen', period)
        return zustimmung * kein_widerspruch
