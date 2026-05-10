"""SR 413.12 Art. 22

Generated from: ch/413/de/413.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_ungenuegend(Variable):
    """Anzahl Faecher mit Note unter 4"""
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Faecher mit ungenuegendem Ergebnis (Note < 4)"
    reference = "SR 413.12 Art. 22 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        noten = [
            person('note_erstsprache', period),
            person('note_zweite_landessprache', period),
            person('note_dritte_sprache', period),
            person('note_mathematik', period),
            person('note_biologie', period),
            person('note_chemie', period),
            person('note_physik', period),
            person('note_geschichte', period),
            person('note_geografie', period),
            person('note_bildnerisches_gestalten_oder_musik', period),
            person('note_schwerpunktfach', period),
            person('note_ergaenzungsfach', period),
            person('note_maturaarbeit', period),
        ]
        count = sum((note < 4) for note in noten)
        return count


class summe_notenabweichungen(Variable):
    """Summe der Abweichungen von 4 nach unten ueber alle Faecher"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Summe der Notenabweichungen von 4 nach unten"
    reference = "SR 413.12 Art. 22 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        noten = [
            person('note_erstsprache', period),
            person('note_zweite_landessprache', period),
            person('note_dritte_sprache', period),
            person('note_mathematik', period),
            person('note_biologie', period),
            person('note_chemie', period),
            person('note_physik', period),
            person('note_geschichte', period),
            person('note_geografie', period),
            person('note_bildnerisches_gestalten_oder_musik', period),
            person('note_schwerpunktfach', period),
            person('note_ergaenzungsfach', period),
            person('note_maturaarbeit', period),
        ]
        abweichungen = sum(max_(4 - note, 0) for note in noten)
        return abweichungen


class maturitaetspruefung_bestanden(Variable):
    """Ob die Maturitaetspruefung bestanden ist gemaess Art. 22 Abs. 1

    Bestanden wenn:
    a) mindestens 105 Punkte; ODER
    b) 84-104.5 Punkte UND hoechstens 4 ungenuegende Faecher UND
       Summe Abweichungen von 4 nach unten hoechstens 7
    """
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Maturitaetspruefung bestanden"
    reference = "SR 413.12 Art. 22 Abs. 1"

    def formula(person, period, parameters):
        punktzahl = person('punktzahl_maturitaet', period)
        anzahl_ungen = person('anzahl_ungenuegennd', period)
        summe_abw = person('summe_notenabweichungen', period)

        # Variante a: mindestens 105 Punkte
        bestanden_a = punktzahl >= 105

        # Variante b: 84-104.5 Punkte, max 4 ungenuegende, max 7 Abweichungspunkte
        punkte_im_bereich = (punktzahl >= 84) * (punktzahl <= 104.5)
        max_vier_ungen = anzahl_ungen <= 4
        max_sieben_abw = summe_abw <= 7
        bestanden_b = punkte_im_bereich * max_vier_ungen * max_sieben_abw

        return bestanden_a + bestanden_b * (1 - bestanden_a)


class maturitaetspruefung_nicht_bestanden_fernbleiben(Variable):
    """Pruefung nicht bestanden wegen Fernbleiben ohne triftigen Grund"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pruefung nicht bestanden wegen Fernbleiben"
    reference = "SR 413.12 Art. 22 Abs. 2 Bst. b"
    default_value = False


class maturitaetspruefung_nicht_bestanden_unredlichkeit(Variable):
    """Pruefung nicht bestanden wegen unerlaubter Hilfsmittel/Unredlichkeit"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pruefung nicht bestanden wegen Unredlichkeit"
    reference = "SR 413.12 Art. 22 Abs. 2 Bst. c"
    default_value = False
