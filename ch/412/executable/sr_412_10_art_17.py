"""SR 412.10 Art. 17

Generated from: ch/412/de/412.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class art_der_grundbildung(Variable):
    """Art der beruflichen Grundbildung: 'zweij' or 'drei_vierj'"""
    value_type = str
    max_length = 20
    entity = Person
    definition_period = YEAR
    label = "Art der beruflichen Grundbildung (zweij oder drei_vierj)"
    reference = "SR 412.10 Art. 17"


class dauer_grundbildung_jahre(Variable):
    """Dauer der beruflichen Grundbildung in Jahren (2-4)"""
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der beruflichen Grundbildung in Jahren"
    reference = "SR 412.10 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        # Input: actual specified duration; must be between 2 and 4
        return person('dauer_grundbildung_jahre_eingabe', period)


class dauer_grundbildung_jahre_eingabe(Variable):
    """Vorgesehene Dauer der Grundbildung (Eingabe, 2-4 Jahre)"""
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Vorgesehene Dauer der Grundbildung in Jahren"
    reference = "SR 412.10 Art. 17 Abs. 1"
    default_value = 3


class fuehrt_zu_berufsattest(Variable):
    """Ob die Grundbildung zum eidg. Berufsattest fuehrt (2-jaehrig)"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuehrt zum eidgenoessischen Berufsattest"
    reference = "SR 412.10 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        dauer = person('dauer_grundbildung_jahre_eingabe', period)
        return dauer == 2


class fuehrt_zu_faehigkeitszeugnis(Variable):
    """Ob die Grundbildung zum eidg. Faehigkeitszeugnis fuehrt (3-4 jaehrig)"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuehrt zum eidgenoessischen Faehigkeitszeugnis"
    reference = "SR 412.10 Art. 17 Abs. 3"

    def formula(person, period, parameters):
        dauer = person('dauer_grundbildung_jahre_eingabe', period)
        return (dauer >= 3) * (dauer <= 4)


class berechtigt_berufsmaturitaet(Variable):
    """Ob Zugang zur Berufsmaturitaet besteht (EFZ + erweiterte Allgemeinbildung)"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berechtigung zur Berufsmaturitaet"
    reference = "SR 412.10 Art. 17 Abs. 4"

    def formula(person, period, parameters):
        hat_efz = person('fuehrt_zu_faehigkeitszeugnis', period)
        erweiterte_allgemeinbildung = person('hat_erweiterte_allgemeinbildung', period)
        return hat_efz * erweiterte_allgemeinbildung


class hat_erweiterte_allgemeinbildung(Variable):
    """Ob die Person erweiterte Allgemeinbildung abgeschlossen hat"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat erweiterte Allgemeinbildung abgeschlossen"
    reference = "SR 412.10 Art. 17 Abs. 4"
    default_value = False
