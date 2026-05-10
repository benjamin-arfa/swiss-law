"""SR 314.1 Art. 1

Generated from: ch/314/de/314.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uebertretung_in_obg_gesetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Uebertretung ist in einem der Gesetze nach Art. 1 Abs. 1 Bst. a aufgefuehrt"
    reference = "SR 314.1 Art. 1 Abs. 1 Bst. a"


class uebertretung_in_bussenliste(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Uebertretungstatbestand ist in den Listen nach Art. 15 aufgefuehrt"
    reference = "SR 314.1 Art. 1 Abs. 2"


class verwaltungsstrafrecht_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Uebertretung wird nach dem Verwaltungsstrafrecht verfolgt"
    reference = "SR 314.1 Art. 1 Abs. 3"


class ordnungsbussenverfahren_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Ordnungsbussenverfahren ist anwendbar"
    reference = "SR 314.1 Art. 1 Abs. 1-3"

    def formula(person, period, parameters):
        in_gesetz = person('uebertretung_in_obg_gesetz', period)
        in_liste = person('uebertretung_in_bussenliste', period)
        verwaltungsstrafrecht = person('verwaltungsstrafrecht_anwendbar', period)
        return in_gesetz * in_liste * not_(verwaltungsstrafrecht)


class ordnungsbusse_hoechstbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbetrag der Ordnungsbusse (300 Franken)"
    reference = "SR 314.1 Art. 1 Abs. 4"
    default_value = 300.0
