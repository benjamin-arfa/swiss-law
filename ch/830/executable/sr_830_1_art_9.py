"""SR 830.1 Art. 9

Generated from: ch/830/de/830.1.md

Art. 9: Hilflosigkeit - A person is considered helpless if they permanently
need the help of others or personal supervision for everyday activities
due to health impairment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class benoetigt_hilfe_dritter_fuer_alltag(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Person bedarf wegen Gesundheitsbeeinträchtigung für alltägliche "
        "Lebensverrichtungen dauernd der Hilfe Dritter"
    )
    reference = "SR 830.1 Art. 9"


class benoetigt_persoenliche_ueberwachung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Person bedarf wegen Gesundheitsbeeinträchtigung für alltägliche "
        "Lebensverrichtungen dauernd der persönlichen Überwachung"
    )
    reference = "SR 830.1 Art. 9"


class ist_hilflos(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist hilflos im Sinne von Art. 9 ATSG"
    reference = "SR 830.1 Art. 9"

    def formula(person, period, parameters):
        hilfe = person('benoetigt_hilfe_dritter_fuer_alltag', period)
        ueberwachung = person('benoetigt_persoenliche_ueberwachung', period)
        return hilfe + ueberwachung > 0
