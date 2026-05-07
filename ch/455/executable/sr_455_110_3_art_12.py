"""SR 455.110.3 Art. 12

Generated from: ch/455/de/455.110.3.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_strauss(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist ein Strauss"
    reference = "SR 455.110.3 Art. 12 Abs. 4"


class sandbad_flaeche_m2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Flaeche des Sandbades in m2"
    reference = "SR 455.110.3 Art. 12 Abs. 4"


class sandbad_tiefe_m(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Tiefe des Sandbades in Metern"
    reference = "SR 455.110.3 Art. 12 Abs. 4"


class strauss_sandbad_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sandbad fuer Strausse konform (min 6.25 m2, min 0.2 m tief) nach Art. 12 Abs. 4 SR 455.110.3"
    reference = "SR 455.110.3 Art. 12 Abs. 4"

    def formula(person, period, parameters):
        ist_str = person('ist_strauss', period)
        flaeche = person('sandbad_flaeche_m2', period)
        tiefe = person('sandbad_tiefe_m', period)
        return where(ist_str, (flaeche >= 6.25) * (tiefe >= 0.2), True)
