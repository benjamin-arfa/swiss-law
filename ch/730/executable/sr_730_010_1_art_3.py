"""SR 730.010.1 Art. 3

Generated from: ch/730/fr/730.010.1.md

Art. 3 - Exception to registration:
The following installations cannot be registered:
a. Photovoltaic installations with power < 2 kW
b. Other technology installations with nominal AC power < 2 kVA
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ogom_enregistrement_interdit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the installation is too small to be registered for guarantees of origin"
    reference = "SR 730.010.1 Art. 3"

    def formula(person, period, parameters):
        est_photovoltaique = person('ogom_est_photovoltaique', period)
        puissance_kw = person('ogom_puissance_kw', period)
        puissance_kva = person('ogom_puissance_nominale_ca_kva', period)
        p = parameters(period).sr_730_010_1

        # PV: threshold in kW; others: threshold in kVA
        return where(
            est_photovoltaique,
            puissance_kw < p.seuil_enregistrement_pv_kw,
            puissance_kva < p.seuil_enregistrement_autres_kva
        )


class ogom_est_photovoltaique(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the installation is photovoltaic"
    reference = "SR 730.010.1 Art. 3"


class ogom_puissance_kw(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Power of the installation (kW)"
    reference = "SR 730.010.1 Art. 3"
