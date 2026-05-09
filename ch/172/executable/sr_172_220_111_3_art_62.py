"""SR 172.220.111.3 Art. 62 - Versement du salaire en cas de deces (Death Benefit)

Generated from: ch/172/fr/172.220.111.3.md

If an employee dies, survivors receive 1/6 of the annual salary.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class opers_salaire_annuel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Salaire annuel de l'employe"
    reference = "SR 172.220.111.3 Art. 62"


class opers_employe_decede(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "L'employe est decede"
    reference = "SR 172.220.111.3 Art. 62 al. 1"


class opers_prestation_deces_survivants(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prestation versee aux survivants (1/6 du salaire annuel)"
    reference = "SR 172.220.111.3 Art. 62 al. 1"

    def formula(person, period, parameters):
        salaire = person('opers_salaire_annuel', period)
        decede = person('opers_employe_decede', period)
        return where(decede, salaire / 6, 0)
