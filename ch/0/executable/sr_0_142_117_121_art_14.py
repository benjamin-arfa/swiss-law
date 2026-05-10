"""SR 0.142.117.121 Art. 14

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class migrant_reintegration_contributions(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "Migrant reintegration contributions (Article 14a)"

    def formula(household, period, parameters):
        migrant_population = household("migrant_population", period)
        program_budget = parameters(period).migration_management.migrant_reintegration_program_budget
        return migrant_population * program_budget

class migration_management_programs(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Implementation of migration management programs (Article 14d)"

    def formula(household, period, parameters):
        program_implemented = household("migration_management_program_implemented", period)
        return program_implemented

class migrationssteuerungssystem(Variable):
    value_type = float
    entity = Household
    definition_period = YEAR
    label = "National migrant management system performance (Article 14e)"

    def formula(household, period, parameters):
        system_performance = household("migrationssteuerungssystem_performance", period)
        return system_performance
