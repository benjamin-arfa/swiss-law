"""SR 852.12 Art. 13

Generated from: ch/852/fr/852.12.md

Art. 13: Data destruction timelines for EDAssist+:
- al. 1: Social aid module data destroyed 10 years after last processing,
  but at most 30 years after dossier opening.
- al. 2: Hotline, helpline, and consular protection data with status
  deactivated/terminated/archived destroyed at most 5 years after
  last consultation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class edassist_module_aide_sociale(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the data belongs to the social aid module"
    reference = "SR 852.12 Art. 13 al. 1"


class edassist_annees_depuis_dernier_traitement(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Years since the last data processing"
    reference = "SR 852.12 Art. 13"


class edassist_annees_depuis_ouverture_dossier(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Years since dossier opening"
    reference = "SR 852.12 Art. 13 al. 1"


class edassist_statut_desactive_termine_archive(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the record status is deactivated, terminated, or archived"
    reference = "SR 852.12 Art. 13 al. 2"


class edassist_annees_depuis_derniere_consultation(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Years since the last data consultation"
    reference = "SR 852.12 Art. 13 al. 2"


class edassist_donnees_a_detruire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the EDAssist+ data must be destroyed"
    reference = "SR 852.12 Art. 13"

    def formula(person, period, parameters):
        p = parameters(period).sr_852_12
        est_aide_sociale = person('edassist_module_aide_sociale', period)
        ans_traitement = person('edassist_annees_depuis_dernier_traitement', period)
        ans_dossier = person('edassist_annees_depuis_ouverture_dossier', period)
        statut_inactif = person('edassist_statut_desactive_termine_archive', period)
        ans_consultation = person('edassist_annees_depuis_derniere_consultation', period)

        # al. 1: aide sociale - 10 years after last processing OR 30 years after opening
        destruction_aide = est_aide_sociale * (
            (ans_traitement >= p.delai_destruction_aide_sociale_traitement) +
            (ans_dossier >= p.delai_destruction_aide_sociale_dossier)
        ) > 0

        # al. 2: hotline/helpline/protection - 5 years after last consultation if inactive
        destruction_autres = (1 - est_aide_sociale) * statut_inactif * (
            ans_consultation >= p.delai_destruction_autres_modules
        )

        return (destruction_aide + destruction_autres) > 0
