"""SR 740.1 Art. 1 - Zweck

Generated from: ch/740/de/740.1.md

Zum Schutz des Alpengebietes soll der alpenquerende Gueterschwer-
verkehr auf nachhaltige Weise von der Strasse auf die Schiene
verlagert werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class alpenquerender_gueterschwerkehr_verlagert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der alpenquerende Gueterschwerkehr wird von der Strasse auf die Schiene verlagert"
    reference = "SR 740.1 Art. 1 Abs. 1"


class oekologisch_ausgewogenes_verhaeltnis_verkehrstraeger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Oekologisch ausgewogenes und wirtschaftlich angemessenes Verhaeltnis zwischen den Verkehrstraegern"
    reference = "SR 740.1 Art. 1 Abs. 2"
