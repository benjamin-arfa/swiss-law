"""SR 631.011 Art. 1

Generated from: ch/631/de/631.011.md

Geschenksendungen: Von Privatpersonen mit Wohnsitz im Zollausland an
Privatpersonen mit Wohnsitz im Zollgebiet gesandte Geschenke sind bis
zu einem Wert von 100 Franken pro Sendung zollfrei.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class absender_ist_privatperson_zollausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Absender eine Privatperson mit Wohnsitz im Zollausland ist"
    reference = "SR 631.011 Art. 1 Abs. 1"


class empfaenger_ist_privatperson_zollgebiet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Empfaenger eine Privatperson mit Wohnsitz im Zollgebiet ist"
    reference = "SR 631.011 Art. 1 Abs. 1"


class geschenksendung_wert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Wert der Geschenksendung in Franken"
    reference = "SR 631.011 Art. 1 Abs. 1"


class geschenksendung_ist_tabak(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Geschenksendung Tabakfabrikate enthaelt"
    reference = "SR 631.011 Art. 1 Abs. 2 Bst. a"


class geschenksendung_ist_alkohol(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Geschenksendung alkoholische Getraenke enthaelt"
    reference = "SR 631.011 Art. 1 Abs. 2 Bst. b"


class geschenksendung_zollfrei(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Geschenksendung zollfrei ist (Art. 1 ZV-EFD)"
    reference = "SR 631.011 Art. 1"

    def formula(person, period, parameters):
        wert = person('geschenksendung_wert', period)
        absender_ok = person('absender_ist_privatperson_zollausland', period)
        empfaenger_ok = person('empfaenger_ist_privatperson_zollgebiet', period)
        ist_tabak = person('geschenksendung_ist_tabak', period)
        ist_alkohol = person('geschenksendung_ist_alkohol', period)

        wertfreigrenze = parameters(period).sr_631_011.geschenksendung_wertfreigrenze

        return (
            absender_ok
            * empfaenger_ok
            * (wert <= wertfreigrenze)
            * (1 - ist_tabak)
            * (1 - ist_alkohol)
        )
