"""SR 0.101.06 Art. 4

Generated from: ch/0/de/0.101.06.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class HasReservation(Variable):
    value_type = bool
    entity = person
    definition_period = ETD
    label = u"Whether the person has a reservation that refers to an article not allowed under Article 4 of the Convention."

    def formula(person, period, parameters):
        return person('has_reservation', period)

class HasNoReservation(Variable):
    value_type = bool
    entity = person
    definition_period = ETD
    label = u"Whether the person does not have a reservation that refers to an article not allowed under Article 4 of the Convention."

    def formula(person, period, parameters):
        return ~person('has_reservation', period)

class HasReservationDenied(Variable):
    value_type = bool
    entity = person
    definition_period = ETD
    label = u"Whether the person has a reservation that refers to an article not allowed under Article 4 of the Convention."

    def formula(person, period, parameters):
        reserved_articles = person('has_reserved_article', period)
        return person('reservation_denied_articles', period).apply(on_ = reserved_articles)
