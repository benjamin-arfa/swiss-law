"""SR 961.01 Art. 30a-30f — Preneurs d'assurance professionnels / Professionelle Versicherungsnehmer

Generated from: ch/961/fr/961.01.md

LSA — Professional policyholders regime:
- Art. 30a: Insurers exclusively insuring professional policyholders get relief from
  Art. 10 (org fund), Art. 17-20 (tied assets), Art. 52e al. 2, Art. 54abis
- Art. 30a al. 4: Relief does NOT apply if professional policyholder activity
  generates claims under mandatory insurance for non-professional policyholders;
  tied assets always required for occupational pension risks
- Art. 30b: Clarification and documentation obligation before concluding contract
- Art. 30c: Information obligation about professional status and legal effects
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class assure_exclusivement_preneurs_professionnels(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Assure exclusivement des preneurs d'assurance professionnels"
    reference = "SR 961.01 Art. 30a al. 1"


class genere_pretentions_assurance_obligatoire_non_prof(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'activité génère des prétentions d'assurances obligatoires pour des non-professionnels"
    reference = "SR 961.01 Art. 30a al. 4"


class assure_risques_prevoyance_professionnelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Assure des risques en matière de prévoyance professionnelle"
    reference = "SR 961.01 Art. 30a al. 4"


class allegement_fonds_organisation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Libéré de l'obligation du fonds d'organisation (Art. 10)"
    reference = "SR 961.01 Art. 30a al. 1"

    def formula(person, period, parameters):
        return person('assure_exclusivement_preneurs_professionnels', period)


class allegement_fortune_liee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Libéré de l'obligation de fortune liée (Art. 17-20)"
    reference = "SR 961.01 Art. 30a al. 1 et 4"

    def formula(person, period, parameters):
        prof_seuls = person('assure_exclusivement_preneurs_professionnels', period)
        oblig_non_prof = person('genere_pretentions_assurance_obligatoire_non_prof', period)
        prevoyance = person('assure_risques_prevoyance_professionnelle', period)
        # Relief available only if no mandatory insurance claims for non-professionals
        # and not insuring occupational pension risks
        return prof_seuls * (1 - oblig_non_prof) * (1 - prevoyance)
