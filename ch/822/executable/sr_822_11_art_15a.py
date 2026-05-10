"""SR 822.11 Art. 15a

Generated from: ch/822/de/822.11.md

Art. 15a: Taegliche Ruhezeit
- Abs. 1: Mindestens 11 aufeinanderfolgende Stunden taegliche Ruhezeit
- Abs. 2: Fuer erwachsene AN einmal pro Woche auf 8 Stunden reduzierbar,
  sofern 11-Stunden-Durchschnitt ueber 2 Wochen eingehalten wird
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class arg_taegliche_ruhezeit_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegliche Ruhezeit in aufeinanderfolgenden Stunden"
    reference = "SR 822.11 Art. 15a Abs. 1"


class arg_arbeitnehmer_minderjaehrig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer ist minderjaehrig (unter 18 Jahren)"
    reference = "SR 822.11 Art. 15a Abs. 2"


class arg_ruhezeit_herabsetzung_genutzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Einmalige woechentliche Herabsetzung der Ruhezeit auf 8 Stunden wird genutzt"
    reference = "SR 822.11 Art. 15a Abs. 2"


class arg_mindest_taegliche_ruhezeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesetzliche Mindest-Ruhezeit in Stunden"
    reference = "SR 822.11 Art. 15a"

    def formula(person, period, parameters):
        minderjaehrig = person('arg_arbeitnehmer_minderjaehrig', period)
        herabsetzung = person('arg_ruhezeit_herabsetzung_genutzt', period)
        # Minors always 11h; adults can go to 8h once/week
        kann_herabsetzen = not_(minderjaehrig) * herabsetzung
        return where(kann_herabsetzen, 8.0, 11.0)


class arg_taegliche_ruhezeit_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegliche Ruhezeit entspricht den gesetzlichen Anforderungen"
    reference = "SR 822.11 Art. 15a"

    def formula(person, period, parameters):
        ruhezeit = person('arg_taegliche_ruhezeit_stunden', period)
        mindest = person('arg_mindest_taegliche_ruhezeit', period)
        return ruhezeit >= mindest
