"""SR 631.011 Art. 16

Generated from: ch/631/de/631.011.md

Zahlungserleichterungen: ZAZ-Zahlungsfrist und Ratenzahlungen bei
wirtschaftlichen oder sozialen Schwierigkeiten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zaz_barhinterlage_geleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine entsprechende Barhinterlage geleistet wurde"
    reference = "SR 631.011 Art. 16 Abs. 1"


class zahlungsfrist_zaz_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Zahlungsfrist im Rahmen des ZAZ in Tagen"
    reference = "SR 631.011 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        barhinterlage = person('zaz_barhinterlage_geleistet', period)
        max_frist = parameters(period).sr_631_011.zaz_max_zahlungsfrist_tage
        # Maximale Zahlungsfrist nur bei geleisteter Barhinterlage
        return barhinterlage * max_frist


class erhebliche_wirtschaftliche_schwierigkeiten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Zahlung der Zollschuld zu erheblichen wirtschaftlichen/sozialen Schwierigkeiten fuehren wuerde"
    reference = "SR 631.011 Art. 16 Abs. 2"


class ratenzahlung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Ratenzahlung der Zollschuld zulaessig ist"
    reference = "SR 631.011 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        return person('erhebliche_wirtschaftliche_schwierigkeiten', period)
