"""SR 832.312.15 Art. 9 – Erteilung des Lernfahrausweises

Generated from: ch/832/de/832.312.15.md

Lernfahrausweis: Mindestalter 17 Jahre, körperliche/geistige Eignung.
- Auswahlzeit: einmalig, 2 Monate befristet
- Übungszeit: nach Grundkurs, 10 Monate befristet, max 2x um 6 Monate
  verlängerbar bei nicht bestandener Prüfung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

MINDESTALTER_LERNFAHRAUSWEIS = 17
AUSWAHLZEIT_MONATE = 2
UEBUNGSZEIT_MONATE = 10
VERLAENGERUNG_MONATE = 6
MAX_VERLAENGERUNGEN = 2


class alter_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person in Jahren"
    reference = "SR 832.312.15 Art. 9 Abs. 1 lit. a"


class grundkurs_erfolgreich_abgeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Grundkurs nach Art. 12 Abs. 1 erfolgreich abgeschlossen"
    reference = "SR 832.312.15 Art. 9 Abs. 3"


class anspruch_lernfahrausweis_kran(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Erfüllt Voraussetzungen für einen Lernfahrausweis (Kran)"
    reference = "SR 832.312.15 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter_jahre', period.this_year)
        geeignet = person('koerperlich_geistig_geeignet_kran', period.this_year)
        verstaendigung = person('kann_sich_am_arbeitsplatz_verstaendigen', period.this_year)

        return (alter >= MINDESTALTER_LERNFAHRAUSWEIS) * geeignet * verstaendigung


class anspruch_lernfahrausweis_uebungszeit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf Lernfahrausweis für Übungszeit (nach Grundkurs)"
    reference = "SR 832.312.15 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        grundvoraussetzung = person('anspruch_lernfahrausweis_kran', period)
        grundkurs = person('grundkurs_erfolgreich_abgeschlossen', period)
        return grundvoraussetzung * grundkurs
