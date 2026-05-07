"""SR 451.13 Art. 3

Generated from: ch/451/de/451.13.md
Bundesinventar historischer Verkehrswege - zwei Klassierungen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class verkehrsweg_klassierung(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Klassierung des historischen Verkehrswegs (viel_substanz, substanz)"
    reference = "SR 451.13 Art. 3 Abs. 4"
    default_value = "substanz"


class verkehrsweg_national_bedeutung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Historischer Verkehrsweg ist von nationaler Bedeutung"
    reference = "SR 451.13 Art. 2 Abs. 2"
