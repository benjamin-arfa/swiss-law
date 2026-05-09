"""SR 172.220.111.3 Art. 61 - Versement du salaire en cas d'adoption (Adoption Leave)

Generated from: ch/172/fr/172.220.111.3.md

Adoption leave for federal personnel:
- 2 months paid leave when adopting young children
- If both adoptive parents work in federal administration:
  right applies to only one parent, but they can split the 2 months freely
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class opers_adoption_enfant(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'employe accueille un jeune enfant en vue d'adoption"
    reference = "SR 172.220.111.3 Art. 61 al. 1"


class opers_deux_parents_administration(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Les deux parents adoptifs travaillent dans l'administration federale"
    reference = "SR 172.220.111.3 Art. 61 al. 2"


class opers_conge_adoption_mois(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de mois de conge d'adoption avec salaire"
    reference = "SR 172.220.111.3 Art. 61"

    def formula(person, period, parameters):
        adoption = person('opers_adoption_enfant', period)
        # 2 mois, repartis librement si les deux parents sont dans l'administration
        return where(adoption, 2, 0)
