"""SR 121.3 Art. 1

Generated from: ch/121/de/121.3.md

Gegenstand: This ordinance regulates the administrative assignment of AB-ND,
organization of UKI, cooperation between federal and cantonal oversight bodies,
minimum requirements for cantonal oversight, and cooperation among oversight bodies.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vand_regelt_ab_nd_zuordnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die VAND die administrative Zuordnung der AB-ND regelt"
    reference = "SR 121.3 Art. 1 Bst. a"


class vand_regelt_verwaltungsablaeufe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die VAND die relevanten Verwaltungsablaeufe regelt"
    reference = "SR 121.3 Art. 1 Bst. a"


class vand_regelt_uki_organisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die VAND die Organisation und Aufgabe der UKI regelt"
    reference = "SR 121.3 Art. 1 Bst. b"


class vand_regelt_zusammenarbeit_bund_kantone(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die VAND die Zusammenarbeit zwischen Bund und kantonalen Dienstaufsichtsorganen regelt"
    reference = "SR 121.3 Art. 1 Bst. c"


class vand_regelt_mindestanforderungen_kantone(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die VAND die Mindestanforderungen an die Aufsicht in den Kantonen regelt"
    reference = "SR 121.3 Art. 1 Bst. d"


class vand_regelt_zusammenarbeit_aufsichtsorgane(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die VAND die Zusammenarbeit der Aufsichtsorgane regelt"
    reference = "SR 121.3 Art. 1 Bst. e"


class verordnung_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die VAND auf die nachrichtendienstlichen Taetigkeiten anwendbar ist"
    reference = "SR 121.3 Art. 1"

    def formula(person, period, parameters):
        return True  # This ordinance applies to all regulated matters