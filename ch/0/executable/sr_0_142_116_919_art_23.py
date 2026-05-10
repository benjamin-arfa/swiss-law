"""SR 0.142.116.919 Art. 23

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class belongs_to_liechtenstein_not_switzerland(Variable):
    value_type = bool
    entity = Person, Residency
    definition_period = DAY
    label = "Person living in Liechtenstein, not Switzerland (Art. 23, SR 0.142.116.919)"
    reference = "https://www.admin.ch/opc/fr/classified-compilation/20021393/index.html#art_23"

    def formula(person, period, parameters):
        person_residency = person('main_residence', period)
        in_liechtenstein = person_residency == Residency.LIECHTENSTEIN
        is_liechtenstein_citizen = person('nationality', period) == 'Liechtenstein'
        not_switzerland = person_residency != Residency.SWITZERLAND
        return (in_liechtenstein | is_liechtenstein_citizen) & not_switzerland
