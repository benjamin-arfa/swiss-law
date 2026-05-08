"""SR 821.41 Art. 34

Generated from: ch/821/de/821.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class schiedsspruch_befugnis_uebertragen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Parteien haben der Einigungsstelle die Befugnis uebertragen, "
        "verbindliche Schiedsprueche zu faellen"
    )
    reference = "SR 821.41 Art. 34"
