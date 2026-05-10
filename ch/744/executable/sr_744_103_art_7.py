"""SR 744.103 Art. 7

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pruefung_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat die Prüfung für den Fachausweis bestanden"
    reference = "SR 744.103 Art. 7 Abs. 1"


class fachausweis_bei_bav_gemeldet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Prüfungsträgerschaft hat die Person dem BAV gemeldet (Name, Geburtsdatum, Bürgerort, Adresse)"
    reference = "SR 744.103 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        return person('pruefung_bestanden', period)


class fachausweis_ausgestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV hat den Fachausweis ausgestellt"
    reference = "SR 744.103 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        return person('fachausweis_bei_bav_gemeldet', period)


class fachausweis_rechtswidrig_erworben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fachausweis wurde auf rechtswidrige Weise erworben"
    reference = "SR 744.103 Art. 7 Abs. 3"


class fachausweis_entzogen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV hat den Fachausweis entzogen"
    reference = "SR 744.103 Art. 7 Abs. 3"

    def formula(person, period, parameters):
        return person('fachausweis_rechtswidrig_erworben', period)


class fachausweis_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fachausweis ist gültig (ausgestellt und nicht entzogen)"
    reference = "SR 744.103 Art. 7 Abs. 2-3"

    def formula(person, period, parameters):
        ausgestellt = person('fachausweis_ausgestellt', period)
        entzogen = person('fachausweis_entzogen', period)
        return ausgestellt * not_(entzogen)


class fachausweis_im_register(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist im öffentlichen BAV-Register der Fachausweisinhaber eingetragen"
    reference = "SR 744.103 Art. 7 Abs. 4"

    def formula(person, period, parameters):
        return person('fachausweis_gueltig', period)
