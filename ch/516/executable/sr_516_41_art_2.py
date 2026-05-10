"""SR 516.41 Art. 2 - Champ d'application

Generated from: ch/516/fr/516.41.md

Scope: military legislation applies; OJPM provisions take
priority over this ordinance for military criminal procedure.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class membre_justice_militaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La personne est membre de la justice militaire"
    reference = "SR 516.41 Art. 2 al. 2"


class ojpm_regle_procedure_penale(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'OJPM regle la procedure penale militaire en la matiere"
    reference = "SR 516.41 Art. 2 al. 4"


class legislation_militaire_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La legislation militaire s'applique"
    reference = "SR 516.41 Art. 2 al. 1"
    default_value = True


class ojpm_prime_sur_ojm(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Les dispositions de l'OJPM priment sur celles de la presente ordonnance"
    reference = "SR 516.41 Art. 2 al. 4"

    def formula(self, period, parameters):
        return self('ojpm_regle_procedure_penale', period)
