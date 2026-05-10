"""SR 232.21 Art. 28

Generated from: ch/232/de/232.21.md

Art. 28 defines criminal penalties for unlawful use of public signs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unrechtmaessiger_gebrauch_oeffentliches_zeichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person gebraucht unrechtmaessig geschuetzte oeffentliche Zeichen"
    reference = "SR 232.21 Art. 28 Abs. 1"


class handelt_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Taeterin oder der Taeter handelt vorsaetzlich"
    reference = "SR 232.21 Art. 28 Abs. 1"


class handelt_gewerbsmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Taeterin oder der Taeter handelt gewerbsmaessig"
    reference = "SR 232.21 Art. 28 Abs. 2"


class strafbar_unzulaessiger_gebrauch_zeichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Strafbarkeit wegen unzulaessigem Gebrauch oeffentlicher Zeichen"
    reference = "SR 232.21 Art. 28"

    def formula(person, period, parameters):
        unrechtmaessig = person('unrechtmaessiger_gebrauch_oeffentliches_zeichen', period)
        vorsaetzlich = person('handelt_vorsaetzlich', period)
        return unrechtmaessig * vorsaetzlich


class strafmass_gewerbsmaessig_zeichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Erhoehtes Strafmass (Freiheitsstrafe bis 5 Jahre) wegen gewerbsmaessigem Handeln"
    reference = "SR 232.21 Art. 28 Abs. 2"

    def formula(person, period, parameters):
        strafbar = person('strafbar_unzulaessiger_gebrauch_zeichen', period)
        gewerbsmaessig = person('handelt_gewerbsmaessig', period)
        return strafbar * gewerbsmaessig
