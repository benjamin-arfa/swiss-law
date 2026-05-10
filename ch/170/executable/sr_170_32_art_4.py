"""SR 170.32 Art. 4

Generated from: ch/170/de/170.32.md

Ermässigung oder Entbindung von der Ersatzpflicht bei Einwilligung oder
Mitverschulden des Geschädigten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class geschaedigter_hat_eingewilligt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Geschädigte hat in die schädigende Handlung eingewilligt (Art. 4 VG)"
    reference = "SR 170.32, Art. 4"


class geschaedigter_hat_mitverschulden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Umstände des Geschädigten haben zur Entstehung oder Verschlimmerung des Schadens beigetragen (Art. 4 VG)"
    reference = "SR 170.32, Art. 4"


class ersatzpflicht_kann_ermaessigt_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Ersatzpflicht kann ermässigt oder gänzlich aufgehoben werden (Art. 4 VG)"
    reference = "SR 170.32, Art. 4"

    def formula(person, period, parameters):
        eingewilligt = person('geschaedigter_hat_eingewilligt', period)
        mitverschulden = person('geschaedigter_hat_mitverschulden', period)
        return eingewilligt + mitverschulden > 0
