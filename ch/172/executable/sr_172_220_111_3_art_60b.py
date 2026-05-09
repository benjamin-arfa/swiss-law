"""SR 172.220.111.3 Art. 60b - Conge paternite (Paternity Leave)

Generated from: ch/172/fr/172.220.111.3.md

Federal personnel paternity/partner leave:
- 20 working days paid leave for legally recognized father
- Same 20 days for registered partner at birth of partner's child
- Must be taken within 6 months of birth (as separate days or cumulated)
- If mother dies on delivery day or within 97 days: 4 additional months
  (starts day after death, must be taken consecutively)
- If mother dies AND newborn hospitalized >= 2 weeks: Art. 60 al. 1+3 apply by analogy
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class opers_est_pere_juridique(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Est reconnu comme pere sur le plan juridique"
    reference = "SR 172.220.111.3 Art. 60b al. 1"


class opers_est_partenaire_enregistre(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Est partenaire enregistre de la mere"
    reference = "SR 172.220.111.3 Art. 60b al. 2"


class opers_mere_decedee_dans_97_jours(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "La mere est decedee le jour de l'accouchement ou dans les 97 jours suivants"
    reference = "SR 172.220.111.3 Art. 60b al. 3"


class opers_conge_paternite_jours_ouvres(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours ouvres de conge paternite/partenaire"
    reference = "SR 172.220.111.3 Art. 60b"

    def formula(person, period, parameters):
        pere = person('opers_est_pere_juridique', period)
        partenaire = person('opers_est_partenaire_enregistre', period)
        mere_decedee = person('opers_mere_decedee_dans_97_jours', period)
        naissance = person('opers_naissance_enfant', period)

        a_droit = (pere + partenaire) > 0

        # Base: 20 working days
        base = 20

        # If mother deceased: +4 months ~ 88 working days (4 * 22)
        supplement_deces = where(mere_decedee, 88, 0)

        return where(naissance * a_droit, base + supplement_deces, 0)


class opers_delai_conge_paternite_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai pour prendre le conge paternite (6 mois des la naissance)"
    reference = "SR 172.220.111.3 Art. 60b al. 1"

    def formula(person, period, parameters):
        return where(person('opers_naissance_enfant', period), 6, 0)
