"""SR 516.41 Art. 3 - Taches de la justice militaire

Generated from: ch/516/fr/516.41.md

Tasks: military justice acts as administrative and criminal authority;
DDPS may assign administrative investigations to judicial officers.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class autorite_administrative_et_penale(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La justice militaire agit en qualite d'autorite administrative et penale"
    reference = "SR 516.41 Art. 3 al. 1"

    def formula(self, period, parameters):
        return self('membre_justice_militaire', period)


class officier_justice_charge_enquete_administrative(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le DDPS a confie a l'officier de justice une enquete administrative"
    reference = "SR 516.41 Art. 3 al. 2"
