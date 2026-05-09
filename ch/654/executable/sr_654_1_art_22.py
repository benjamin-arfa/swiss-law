"""SR 654.1 Art. 22 - Verification

Generated from: ch/654/de/654.1.md

The ESTV verifies compliance with obligations under the agreement and
the law. It may set deadlines, request documents, and issue rulings.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class obligations_albag_completement_remplies(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite constitutive a rempli completement ses obligations selon l'accord et la loi"
    reference = "SR 654.1 Art. 22 al. 1"


class delai_correction_fixe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC a fixe un delai pour la correction des manquements"
    reference = "SR 654.1 Art. 22 al. 2"


class manquements_corriges_dans_delai(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite a corrige les manquements dans le delai imparti"
    reference = "SR 654.1 Art. 22 al. 3"


class afc_peut_exiger_documents(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC peut exiger la remise de documents ou les verifier sur place"
    reference = "SR 654.1 Art. 22 al. 3 let. a"

    def formula(self, period, parameters):
        delai_fixe = self('delai_correction_fixe', period)
        pas_corrige = not_(self('manquements_corriges_dans_delai', period))
        return delai_fixe * pas_corrige
