"""SR 116 Art. 1 - Grundsatz (Federal Holiday Principle)

Generated from: ch/de/116.md
The Swiss National Day (August 1) is a work-free day equivalent to Sundays.
Full wage must be paid. It does not count toward cantonal holiday quotas.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class bundesfeiertag_ist_arbeitsfrei(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bundesfeiertag (1. August) ist ein den Sonntagen gleichgestellter arbeitsfreier Tag"
    reference = "SR 116 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return True


class bundesfeiertag_lohnzahlungspflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Volle Lohnzahlungspflicht des Arbeitgebers fuer den arbeitsfreien Bundesfeiertag"
    reference = "SR 116 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        return True


class bundesfeiertag_zaehlt_als_kantonaler_feiertag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ob der Bundesfeiertag der Anzahl der kantonalen Feiertage nach ArG Art. 18 Abs. 2 angerechnet wird"
    reference = "SR 116 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        # Der Bundesfeiertag wird NICHT den kantonalen Feiertagen angerechnet
        return False
