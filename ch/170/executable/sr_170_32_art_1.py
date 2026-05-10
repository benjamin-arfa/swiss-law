"""SR 170.32 Art. 1

Generated from: ch/170/de/170.32.md

Geltungsbereich des Verantwortlichkeitsgesetzes (VG).
Definiert die Personen, die dem Gesetz unterstehen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_bundesratsmitglied(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Mitglied des Bundesrates oder Bundeskanzler (Art. 1 Abs. 1 Bst. b VG)"
    reference = "SR 170.32, Art. 1 Abs. 1 Bst. b"


class ist_mitglied_eidg_gericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Mitglied oder Ersatzmitglied der eidgenössischen Gerichte (Art. 1 Abs. 1 Bst. c VG)"
    reference = "SR 170.32, Art. 1 Abs. 1 Bst. c"


class ist_mitglied_aufsichtsbehoerde_ba(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Mitglied der Aufsichtsbehörde über die Bundesanwaltschaft (Art. 1 Abs. 1 Bst. cbis VG)"
    reference = "SR 170.32, Art. 1 Abs. 1 Bst. cbis"


class ist_beamter_bund(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Beamter oder übrige Arbeitskraft des Bundes (Art. 1 Abs. 1 Bst. e VG)"
    reference = "SR 170.32, Art. 1 Abs. 1 Bst. e"


class ist_mit_oeffentlichen_aufgaben_betraut(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist unmittelbar mit öffentlichrechtlichen Aufgaben des Bundes betraut (Art. 1 Abs. 1 Bst. f VG)"
    reference = "SR 170.32, Art. 1 Abs. 1 Bst. f"


class ist_armee_angehoeriger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Angehöriger der Armee (Art. 1 Abs. 2 VG)"
    reference = "SR 170.32, Art. 1 Abs. 2"


class untersteht_verantwortlichkeitsgesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Untersteht dem Verantwortlichkeitsgesetz (Art. 1 VG)"
    reference = "SR 170.32, Art. 1"

    def formula(person, period, parameters):
        ist_bundesrat = person('ist_bundesratsmitglied', period)
        ist_gericht = person('ist_mitglied_eidg_gericht', period)
        ist_aufsicht = person('ist_mitglied_aufsichtsbehoerde_ba', period)
        ist_beamter = person('ist_beamter_bund', period)
        ist_betraut = person('ist_mit_oeffentlichen_aufgaben_betraut', period)
        ist_armee = person('ist_armee_angehoeriger', period)

        hat_bundesamt = ist_bundesrat + ist_gericht + ist_aufsicht + ist_beamter + ist_betraut
        return (hat_bundesamt > 0) * (1 - ist_armee)
