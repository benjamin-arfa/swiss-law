"""SR 654.1 Art. 5 - Monnaie de la declaration pays par pays

Generated from: ch/654/de/654.1.md

The country-by-country report must contain the financial data in the
national currency or in the currency that is material for the business
activity of the multinational group.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class monnaie_declaration_pays(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Monnaie utilisee dans la declaration pays par pays"
    reference = "SR 654.1 Art. 5"


class monnaie_declaration_pays_valide(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La monnaie est la monnaie nationale ou une monnaie essentielle pour l'activite du groupe"
    reference = "SR 654.1 Art. 5"
