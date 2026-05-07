"""SR 513.72 Art. 2

Generated from: ch/513/de/513.72.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_rekrutenformation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Formation ist eine Rekrutenformation"


class ist_fuer_aufgabe_ausgebildet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Truppe ist fuer die Aufgabe ausgebildet"


class hat_zweckmaessige_ausruestung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Truppe verfuegt ueber zweckmaessige Ausruestung"


class grenzpolizeidienst_einsatz_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Truppeneinsatz fuer Grenzpolizeidienst zulaessig (Art. 2 Abs. 2-3 SR 513.72)"
    reference = "SR 513.72 Art. 2"

    def formula(person, period, parameters):
        # Abs. 2: nur fuer Aufgaben einsetzen, fuer die ausgebildet + ausgeruestet
        # Abs. 3: Rekrutenformationen duerfen NICHT eingesetzt werden
        ausgebildet = person('ist_fuer_aufgabe_ausgebildet', period)
        ausgeruestet = person('hat_zweckmaessige_ausruestung', period)
        rekruten = person('ist_rekrutenformation', period)
        return ausgebildet * ausgeruestet * (rekruten == False)
