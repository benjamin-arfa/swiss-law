"""SR 832.312.15 Art. 16 – Anerkennung als Kranexpertin/-experte

Generated from: ch/832/de/832.312.15.md

Voraussetzungen:
a) Eidg. Fachausweis für Instandhaltungsfachleute oder gleichwertig
b) Mindestens 5 Jahre Berufserfahrung in Montage/Demontage/Instandhaltung
c) Erfahrung in Elektrotechnik und Steuerungstechnik
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

MIN_BERUFSERFAHRUNG_JAHRE = 5


class hat_fachausweis_instandhaltung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besitzt eidg. Fachausweis für Instandhaltungsfachleute oder gleichwertig"
    reference = "SR 832.312.15 Art. 16 Abs. 1 lit. a"


class berufserfahrung_kranbau_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahre Berufserfahrung in Montage/Demontage/Instandhaltung von Kranen"
    reference = "SR 832.312.15 Art. 16 Abs. 1 lit. b"


class erfahrung_elektrotechnik_steuerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfahrung in Elektrotechnik und Steuerungstechnik im Kranbau"
    reference = "SR 832.312.15 Art. 16 Abs. 1 lit. c"


class anspruch_anerkennung_kranexperte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfüllt Voraussetzungen für Anerkennung als Kranexpertin/-experte"
    reference = "SR 832.312.15 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        fachausweis = person('hat_fachausweis_instandhaltung', period)
        erfahrung = person('berufserfahrung_kranbau_jahre', period)
        elektro = person('erfahrung_elektrotechnik_steuerung', period)

        return fachausweis * (erfahrung >= MIN_BERUFSERFAHRUNG_JAHRE) * elektro
