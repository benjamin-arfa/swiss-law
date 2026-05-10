"""SR 413.12 Art. 14

Generated from: ch/413/de/413.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 14 defines the exam subject structure and exclusion rules


class schwerpunktfach_code(Variable):
    """Code des gewaehlten Schwerpunktfachs (a-h gemaess Art. 14 Abs. 3)"""
    value_type = str
    max_length = 50
    entity = Person
    definition_period = YEAR
    label = "Gewaehltes Schwerpunktfach"
    reference = "SR 413.12 Art. 14 Abs. 3"


class ergaenzungsfach_code(Variable):
    """Code des gewaehlten Ergaenzungsfachs (a-m gemaess Art. 14 Abs. 4)"""
    value_type = str
    max_length = 50
    entity = Person
    definition_period = YEAR
    label = "Gewaehltes Ergaenzungsfach"
    reference = "SR 413.12 Art. 14 Abs. 4"


class grundlagenfach_bildnerisch_oder_musik(Variable):
    """Wahl im Grundlagenfach: 'bildnerisches_gestalten' oder 'musik'"""
    value_type = str
    max_length = 30
    entity = Person
    definition_period = YEAR
    label = "Wahl bildnerisches Gestalten oder Musik als Grundlagenfach"
    reference = "SR 413.12 Art. 14 Abs. 2 Bst. j"


class dritte_sprache_als_grundlagenfach(Variable):
    """Welche dritte Sprache als Grundlagenfach gewaehlt wurde"""
    value_type = str
    max_length = 20
    entity = Person
    definition_period = YEAR
    label = "Dritte Sprache als Grundlagenfach"
    reference = "SR 413.12 Art. 14 Abs. 2 Bst. c"


class anzahl_pruefungsfaecher(Variable):
    """Gesamtanzahl der Pruefungsfaecher (muss 12 sein)"""
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Pruefungsfaecher"
    reference = "SR 413.12 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        # Immer 12: 10 Grundlagenfaecher + 1 Schwerpunktfach + 1 Ergaenzungsfach
        return person.filled_array(12)


class kombination_gueltig(Variable):
    """Ob die gewaehlte Faecherkombination gueltig ist (Art. 14 Abs. 5)

    Ausgeschlossene Kombinationen:
    a) gleiche Sprache als Grundlagen- und Schwerpunktfach
    b) gleiches Fach als Schwerpunkt- und Ergaenzungsfach
    c) bild. Gest./Musik als Schwerpunkt -> kein bild.Gest./Musik/Sport als Ergaenzung
    d) gleiches Fach aus bild.Gest./Musik als Grundlagen- und Ergaenzungsfach
    """
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Faecherkombination ist gueltig"
    reference = "SR 413.12 Art. 14 Abs. 5"
    default_value = True
