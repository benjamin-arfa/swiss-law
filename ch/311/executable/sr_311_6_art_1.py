"""SR 311.6 Art. 1

Generated from: ch/311/de/311.6.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ort_ist_oeffentlich_zugaenglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befindet sich die Person an einem oeffentlich oder privat zugaenglichen Ort"
    reference = "SR 311.6 Art. 1"


class an_bord_ziviles_luftfahrzeug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befindet sich die Person an Bord eines zivilen Luftfahrzeugs"
    reference = "SR 311.6 Art. 1 Abs. 2 lit. a"


class in_diplomatischen_raeumlichkeiten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Befindet sich die Person in diplomatischen oder konsularischen Raeumlichkeiten"
    reference = "SR 311.6 Art. 1 Abs. 2 lit. b"


class bvvg_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Bundesgesetz ueber das Verbot der Verhuelllung des Gesichts anwendbar"
    reference = "SR 311.6 Art. 1"

    def formula(person, period, parameters):
        oeffentlich = person('ort_ist_oeffentlich_zugaenglich', period)
        luftfahrzeug = person('an_bord_ziviles_luftfahrzeug', period)
        diplomatisch = person('in_diplomatischen_raeumlichkeiten', period)
        return oeffentlich * not_(luftfahrzeug) * not_(diplomatisch)
