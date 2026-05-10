"""SR 711 Art. 15

Generated from: ch/fr/711.md

Actes preparatoires (Preparatory acts) and notification deadlines:
- Surveys, staking, measurements: written notice 10 days before
- Soil/building analyses: written notice 30 days before, requires authorization if opposed
- Opposition period: 10 days
- Damage from preparatory acts: full compensation
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

DELAI_AVIS_ARPENTAGE_JOURS = 10
DELAI_AVIS_ANALYSES_JOURS = 30
DELAI_OPPOSITION_JOURS = 10


class est_arpentage_piquetage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "L'acte preparatoire est un passage, leve de plan, piquetage ou mesurage"
    reference = "SR 711 Art. 15 al. 1"


class est_analyse_sol_batiment(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "L'acte preparatoire est une analyse du sol ou du batiment"
    reference = "SR 711 Art. 15 al. 2"


class delai_avis_prealable_jours(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Delai d'avis prealable au proprietaire en jours"
    reference = "SR 711 Art. 15"

    def formula(person, period):
        import numpy as np
        arpentage = person('est_arpentage_piquetage', period)
        analyse = person('est_analyse_sol_batiment', period)
        return np.where(
            analyse,
            DELAI_AVIS_ANALYSES_JOURS,
            np.where(arpentage, DELAI_AVIS_ARPENTAGE_JOURS, 0)
        )


class dommage_actes_preparatoires_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Dommage resultant des actes preparatoires (CHF)"
    reference = "SR 711 Art. 15 al. 3"


class indemnite_actes_preparatoires_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Indemnite pleine et entiere pour dommage des actes preparatoires (CHF)"
    reference = "SR 711 Art. 15 al. 3"

    def formula(person, period):
        # Indemnite pleine et entiere = 100% du dommage
        return person('dommage_actes_preparatoires_chf', period)
