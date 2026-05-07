"""SR 654.1 Art. 26 - Insoumission a une decision de l'autorite

Generated from: ch/654/fr/654.1.md

Penalty for intentional non-compliance with a decision during
a control (Art. 22): fine up to CHF 10,000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class insoumission_intentionnelle_decision(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite a omis intentionnellement de se conformer a une decision dans le cadre d'un controle"
    reference = "SR 654.1 Art. 26"


class amende_insoumission_decision(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amende pour insoumission a une decision de l'autorite (CHF, max 10'000)"
    reference = "SR 654.1 Art. 26"
    default_value = 0.0


class amende_maximale_insoumission(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amende maximale pour insoumission (CHF)"
    reference = "SR 654.1 Art. 26"
    default_value = 10_000.0
