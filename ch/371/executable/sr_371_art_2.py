"""SR 371 Art. 2 - Begriff (Definition)

Generated from: ch/de/371.md
Refugee helpers are persons convicted for helping persecuted people flee during
the Nazi era or for sheltering refugees without reporting them. Excludes persons
who exploited, abandoned, or denounced the refugees.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class verurteilt_wegen_fluchthilfe_ns_zeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verurteilt wegen Fluchthilfe oder Beherbergung von Fluechtlingen zur NS-Zeit"
    reference = "SR 371 Art. 2 Abs. 1"
    default_value = False


class hat_fluechtlinge_ausgenutzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat verfolgte Menschen ausgenutzt, im Stiche gelassen oder denunziert"
    reference = "SR 371 Art. 2 Abs. 2"
    default_value = False


class gilt_als_fluechtlingshelfer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gilt als Fluechtlingshelfer im Sinne des Gesetzes"
    reference = "SR 371 Art. 2"

    def formula(person, period, parameters):
        verurteilt = person('verurteilt_wegen_fluchthilfe_ns_zeit', period)
        ausgenutzt = person('hat_fluechtlinge_ausgenutzt', period)
        return verurteilt * not_(ausgenutzt)
