"""SR 251.5 Art. 6

Generated from: ch/251/de/251.5.md

Mildernde Umstaende: Verminderung des Betrags wenn das Unternehmen
den Verstoss beendet hat, nur passive Rolle spielte oder
Vergeltungsmassnahmen nicht durchgefuehrt hat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verstoss_frueh_beendet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen den Verstoss nach erstem Eingreifen des Sekretariats beendet hat"
    reference = "SR 251.5 Art. 6 Abs. 1"


class ausschliesslich_passive_rolle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen ausschliesslich eine passive Rolle gespielt hat"
    reference = "SR 251.5 Art. 6 Abs. 2 Bst. a"


class vergeltungsmassnahmen_nicht_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob vereinbarte Vergeltungsmassnahmen nicht durchgefuehrt wurden"
    reference = "SR 251.5 Art. 6 Abs. 2 Bst. b"


class mildernde_umstaende_reduktion_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prozentuale Reduktion wegen mildernder Umstaende"
    reference = "SR 251.5 Art. 6"


class sanktion_nach_mildernd(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Sanktionsbetrag nach Beruecksichtigung mildernder Umstaende"
    reference = "SR 251.5 Art. 6"

    def formula(person, period, parameters):
        betrag = person('sanktion_nach_erschwerend', period)
        reduktion = person('mildernde_umstaende_reduktion_prozent', period)
        return betrag * (1 - reduktion / 100)
