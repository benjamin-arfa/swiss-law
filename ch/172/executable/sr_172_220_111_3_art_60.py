"""SR 172.220.111.3 Art. 60 - Conge maternite (Maternity Leave)

Generated from: ch/172/fr/172.220.111.3.md

Federal personnel maternity leave:
- 4 months paid maternity leave at full salary
- If newborn hospitalized >= 2 weeks immediately after birth: extended by hospitalization duration
- Maximum total: 154 days (with hospitalization extension)
- Can start up to 2 weeks before expected delivery date
- Full salary + social allowances during first 4 months
- If extended due to hospitalization: only statutory maternity allowance (EOG/APG)
- If other parent dies within 6 months of birth: 20 additional working days
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class opers_naissance_enfant(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'employee a donne naissance a un ou plusieurs enfants"
    reference = "SR 172.220.111.3 Art. 60 al. 1"


class opers_nouveau_ne_hospitalise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le nouveau-ne a ete hospitalise de facon ininterrompue au moins 2 semaines apres la naissance"
    reference = "SR 172.220.111.3 Art. 60 al. 1"


class opers_jours_hospitalisation_nouveau_ne(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours d'hospitalisation ininterrompue du nouveau-ne"
    reference = "SR 172.220.111.3 Art. 60 al. 1"


class opers_autre_parent_decede_6_mois(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Le pere ou deuxieme parent est decede dans les 6 mois suivant la naissance"
    reference = "SR 172.220.111.3 Art. 60 al. 1bis"


class opers_conge_maternite_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree totale du conge maternite en jours calendaires"
    reference = "SR 172.220.111.3 Art. 60"

    def formula(person, period, parameters):
        naissance = person('opers_naissance_enfant', period)
        hospitalise = person('opers_nouveau_ne_hospitalise', period)
        jours_hospi = person('opers_jours_hospitalisation_nouveau_ne', period)
        parent_decede = person('opers_autre_parent_decede_6_mois', period)

        # Base: 4 mois = ~122 jours calendaires (4 * 30.5)
        base_jours = 122

        # Extension for hospitalization: capped at 154 total
        extension_hospi = where(hospitalise, min_(jours_hospi, 154 - base_jours), 0)

        # Additional 20 working days (~28 calendar days) if other parent deceased
        extension_deces = where(parent_decede, 28, 0)

        total = where(naissance, base_jours + extension_hospi + extension_deces, 0)
        return total


class opers_conge_maternite_max_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Duree maximale du conge maternite avec hospitalisation (154 jours)"
    reference = "SR 172.220.111.3 Art. 60 al. 1"

    def formula(person, period, parameters):
        return where(person('opers_naissance_enfant', period), 154, 0)
