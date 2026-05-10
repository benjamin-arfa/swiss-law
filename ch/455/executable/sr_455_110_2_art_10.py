"""SR 455.110.2 Art. 10

Generated from: ch/455/de/455.110.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class richtungswechsel_grad(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kleinster Richtungswechsel im Treibgang in Grad"
    reference = "SR 455.110.2 Art. 10 Abs. 3 lit. d"


class kurvenradius_meter(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kleinster Kurvenradius im Treibgang in Metern"
    reference = "SR 455.110.2 Art. 10 Abs. 3 lit. e"


class einzeltreibgang_lichte_hoehe_cm(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Lichte Hoehe des Einzeltreibgangs fuer Rinder in cm"
    reference = "SR 455.110.2 Art. 10 Abs. 6"


class widerristhoehe_rind_cm(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Widerristhoehe des Rindes in cm"
    reference = "SR 455.110.2 Art. 10 Abs. 6"


class treibgang_richtungswechsel_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Richtungswechsel im Treibgang konform (min 100 Grad) nach Art. 10 Abs. 3 lit. d SR 455.110.2"
    reference = "SR 455.110.2 Art. 10 Abs. 3 lit. d"

    def formula(person, period, parameters):
        return person('richtungswechsel_grad', period) >= 100


class treibgang_kurvenradius_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kurvenradius im Treibgang konform (min 3 m) nach Art. 10 Abs. 3 lit. e SR 455.110.2"
    reference = "SR 455.110.2 Art. 10 Abs. 3 lit. e"

    def formula(person, period, parameters):
        return person('kurvenradius_meter', period) >= 3.0


class einzeltreibgang_hoehe_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Lichte Hoehe des Einzeltreibgangs fuer Rinder konform (min Widerristhoehe + 20cm) nach Art. 10 Abs. 6 SR 455.110.2"
    reference = "SR 455.110.2 Art. 10 Abs. 6"

    def formula(person, period, parameters):
        hoehe = person('einzeltreibgang_lichte_hoehe_cm', period)
        widerrist = person('widerristhoehe_rind_cm', period)
        return hoehe >= (widerrist + 20)
