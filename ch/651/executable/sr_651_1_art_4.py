"""SR 651.1 Art. 4 - Principes

Generated from: ch/651/fr/651.1.md

Principles: diligence, exclusion of information on non-concerned persons
unless relevant or unless legitimate interests prevail.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class personne_concernee_par_demande(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La personne est la personne concernee par la demande d'assistance administrative"
    reference = "SR 651.1 Art. 3 let. a"


class renseignements_vraisemblablement_pertinents(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Les renseignements sont vraisemblablement pertinents pour evaluer la situation fiscale"
    reference = "SR 651.1 Art. 4 al. 3"


class interets_legitimes_prevalent(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Les interets legitimes des personnes non concernees prevalent"
    reference = "SR 651.1 Art. 4 al. 3"


class transmission_renseignements_tiers_exclue(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La transmission de renseignements concernant des tiers est exclue"
    reference = "SR 651.1 Art. 4 al. 3"

    def formula(self, period, parameters):
        concernee = self('personne_concernee_par_demande', period)
        pertinents = self('renseignements_vraisemblablement_pertinents', period)
        interets = self('interets_legitimes_prevalent', period)

        # Transmission exclue si personne non concernee ET (non pertinent OU interets prevalent)
        non_concernee = not_(concernee)
        return non_concernee * (not_(pertinents) + interets > 0)
