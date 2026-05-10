"""SR 822.11 Art. 17b

Generated from: ch/822/de/822.11.md

Art. 17b: Lohnzuschlag und Zeitkompensation bei Nachtarbeit
- Abs. 1: Voruebergehende Nachtarbeit: Lohnzuschlag von mindestens 25%
- Abs. 2: Dauernde/regelmaessige Nachtarbeit: Kompensation von 10% der
  Nachtarbeitszeit als Ausgleichsruhezeit (innerhalb eines Jahres)
- Abs. 3: Keine Ausgleichsruhezeit wenn:
  a. Schichtdauer inkl. Pausen <= 7 Stunden, oder
  b. Vier-Tage-Woche, oder
  c. Gleichwertige Ausgleichsruhezeit durch GAV
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class arg_nachtarbeit_voruebergehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer verrichtet voruebergehende Nachtarbeit"
    reference = "SR 822.11 Art. 17b Abs. 1"


class arg_nachtarbeit_dauernd(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer verrichtet dauernde oder regelmaessig wiederkehrende Nachtarbeit"
    reference = "SR 822.11 Art. 17b Abs. 2"


class arg_nachtarbeit_stunden_monat(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    default_value = 0.0
    label = "Nachtarbeitsstunden im Monat"
    reference = "SR 822.11 Art. 17b Abs. 2"


class arg_nachtarbeit_lohnzuschlag_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Lohnzuschlag fuer Nachtarbeit in Prozent"
    reference = "SR 822.11 Art. 17b Abs. 1"

    def formula(person, period, parameters):
        voruebergehend = person('arg_nachtarbeit_voruebergehend', period)
        # 25% surcharge for temporary night work; 0% for permanent (compensated by time off)
        return where(voruebergehend, 25.0, 0.0)


class arg_nachtarbeit_schichtdauer_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    default_value = 8.0
    label = "Durchschnittliche betriebliche Schichtdauer inkl. Pausen in Stunden"
    reference = "SR 822.11 Art. 17b Abs. 3 Bst. a"


class arg_nachtarbeit_vier_tage_woche(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Arbeitnehmer arbeitet in Vier-Tage-Woche (nur 4 Naechte/Woche)"
    reference = "SR 822.11 Art. 17b Abs. 3 Bst. b"


class arg_nachtarbeit_gav_ausgleich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Gleichwertige Ausgleichsruhezeit durch GAV gewaehrt"
    reference = "SR 822.11 Art. 17b Abs. 3 Bst. c"


class arg_nachtarbeit_ausgleichsruhezeit_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Befreiung von der 10%-Ausgleichsruhezeit bei Nachtarbeit"
    reference = "SR 822.11 Art. 17b Abs. 3"

    def formula(person, period, parameters):
        schicht_kurz = person('arg_nachtarbeit_schichtdauer_stunden', period) <= 7.0
        vier_tage = person('arg_nachtarbeit_vier_tage_woche', period)
        gav = person('arg_nachtarbeit_gav_ausgleich', period)
        return schicht_kurz + vier_tage + gav > 0


class arg_nachtarbeit_ausgleichsruhezeit_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Ausgleichsruhezeit fuer Nachtarbeit in Stunden"
    reference = "SR 822.11 Art. 17b Abs. 2"

    def formula(person, period, parameters):
        dauernd = person('arg_nachtarbeit_dauernd', period)
        stunden = person('arg_nachtarbeit_stunden_monat', period)
        befreit = person('arg_nachtarbeit_ausgleichsruhezeit_befreit', period)
        # 10% of night work hours as compensatory rest
        kompensation = stunden * 0.10
        return where(dauernd * not_(befreit), kompensation, 0.0)
