"""SR 836.1 Art. 4

Generated from: ch/836/de/836.1.md

Art. 4: Anspruch auf Familienzulagen - Full allowances only for permanent
employees. Entitlement requires AHV contributions on annual income of at
least half the minimum full AHV old-age pension.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_in_dauerstellung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitskraft ist in Dauerstellung im landwirtschaftlichen Betrieb"
    reference = "SR 836.1 Art. 4"


class jaehrliches_erwerbseinkommen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jährliches Erwerbseinkommen, auf dem AHV-Beiträge entrichtet werden"
    reference = "SR 836.1 Art. 4"


class minimale_volle_ahv_altersrente_jaehrlich(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jährlicher Betrag der minimalen vollen Altersrente der AHV"
    reference = "SR 836.1 Art. 4"

    def formula(person, period, parameters):
        # Minimale volle AHV-Altersrente: 1'260 CHF/Monat = 15'120 CHF/Jahr
        # (Stand 2025, gemäss AHVG)
        return 15120.0


class anspruch_ganze_zulagen_dauerstellung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Anspruch auf ganze Familienzulagen bei Dauerstellung: jährliches "
        "Erwerbseinkommen >= halbe minimale volle AHV-Altersrente (Art. 4 FLG)"
    )
    reference = "SR 836.1 Art. 4"

    def formula(person, period, parameters):
        dauerstellung = person('ist_in_dauerstellung', period)
        einkommen = person('jaehrliches_erwerbseinkommen', period)
        min_rente = person('minimale_volle_ahv_altersrente_jaehrlich', period)
        mindesterwerbseinkommen = min_rente / 2
        return dauerstellung * (einkommen >= mindesterwerbseinkommen)
