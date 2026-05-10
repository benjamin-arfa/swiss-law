"""SR 831.111 Art. 7

Generated from: ch/831/de/831.111.md

Art. 7: Voraussetzungen - Requirements for joining voluntary insurance.

Abs. 1: Persons meeting the conditions of Art. 2 Abs. 1 AHVG may join
the voluntary insurance, including those subject to mandatory insurance
for part of their income.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vfv_erfuellt_versicherungsvoraussetzungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person erfuellt die Versicherungsvoraussetzungen nach Art. 2 Abs. 1 AHVG"
    reference = "SR 831.111 Art. 7 Abs. 1"


class vfv_teilweise_obligatorisch_versichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist fuer einen Teil ihres Einkommens der obligatorischen Versicherung unterstellt"
    reference = "SR 831.111 Art. 7 Abs. 1"


class vfv_beitritt_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beitritt zur freiwilligen AHV/IV moeglich (Art. 7 VFV)"
    reference = "SR 831.111 Art. 7"

    def formula(person, period, parameters):
        return person('vfv_erfuellt_versicherungsvoraussetzungen', period)
