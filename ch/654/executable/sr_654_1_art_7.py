"""SR 654.1 Art. 7 - Obligation de l'entite declarante de fournir la declaration

Generated from: ch/654/fr/654.1.md

The reporting entity must provide the CbC report to the FTA.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class entite_declarante(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite est l'entite declarante (societe mere ou societe mere de substitution residente de Suisse)"
    reference = "SR 654.1 Art. 7"


class obligation_fournir_declaration_afc(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite declarante est tenue de fournir la declaration pays par pays a l'AFC"
    reference = "SR 654.1 Art. 7"

    def formula(self, period, parameters):
        declarante = self('entite_declarante', period)
        obligation = self('obligation_declaration_pays_par_pays', period)
        return declarante * obligation
