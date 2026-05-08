"""SR 916.341.21 Art. 2

Generated from: ch/916/fr/916.341.21.md

Utilisation et surveillance des appareils de classification.
Classification devices from Annex 1 are used by experts of the mandated organisation;
those from Annex 2 are periodically monitored. Faulty devices may not be used for
quality taxation until the defect is remedied.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class appareil_classification_annexe_1(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = MONTH
    label = "Classification device is approved under Annex 1 (used by mandated experts)"
    reference = "SR 916.341.21 Art. 2 al. 1"


class appareil_classification_annexe_2(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = MONTH
    label = "Classification device is approved under Annex 2 (periodically monitored)"
    reference = "SR 916.341.21 Art. 2 al. 2"


class appareil_defaut_constate(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = MONTH
    label = "A defect has been found during homologation or monitoring of the device"
    reference = "SR 916.341.21 Art. 2 al. 5"


class appareil_autorise_pour_taxation(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = MONTH
    label = "The classification device is authorized for quality taxation"
    reference = "SR 916.341.21 Art. 2 al. 5"

    def formula_2000(organisation, period, parameters):
        annexe_1 = organisation('appareil_classification_annexe_1', period)
        annexe_2 = organisation('appareil_classification_annexe_2', period)
        defaut = organisation('appareil_defaut_constate', period)

        est_admis = annexe_1 + annexe_2 > 0
        return est_admis * not_(defaut)
