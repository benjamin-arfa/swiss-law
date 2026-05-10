"""SR 824.012.2 Art. 1

Generated from: ch/824/de/824.012.2.md

Biodiversitaetsfoerderflaechen: Service days per hectare for civilian service
deployments in agricultural operations for biodiversity areas.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zdv_wbf_extensiv_wiesen_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare extensiv genutzte Wiesen"
    reference = "SR 824.012.2 Art. 1 Abs. 1 Bst. a"
    default_value = 0.0


class zdv_wbf_wenig_intensiv_wiesen_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare wenig intensiv genutzte Wiesen"
    reference = "SR 824.012.2 Art. 1 Abs. 1 Bst. b"
    default_value = 0.0


class zdv_wbf_extensiv_weiden_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare extensiv genutzte Weiden"
    reference = "SR 824.012.2 Art. 1 Abs. 1 Bst. c"
    default_value = 0.0


class zdv_wbf_waldweiden_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare Waldweiden"
    reference = "SR 824.012.2 Art. 1 Abs. 1 Bst. d"
    default_value = 0.0


class zdv_wbf_streueflaechen_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare Streuflaechen"
    reference = "SR 824.012.2 Art. 1 Abs. 1 Bst. e"
    default_value = 0.0


class zdv_wbf_hecken_ha(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hektare Hecken, Feld- und Ufergehoelze"
    reference = "SR 824.012.2 Art. 1 Abs. 1 Bst. f"
    default_value = 0.0


class zdv_wbf_hochstamm_baeume(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Hochstamm-Feldobstbaeume"
    reference = "SR 824.012.2 Art. 1 Abs. 2 Bst. a"
    default_value = 0


class zdv_wbf_diensttage_biodiversitaet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zustehende Diensttage fuer Biodiversitaetsfoerderflaechen"
    reference = "SR 824.012.2 Art. 1"

    def formula(person, period, parameters):
        p = parameters(period).sr_824_012_2

        tage = (
            person('zdv_wbf_extensiv_wiesen_ha', period) * p.diensttage_extensiv_wiesen +
            person('zdv_wbf_wenig_intensiv_wiesen_ha', period) * p.diensttage_wenig_intensiv_wiesen +
            person('zdv_wbf_extensiv_weiden_ha', period) * p.diensttage_extensiv_weiden +
            person('zdv_wbf_waldweiden_ha', period) * p.diensttage_waldweiden +
            person('zdv_wbf_streueflaechen_ha', period) * p.diensttage_streueflaechen +
            person('zdv_wbf_hecken_ha', period) * p.diensttage_hecken +
            person('zdv_wbf_hochstamm_baeume', period) * p.diensttage_pro_baum
        )
        return tage
