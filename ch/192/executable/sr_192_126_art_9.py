"""SR 192.126 Art. 9

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hausangestellte_alter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der/des privaten Hausangestellten"
    reference = "SR 192.126 Art. 9"

class ist_familienangehoeriger_arbeitgeber(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Familienangehoeriger der Arbeitgeberin/des Arbeitgebers"
    reference = "SR 192.126 Art. 9"

class hat_gueltigen_pass(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person besitzt einen gueltigen Nationalpass"
    reference = "SR 192.126 Art. 9"

class arbeitet_vollzeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person arbeitet Vollzeit"
    reference = "SR 192.126 Art. 9"

class lebt_im_haushalt_arbeitgeber(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person lebt und arbeitet im Haushalt der Arbeitgeberin/des Arbeitgebers"
    reference = "SR 192.126 Art. 9"

class erfuellt_allgemeine_voraussetzungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfuellt allgemeine Voraussetzungen fuer private Hausangestellte (Art. 9 Abs. 1)"
    reference = "SR 192.126 Art. 9"

    def formula(person, period, parameters):
        alter = person('hausangestellte_alter', period)
        nicht_familie = 1 - person('ist_familienangehoeriger_arbeitgeber', period)
        hat_pass = person('hat_gueltigen_pass', period)
        vollzeit = person('arbeitet_vollzeit', period)
        im_haushalt = person('lebt_im_haushalt_arbeitgeber', period)
        return (alter >= 18) * nicht_familie * hat_pass * vollzeit * im_haushalt
