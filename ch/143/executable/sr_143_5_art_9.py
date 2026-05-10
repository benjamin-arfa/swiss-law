"""SR 143.5 Art. 9

Generated from: ch/143/fr/143.5.md

Travel reasons for asylum seekers and provisionally admitted:
limited travel reasons (serious illness/death, urgent personal matters,
school trips, sports/cultural events). Provisionally admitted:
max 30 days/year travel; after 3 years for non-humanitarian reasons.
Family members defined: parents, grandparents, siblings, spouse, children, grandchildren.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class odv_maladie_grave_ou_deces_famille(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Cas de grave maladie ou deces d'un membre de la famille"
    reference = "SR 143.5 Art. 9 al. 1 let. a"


class odv_affaires_strictement_personnelles(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Affaires importantes, strictement personnelles et ne souffrant aucun report"
    reference = "SR 143.5 Art. 9 al. 1 let. b"


class odv_voyage_scolaire_obligatoire(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Voyage transfrontalier rendu obligatoire par l'etablissement scolaire"
    reference = "SR 143.5 Art. 9 al. 1 let. c"


class odv_participation_manifestation_sportive_culturelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Participation active a une manifestation sportive ou culturelle a l'etranger"
    reference = "SR 143.5 Art. 9 al. 1 let. d"


class odv_motif_voyage_valable_requerant(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le requerant d'asile a un motif de voyage valable (al. 1)"
    reference = "SR 143.5 Art. 9 al. 1"

    def formula(person, period, parameters):
        maladie_deces = person('odv_maladie_grave_ou_deces_famille', period)
        affaires = person('odv_affaires_strictement_personnelles', period)
        scolaire = person('odv_voyage_scolaire_obligatoire', period)
        sport_culture = person('odv_participation_manifestation_sportive_culturelle', period)
        return (maladie_deces + affaires + scolaire + sport_culture) > 0


class odv_duree_max_voyage_provisoire_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree maximale de voyage par an pour personne admise provisoirement (30 jours)"
    reference = "SR 143.5 Art. 9 al. 4"

    def formula(person, period, parameters):
        return 30


class odv_annees_depuis_admission_provisoire(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre d'annees depuis le prononce de l'admission provisoire"
    reference = "SR 143.5 Art. 9 al. 4 let. b"


class odv_voyage_raisons_humanitaires(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Voyage pour raisons humanitaires"
    reference = "SR 143.5 Art. 9 al. 4 let. a"


class odv_voyage_autres_motifs_apres_3_ans(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Voyage pour autres motifs, 3 ans apres admission provisoire"
    reference = "SR 143.5 Art. 9 al. 4 let. b"

    def formula(person, period, parameters):
        annees = person('odv_annees_depuis_admission_provisoire', period.this_year)
        est_provisoire = person('odv_est_personne_admise_provisoirement', period)
        humanitaire = person('odv_voyage_raisons_humanitaires', period)
        return est_provisoire * not_(humanitaire) * (annees >= 3)
