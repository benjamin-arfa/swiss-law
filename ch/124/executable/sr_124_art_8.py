"""SR 124 Art. 8 - Ausruestung des Personals im Ausland (Equipment Abroad)

Generated from: ch/de/124.md
Personnel abroad is generally unarmed.
Weapons only exceptionally if the situation requires it.
Local weapons legislation applies.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class sicherheitspersonal_bewaffnet_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitspersonal ist im Ausland ausnahmsweise bewaffnet"
    reference = "SR 124 Art. 8 Abs. 2"
    default_value = False
