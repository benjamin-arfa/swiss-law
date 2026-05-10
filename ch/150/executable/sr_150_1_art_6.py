"""SR 150.1 Art. 6

Generated from: ch/150/de/150.1.md

Vorschlagsrecht, Ernennung und Amtszeit: Bundesrat ernennt auf Antrag
von EJPD und EDA. NGOs koennen Kandidaten vorschlagen.
Amtszeit 4 Jahre, hoechstens zweimal wiederwaehlbar.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class amtszeit_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Amtszeit der Kommissionsmitglieder in Jahren"
    reference = "SR 150.1 Art. 6 Abs. 3"
    default_value = 4


class anzahl_bisherige_wiederwahlen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl bisheriger Wiederwahlen des Kommissionsmitglieds"
    reference = "SR 150.1 Art. 6 Abs. 3"


class ist_wiederwahl_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Kommissionsmitglied wiedergewaehlt werden kann (max. 2 Wiederwahlen)"
    reference = "SR 150.1 Art. 6 Abs. 3"

    def formula(person, period, parameters):
        return person('anzahl_bisherige_wiederwahlen', period) < 2
