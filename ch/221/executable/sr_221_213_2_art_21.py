"""SR 221.213.2 Art. 21

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class paechter_im_zahlungsrueckstand(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pächter ist mit einer Zinszahlung im Rückstand"
    reference = "SR 221.213.2 Art. 21 Abs. 1"


class schriftliche_androhung_erfolgt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verpächter hat schriftlich Vertragsauflösung angedroht"
    reference = "SR 221.213.2 Art. 21 Abs. 1"


class ausstehender_zins_nicht_bezahlt_innert_6_monaten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausstehender Zins wurde nicht innerhalb von 6 Monaten nach Androhung bezahlt"
    reference = "SR 221.213.2 Art. 21 Abs. 1"


class pachtvertrag_aufgeloest_wegen_zahlungsrueckstand(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pachtvertrag wird wegen Zahlungsrückstand aufgelöst"
    reference = "SR 221.213.2 Art. 21"

    def formula(person, period, parameters):
        rueckstand = person('paechter_im_zahlungsrueckstand', period)
        androhung = person('schriftliche_androhung_erfolgt', period)
        nicht_bezahlt = person('ausstehender_zins_nicht_bezahlt_innert_6_monaten', period)
        return rueckstand * androhung * nicht_bezahlt
