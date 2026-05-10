"""SR 956.1 Art. 9

Generated from: ch/956/de/956.1.md

Verwaltungsrat der FINMA:
- 7-9 fachkundige Mitglieder, unabhängig von Beaufsichtigten
- Amtsdauer 4 Jahre, max. 2 Wiederwahlen
- Präsident darf keine andere wirtschaftliche Tätigkeit ausüben
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_verwaltungsratsmitglieder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Verwaltungsratsmitglieder der FINMA"
    reference = "SR 956.1 Art. 9 Abs. 2"


class ist_fachkundig_und_unabhaengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das VR-Mitglied fachkundig und von Beaufsichtigten unabhängig ist"
    reference = "SR 956.1 Art. 9 Abs. 2"


class anzahl_bisherige_wiederwahlen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl bisheriger Wiederwahlen des VR-Mitglieds"
    reference = "SR 956.1 Art. 9 Abs. 2"


class verwaltungsrat_zusammensetzung_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zusammensetzung des Verwaltungsrats den Anforderungen entspricht"
    reference = "SR 956.1 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        anzahl = person('anzahl_verwaltungsratsmitglieder', period)
        min_mitglieder = parameters(period).sr_956_1.min_verwaltungsratsmitglieder
        max_mitglieder = parameters(period).sr_956_1.max_verwaltungsratsmitglieder
        return (anzahl >= min_mitglieder) * (anzahl <= max_mitglieder)


class wiederwahl_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Wiederwahl des VR-Mitglieds zulässig ist"
    reference = "SR 956.1 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        wiederwahlen = person('anzahl_bisherige_wiederwahlen', period)
        max_wiederwahlen = parameters(period).sr_956_1.max_wiederwahlen
        return wiederwahlen < max_wiederwahlen
