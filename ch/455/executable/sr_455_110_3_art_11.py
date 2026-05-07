"""SR 455.110.3 Art. 11

Generated from: ch/455/de/455.110.3.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class laufvogel_alter_wochen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter des Laufvogels in Wochen"
    reference = "SR 455.110.3 Art. 11"


class laufvogel_hat_weidezugang(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Laufvogel hat permanenten Zugang zu Weideflaechen"
    reference = "SR 455.110.3 Art. 11"


class laufvogel_weidezugang_pflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Laufvogel hat Pflicht zum ganzjaehrig permanenten Weidezugang (ab 9. Lebenswoche) nach Art. 11 SR 455.110.3"
    reference = "SR 455.110.3 Art. 11"

    def formula(person, period, parameters):
        alter = person('laufvogel_alter_wochen', period)
        return alter >= 9
