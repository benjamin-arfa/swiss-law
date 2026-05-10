"""SR 432.219 Art. 3

Generated from: ch/432/de/432.219.md

Gebuehrenermässigung und Gebuehrenerlass - drei Gruende fuer Ermaessigung oder Erlass.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dienstleistung_wenig_aufwand(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung erfordert wenig Aufwand"
    reference = "SR 432.219 Art. 3 Bst. a"


class gebuehrenpflichtige_wenig_bemittelt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Gebuehrenpflichtige Person ist wenig bemittelt"
    reference = "SR 432.219 Art. 3 Bst. b"


class dienstleistung_im_oeffentlichen_interesse(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Dienstleistung wird vorwiegend im oeffentlichen Interesse erbracht"
    reference = "SR 432.219 Art. 3 Bst. c"


class gebuehrenreduktion_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Gebuehr kann ermaessigt oder erlassen werden"
    reference = "SR 432.219 Art. 3"

    def formula(person, period, parameters):
        return (
            person('dienstleistung_wenig_aufwand', period) +
            person('gebuehrenpflichtige_wenig_bemittelt', period) +
            person('dienstleistung_im_oeffentlichen_interesse', period)
        ) > 0
