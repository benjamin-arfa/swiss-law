"""SR 453.1 Art. 5

Generated from: ch/453/de/453.1.md
Etikettierung von Kaviar, Registrierungspflicht.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class produziert_kaviar_gewerbsmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person produziert oder verpackt gewerbsmaessig Kaviar"
    reference = "SR 453.1 Art. 5 Abs. 3"


class ist_beim_blv_registriert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist beim BLV registriert"
    reference = "SR 453.1 Art. 5 Abs. 3"


class registrierungspflicht_kaviar_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Registrierungspflicht fuer Kaviarproduzenten/-umverpacker erfuellt"
    reference = "SR 453.1 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        produziert = person('produziert_kaviar_gewerbsmaessig', period)
        registriert = person('ist_beim_blv_registriert', period)
        return where(produziert, registriert, True)
