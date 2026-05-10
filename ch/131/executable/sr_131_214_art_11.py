"""SR 131.214 Art. 11

Generated from: ch/131/de/131.214.md

Rechtsgleichheit:
1. Alle Menschen sind vor dem Gesetze gleich.
2. Niemand darf wegen seiner Herkunft, seines Geschlechts, seiner Rasse, seiner Sprache,
   seiner sozialen Stellung oder seiner Weltanschauung oder Religion benachteiligt oder bevorzugt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class herkunft(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Herkunft der Person"


class geschlecht(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Geschlecht der Person"


class rasse_ethnizitaet(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Rasse oder Ethnizität der Person"


class sprache(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Sprache der Person"


class soziale_stellung(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Soziale Stellung der Person"


class weltanschauung(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Weltanschauung der Person"


class religion(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Religion der Person"


class rechtsgleichheit_garantiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Rechtsgleichheit verfassungsrechtlich garantiert ist"
    reference = "SR 131.214 Art. 11 Abs. 1"
    default_value = True

    def formula(person, period, parameters):
        # All people are equal before the law - this is guaranteed for everyone
        return parameters(period).grundrechte_uri.rechtsgleichheit_schutz


class diskriminierung_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Diskriminierung verfassungsrechtlich verboten ist"
    reference = "SR 131.214 Art. 11 Abs. 2"
    default_value = True

    def formula(person, period, parameters):
        # Discrimination is constitutionally prohibited
        return parameters(period).grundrechte_uri.diskriminierungsverbot


class benachteiligung_vorliegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine verfassungswidrige Benachteiligung vorliegt"
    reference = "SR 131.214 Art. 11 Abs. 2"
    default_value = False


class anspruch_gleichbehandlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Gleichbehandlung vor dem Gesetz"
    reference = "SR 131.214 Art. 11"

    def formula(person, period, parameters):
        # Everyone has a right to equal treatment before the law
        rechtsgleichheit = person('rechtsgleichheit_garantiert', period)
        diskriminierung_verboten = person('diskriminierung_verboten', period)

        return rechtsgleichheit * diskriminierung_verboten


class verfassungswidriger_akt_vorliegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein verfassungswidriger Akt der Ungleichbehandlung vorliegt"
    reference = "SR 131.214 Art. 11"

    def formula(person, period, parameters):
        benachteiligung = person('benachteiligung_vorliegt', period)
        diskriminierung_verboten = person('diskriminierung_verboten', period)

        # Constitutional violation occurs when discrimination is prohibited but benachteiligung exists
        return diskriminierung_verboten * benachteiligung