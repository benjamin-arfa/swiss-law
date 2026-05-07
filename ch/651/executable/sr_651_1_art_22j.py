"""SR 651.1 Art. 22j - Infractions a des injonctions officielles

Generated from: ch/651/fr/651.1.md

Penalty for intentional non-compliance with an enforceable decision
regarding the provision of information: fine up to CHF 10,000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class non_conformite_intentionnelle_decision_art_9_10(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La personne ne s'est intentionnellement pas conformee a une decision sur la remise de renseignements (art. 9 ou 10)"
    reference = "SR 651.1 Art. 22j"


class amende_infraction_injonction_officielle(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amende pour infraction a des injonctions officielles (CHF, max 10'000)"
    reference = "SR 651.1 Art. 22j"
    default_value = 0.0


class amende_maximale_injonction_officielle(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amende maximale pour infraction a des injonctions officielles (CHF)"
    reference = "SR 651.1 Art. 22j"
    default_value = 10_000.0
