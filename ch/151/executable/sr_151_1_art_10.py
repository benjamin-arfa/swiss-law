"""SR 151.1 Art. 10 - Protection contre le conge (Protection Against Dismissal)

Generated from: ch/151/fr/151.1.md

Retaliation protection for workers who raise discrimination complaints:
- Dismissal is voidable if it follows a complaint, conciliation, or lawsuit
  and lacks justified grounds
- Protection lasts during internal proceedings, conciliation, trial,
  AND 6 months after conclusion
- Worker must challenge dismissal within the notice period
- Worker may opt for CO Art. 336a indemnity instead of reinstatement
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class leg_a_depose_reclamation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le travailleur a adresse une reclamation, ouvert une conciliation ou introduit une action"
    reference = "SR 151.1 Art. 10 al. 1"


class leg_conge_motif_justifie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le conge repose sur un motif justifie"
    reference = "SR 151.1 Art. 10 al. 1"


class leg_procedure_en_cours(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Une procedure (interne, conciliation ou judiciaire) est en cours"
    reference = "SR 151.1 Art. 10 al. 2"


class leg_mois_depuis_cloture_procedure(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Nombre de mois ecoules depuis la cloture de la procedure"
    reference = "SR 151.1 Art. 10 al. 2"


class leg_conge_annulable(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le conge est annulable car il fait suite a une reclamation sans motif justifie"
    reference = "SR 151.1 Art. 10 al. 1"

    def formula(person, period, parameters):
        reclamation = person('leg_a_depose_reclamation', period)
        motif_justifie = person('leg_conge_motif_justifie', period)
        return reclamation * (1 - motif_justifie)


class leg_protection_contre_conge_active(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "La protection contre le conge est active (procedure en cours ou moins de 6 mois apres)"
    reference = "SR 151.1 Art. 10 al. 2"

    def formula(person, period, parameters):
        en_cours = person('leg_procedure_en_cours', period)
        mois_depuis = person('leg_mois_depuis_cloture_procedure', period)

        # Protection during proceedings AND 6 months after
        dans_delai_post = mois_depuis <= 6
        return en_cours + (1 - en_cours) * dans_delai_post
