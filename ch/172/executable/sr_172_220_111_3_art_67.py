"""SR 172.220.111.3 Art. 67 - Vacances (Annual Leave / Vacation)

Generated from: ch/172/fr/172.220.111.3.md

Vacation entitlement for federal personnel by age:
- Up to and including the year of turning 20: 6 weeks
- From the year of turning 21: 5 weeks
- From the year of turning 50: 6 weeks
- From the year of turning 60: 7 weeks

Must be taken in the calendar year earned; if impossible due to operational
reasons, illness or accident, must be taken the following year.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class opers_age_employe(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Age de l'employe (annee en cours)"
    reference = "SR 172.220.111.3 Art. 67 al. 1"


class opers_vacances_semaines(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de semaines de vacances annuelles"
    reference = "SR 172.220.111.3 Art. 67 al. 1"

    def formula(person, period, parameters):
        age = person('opers_age_employe', period)

        # Age brackets (year in which the age is reached)
        return select(
            [age >= 60, age >= 50, age >= 21, age <= 20],
            [7, 6, 5, 6]
        )


class opers_vacances_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Nombre de jours ouvres de vacances annuelles"
    reference = "SR 172.220.111.3 Art. 67 al. 1"

    def formula(person, period, parameters):
        semaines = person('opers_vacances_semaines', period)
        return semaines * 5
