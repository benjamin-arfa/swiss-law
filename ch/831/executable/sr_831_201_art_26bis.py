"""SR 831.201 Art. 26bis

Generated from: ch/831/de/831.201.md

Bestimmung des Einkommens mit Invaliditaet:
- Abs. 1: Actual income if best use of remaining capacity
- Abs. 2: Otherwise statistical values (LSE)
- Abs. 3: 10% deduction from statistical value; 20% if functional capacity <= 50%
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_erwerbseinkommen_mit_invaliditaet_tatsaechlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tatsaechlich erzieltes Erwerbseinkommen nach Eintritt der Invaliditaet"
    reference = "SR 831.201 Art. 26bis Abs. 1"


class iv_hat_anrechenbares_erwerbseinkommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein anrechenbares Erwerbseinkommen vorliegt"
    reference = "SR 831.201 Art. 26bis Abs. 1-2"


class iv_statistischer_lohnwert(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Statistischer Lohnwert (LSE-Zentralwert) fuer die versicherte Person"
    reference = "SR 831.201 Art. 25 Abs. 3 / Art. 26bis Abs. 2"


class iv_funktionelle_leistungsfaehigkeit_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Funktionelle Leistungsfaehigkeit in Prozent (0-100)"
    reference = "SR 831.201 Art. 26bis Abs. 3"


class iv_einkommen_mit_invaliditaet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Massgebendes Einkommen mit Invaliditaet (Art. 26bis IVV)"
    reference = "SR 831.201 Art. 26bis"

    def formula(person, period, parameters):
        import numpy as np
        hat_einkommen = person('iv_hat_anrechenbares_erwerbseinkommen', period)
        tatsaechlich = person('iv_erwerbseinkommen_mit_invaliditaet_tatsaechlich', period)
        statistisch = person('iv_statistischer_lohnwert', period)
        leistungsfaehigkeit = person('iv_funktionelle_leistungsfaehigkeit_prozent', period)

        # Abs. 3: deduction from statistical value
        # 20% if functional capacity <= 50%, otherwise 10%
        abzug = np.where(leistungsfaehigkeit <= 50, 0.20, 0.10)
        einkommen_statistisch = statistisch * (1 - abzug)

        return np.where(hat_einkommen, tatsaechlich, einkommen_statistisch)
