"""SR 142.206 Art. 17

Generated from: ch/142/de/142.206.md

Berichtigung, Ergaenzung oder Loeschung der Daten des
Informationsmechanismus: Das SEM korrigiert auf Gesuch hin,
wenn unvorhersehbare Ereignisse oder inzwischen bestehende
Aufenthaltsberechtigung nachgewiesen werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unvorhersehbare_ereignisse_aufenthaltsdauer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob unvorhersehbare, ernste Ereignisse die Person zur Ueberziehung der Aufenthaltsdauer gezwungen haben"
    reference = "SR 142.206 Art. 17 Bst. a"


class inzwischen_aufenthaltsberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person inzwischen berechtigt ist, sich im Schengen-Raum aufzuhalten"
    reference = "SR 142.206 Art. 17 Bst. b"


class ees_informationsmechanismus_korrektur_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das SEM Daten des Informationsmechanismus berichtigen, ergaenzen oder loeschen darf"
    reference = "SR 142.206 Art. 17"

    def formula_2022_05(person, period, parameters):
        return (
            person('unvorhersehbare_ereignisse_aufenthaltsdauer', period)
            + person('inzwischen_aufenthaltsberechtigt', period)
        ) > 0
