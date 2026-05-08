"""SR 821.41 Art. 30

Generated from: ch/821/de/821.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class kantonale_einigungsstelle_errichtet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Kanton hat staendige Einigungsstelle zur Vermittlung von "
        "Kollektivstreitigkeiten zwischen Fabrikinhabern und Arbeitern errichtet"
    )
    reference = "SR 821.41 Art. 30 Abs. 1"
