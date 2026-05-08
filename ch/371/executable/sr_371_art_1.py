"""SR 371 Art. 1 - Gegenstand und Zweck (Subject and Purpose)

Generated from: ch/de/371.md
This act governs the annulment of criminal convictions against persons who helped
persecuted people flee during the Nazi era, and their rehabilitation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class ist_fluechtlingshelfer_ns_zeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat verfolgten Menschen zur Zeit des Nationalsozialismus zur Flucht verholfen"
    reference = "SR 371 Art. 1 Abs. 1"
    default_value = False
