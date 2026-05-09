"""SR 431.011 Art. 1

Generated from: ch/431/de/431.011.md

Zweck - Regelt Anwendungsbereich, Mehrjahresprogramm, Zusammenarbeit und Diffusion.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class bundesstatistik_anwendungsbereich_geregelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anwendungsbereich des Bundesstatistikgesetzes ist geregelt"
    reference = "SR 431.011 Art. 1 Bst. a"
    default_value = True


class bundesstatistik_mehrjahresprogramm_geregelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erstellung des Mehrjahresprogramms ist geregelt"
    reference = "SR 431.011 Art. 1 Bst. b"
    default_value = True


class bundesstatistik_zusammenarbeit_geregelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zusammenarbeit der verschiedenen Stellen ist geregelt"
    reference = "SR 431.011 Art. 1 Bst. c"
    default_value = True


class bundesstatistik_diffusion_geregelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Diffusion der Statistik ist geregelt"
    reference = "SR 431.011 Art. 1 Bst. d"
    default_value = True
