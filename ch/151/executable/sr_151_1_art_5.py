"""SR 151.1 Art. 5 - Droits des travailleurs (Workers' Rights / Indemnity Caps)

Generated from: ch/151/fr/151.1.md

Indemnity caps for gender discrimination under the Gender Equality Act:
- Hiring refusal: max 3 months' salary (per person AND total for same position)
- Termination or sexual harassment: max 6 months' salary
- Damages and moral tort claims are reserved (no cap)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class leg_discrimination_type(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Type de discrimination LEg: 0=aucune, 1=embauche, 2=resiliation, 3=harcelement_sexuel"
    reference = "SR 151.1 Art. 5"


class leg_salaire_mensuel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Salaire mensuel de reference pour le calcul de l'indemnite LEg"
    reference = "SR 151.1 Art. 5 al. 2"


class leg_indemnite_max_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre maximum de mois de salaire pour l'indemnite selon le type de discrimination"
    reference = "SR 151.1 Art. 5 al. 2-4"

    def formula(person, period, parameters):
        discrimination = person('leg_discrimination_type', period)

        # Art. 5 al. 4: refus d'embauche -> max 3 mois
        # Art. 5 al. 4: resiliation ou harcelement -> max 6 mois
        plafond = select(
            [discrimination == 0, discrimination == 1, discrimination == 2, discrimination == 3],
            [0, 3, 6, 6]
        )
        return plafond


class leg_indemnite_max_montant(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Montant maximum de l'indemnite LEg en francs"
    reference = "SR 151.1 Art. 5 al. 2-4"

    def formula(person, period, parameters):
        salaire = person('leg_salaire_mensuel', period.first_month)
        mois_max = person('leg_indemnite_max_mois', period)
        return salaire * mois_max
