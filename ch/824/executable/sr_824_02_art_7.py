"""SR 824.02 Art. 7-9

Generated from: ch/824/de/824.02.md

Pensum und Dienstleistung: Work arrangements in pilot projects -
full-time, part-time (50-90%), or hourly. Conversion rules for
service days.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zdpv_pensum_prozent(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Arbeitspensum in Prozent (50, 60, 70, 80, 90 oder 100)"
    reference = "SR 824.02 Art. 7 Abs. 1 Bst. a"
    default_value = 100


class zdpv_ist_stundenweise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Zivildienstleistung stundenweise erbracht wird"
    reference = "SR 824.02 Art. 7 Abs. 1 Bst. b"
    default_value = False


class zdpv_geleistete_stunden_monat(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Im Monat geleistete Stunden (bei stundenweiser Dienstleistung)"
    reference = "SR 824.02 Art. 9 Abs. 1"
    default_value = 0.0


class zdpv_diensttage_monat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Angerechnete Diensttage im Monat"
    reference = "SR 824.02 Art. 8-9"

    def formula(person, period, parameters):
        stundenweise = person('zdpv_ist_stundenweise', period)
        stunden = person('zdpv_geleistete_stunden_monat', period)

        # Stundenweise: pro 8 Stunden = 1 Diensttag
        tage_stundenweise = (stunden / 8).astype(int)

        # Teilzeit: Pensum wird monatsweise in ganze Tage umgerechnet
        # (simplified: assume ~21 working days per month)
        pensum = person('zdpv_pensum_prozent', period)
        tage_teilzeit = (21 * pensum / 100).astype(int)

        return where(stundenweise, tage_stundenweise, tage_teilzeit)
