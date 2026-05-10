"""SR 523.51 Art. 15

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class diplom_hauptberuflich_erhalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat das Diplom fuer hauptberufliches Zivilschutzlehrpersonal erhalten"
    reference = "SR 523.51 Art. 15 Abs. 2"


class berechtigung_titel_zivilschutzinstruktor(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist berechtigt den Titel 'Eidgenoessisch diplomierter Zivilschutzinstruktor' zu fuehren"
    reference = "SR 523.51 Art. 15 Abs. 2"

    def formula(person, period, parameters):
        return person('diplom_hauptberuflich_erhalten', period)
