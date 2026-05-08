"""SR 124 Art. 7 - Ausruestung des Personals in der Schweiz (Equipment in Switzerland)

Generated from: ch/de/124.md
Whether personnel carry weapons for self-defense/emergency is set by contract.
Required permits must be held. Self-defense provisions are reserved.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class sicherheitspersonal_bewaffnet_inland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitspersonal ist fuer Notwehr/Notstand in der Schweiz bewaffnet (vertraglich festgelegt)"
    reference = "SR 124 Art. 7 Abs. 1"
    default_value = False


class sicherheitspersonal_hat_bewilligungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitspersonal verfuegt ueber erforderliche Bewilligungen"
    reference = "SR 124 Art. 7 Abs. 2"
    default_value = False
