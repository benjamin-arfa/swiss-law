"""SR 455.110.3 Art. 9

Generated from: ch/455/de/455.110.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hirschgehege_zaunhoehe_m(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoehe des Aussenzauns des Hirschgeheges in Metern"
    reference = "SR 455.110.3 Art. 9 Abs. 1"


class hirschgehege_zaun_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aussenzaun des Hirschgeheges konform (min 2 m) nach Art. 9 Abs. 1 SR 455.110.3"
    reference = "SR 455.110.3 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return person('hirschgehege_zaunhoehe_m', period) >= 2.0
