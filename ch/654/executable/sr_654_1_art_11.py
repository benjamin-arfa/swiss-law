"""SR 654.1 Art. 11 - Delai pour fournir la declaration pays par pays

Generated from: ch/654/fr/654.1.md

Deadline: 12 months after the last day of the reportable fiscal period.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class delai_declaration_mois(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Delai pour fournir la declaration pays par pays (en mois apres fin de la periode fiscale)"
    reference = "SR 654.1 Art. 11 al. 1"
    default_value = 12
