"""SR 744.21 Art. 4

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class recht_personenbefoerderung_erteilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Recht zur regelmässigen und gewerbsmässigen Beförderung von Reisenden erteilt (SR 744.21 Art. 4)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1986/1974_1974_1974/de#art_4"

    def formula(person, period, parameters):
        # The right to regularly and commercially transport passengers
        # is granted pursuant to Art. 6–8 of the Personenbeförderungsgesetz
        # (SR 745.1) of 20 March 2009. This variable captures whether
        # such a concession/authorisation has been granted.
        return person('konzession_personenbefoerderung_beantragt', period) * \
               person('konzession_personenbefoerderung_bewilligt', period)


class konzession_personenbefoerderung_beantragt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konzession oder Bewilligung zur Personenbeförderung beantragt (SR 745.1 Art. 6–8)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1986/1974_1974_1974/de#art_4"


class konzession_personenbefoerderung_bewilligt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Konzession oder Bewilligung zur Personenbeförderung durch Behörde erteilt (SR 745.1 Art. 6–8)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1986/1974_1974_1974/de#art_4"
