"""SR 654.1 Art. 8 - Obligation d'une autre entite constitutive residente de Suisse

Generated from: ch/654/fr/654.1.md

The FTA may require another Swiss-resident constituent entity to
provide the CbC report in certain circumstances.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class societe_mere_dans_etat_non_partenaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La societe mere a sa residence fiscale dans un Etat non partenaire"
    reference = "SR 654.1 Art. 8 al. 1 let. a"


class defaillance_systemique_etat_partenaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'Etat partenaire de la societe mere presente une defaillance systemique"
    reference = "SR 654.1 Art. 8 al. 1 let. b"


class societe_mere_substitution_a_fourni(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La societe mere de substitution a fourni la declaration a un Etat partenaire"
    reference = "SR 654.1 Art. 8 al. 2"


class entite_constitutive_residente_suisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite est une entite constitutive residente de Suisse"
    reference = "SR 654.1 Art. 8 al. 1"


class obligation_autre_entite_fournir_declaration(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC peut prescrire a une autre entite constitutive de fournir la declaration"
    reference = "SR 654.1 Art. 8 al. 1"

    def formula(self, period, parameters):
        residente = self('entite_constitutive_residente_suisse', period)
        obligation_groupe = self('obligation_declaration_pays_par_pays', period)
        non_partenaire = self('societe_mere_dans_etat_non_partenaire', period)
        defaillance = self('defaillance_systemique_etat_partenaire', period)
        substitution = self('societe_mere_substitution_a_fourni', period)

        # al. 1: if parent state is not a partner or has systemic failure
        condition_al1 = residente * obligation_groupe * (non_partenaire + defaillance > 0)
        # al. 2: exception if surrogate parent has already filed
        return condition_al1 * not_(substitution)
