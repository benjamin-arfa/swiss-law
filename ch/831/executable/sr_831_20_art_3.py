"""SR 831.20 Art. 3

Generated from: ch/831/de/831.20.md

Art. 3: Beitragsbemessung und -bezug - Contribution rates for disability
insurance:
- Abs. 1: Contributions from employment income are 1.4% (IV rate).
- Abs. 1bis: Non-employed persons: minimum CHF 70/year (obligatory) or
  CHF 140/year (voluntary). Maximum = 50x the obligatory minimum.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_beitragssatz_erwerbstaetige(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "IV-Beitragssatz auf Erwerbseinkommen"
    reference = "SR 831.20 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return 0.014


class iv_beitrag_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "IV-Beitrag aus Erwerbseinkommen"
    reference = "SR 831.20 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        einkommen = person('erwerbseinkommen', period)
        return einkommen * 0.014


class iv_mindestbeitrag_nichterwerbstaetige_obligatorisch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "IV-Mindestbeitrag fuer obligatorisch versicherte Nichterwerbstaetige (CHF/Jahr)"
    reference = "SR 831.20 Art. 3 Abs. 1bis"

    def formula(person, period, parameters):
        return parameters(period).iv.mindestbeitrag_nichterwerbstaetige_obligatorisch


class iv_mindestbeitrag_nichterwerbstaetige_freiwillig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "IV-Mindestbeitrag fuer freiwillig versicherte Nichterwerbstaetige (CHF/Jahr)"
    reference = "SR 831.20 Art. 3 Abs. 1bis"

    def formula(person, period, parameters):
        return parameters(period).iv.mindestbeitrag_nichterwerbstaetige_freiwillig


class iv_hoechstbeitrag_nichterwerbstaetige(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "IV-Hoechstbeitrag fuer Nichterwerbstaetige (50x Mindestbeitrag obligatorisch)"
    reference = "SR 831.20 Art. 3 Abs. 1bis"

    def formula(person, period, parameters):
        mindest = parameters(period).iv.mindestbeitrag_nichterwerbstaetige_obligatorisch
        return mindest * 50
