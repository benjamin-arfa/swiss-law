"""SR 120.73 Art. 14e

Generated from: ch/120/de/120.73.md

Periodizitaet: Security procedures must be conducted at least every 5 years.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_letztem_sicherheitsverfahren(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Jahre seit dem letzten Sicherheitsverfahren"
    reference = "SR 120.73 Art. 14e Abs. 1"


class sicherheitsrelevante_aenderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sicherheitsrelevante Aenderungen am Schutzobjekt oder der Bedrohungslage vorliegen"
    reference = "SR 120.73 Art. 14e Abs. 2"


class sicherheitsverfahren_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Sicherheitsverfahren durchzufuehren ist"
    reference = "SR 120.73 Art. 14e"

    def formula(person, period, parameters):
        # Abs. 1: Mindestens alle 5 Jahre
        periodisch = person('jahre_seit_letztem_sicherheitsverfahren', period) >= 5

        # Abs. 2: Bei sicherheitsrelevanten Aenderungen unverzueglich
        aenderung = person('sicherheitsrelevante_aenderung', period)

        return periodisch + aenderung > 0
