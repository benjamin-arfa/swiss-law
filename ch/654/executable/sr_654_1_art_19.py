"""SR 654.1 Art. 19 - Obligation de renseigner

Generated from: ch/654/de/654.1.md

Reporting entities must provide the ESTV with information on all facts
relevant to the implementation of the agreement and this law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class obligation_renseigner_afc(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite declarante est tenue de fournir des renseignements a l'AFC sur demande"
    reference = "SR 654.1 Art. 19"

    def formula(self, period, parameters):
        est_declarant = self('est_entite_declarante', period)
        return est_declarant


class est_entite_declarante(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite est une entite declarante au sens de la loi"
    reference = "SR 654.1 Art. 2 let. i"
