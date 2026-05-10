"""SR 740.1 Art. 8 - Foerderung des Schienengueterverkehrs

Generated from: ch/740/de/740.1.md

Im unbegleiteten kombinierten Verkehr hat die Hoehe der durchschnittlichen
Abgeltung pro transportierte Sendung von Jahr zu Jahr abzunehmen.
Der begleitete kombinierte Verkehr kann bis Ende 2028 gefoerdert werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# Input variables

class durchschnittliche_abgeltung_ukv_pro_sendung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Durchschnittliche Abgeltung pro transportierte Sendung im unbegleiteten kombinierten Verkehr (CHF)"
    reference = "SR 740.1 Art. 8 Abs. 2"


class durchschnittliche_abgeltung_ukv_vorjahr(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Durchschnittliche Abgeltung UKV im Vorjahr (CHF)"
    reference = "SR 740.1 Art. 8 Abs. 2"


# Computed variables

class abgeltung_ukv_abnehmend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die durchschnittliche Abgeltung im UKV nimmt von Jahr zu Jahr ab"
    reference = "SR 740.1 Art. 8 Abs. 2"

    def formula(self, period, parameters):
        aktuell = self('durchschnittliche_abgeltung_ukv_pro_sendung', period)
        vorjahr = self('durchschnittliche_abgeltung_ukv_vorjahr', period)
        return aktuell < vorjahr


class foerderung_rollende_landstrasse_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Foerderung der Rollenden Landstrasse (begleiteter kombinierter Verkehr) ist zulaessig"
    reference = "SR 740.1 Art. 8 Abs. 3"

    def formula(self, period, parameters):
        # Foerderung bis Ende 2028 zulaessig
        return period.start.year <= 2028

    def formula_2029(self, period, parameters):
        return False
