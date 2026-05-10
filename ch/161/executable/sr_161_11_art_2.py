"""SR 161.11 Art. 2

Generated from: ch/161/fr/161.11.md

Change of political domicile: if changed within 4 weeks before a federal vote,
must prove they have not already voted at old domicile to receive new voting material.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class odp_changement_domicile_politique(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La personne a change de domicile politique"
    reference = "SR 161.11 Art. 2"


class odp_delai_changement_avant_scrutin_semaines(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai critique avant scrutin pour changement de domicile (4 semaines)"
    reference = "SR 161.11 Art. 2"

    def formula(person, period, parameters):
        return 4


class odp_changement_dans_4_semaines_avant_scrutin(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le changement de domicile a eu lieu dans les 4 semaines precedant le scrutin"
    reference = "SR 161.11 Art. 2"


class odp_doit_prouver_non_vote_ancien_domicile(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Doit prouver ne pas avoir deja vote a l'ancien domicile politique"
    reference = "SR 161.11 Art. 2"

    def formula(person, period, parameters):
        changement = person('odp_changement_domicile_politique', period)
        dans_delai = person('odp_changement_dans_4_semaines_avant_scrutin', period)
        return changement * dans_delai
