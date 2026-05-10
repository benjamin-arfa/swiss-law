"""SR 514.544.2 Art. 9

Generated from: ch/514/de/514.544.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

import datetime


Organisation = build_entity(key='organisation', plural='organisations', label='An organisation')


class waffenhandlung_betrieben_nach_bisherigem_recht(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Geschaeftsraeume nach bisherigem Recht betrieben"


class waffenhandlung_uebergangsrecht_gueltig(Variable):
    value_type = bool
    entity = Organisation
    definition_period = YEAR
    label = "Uebergangsrecht fuer bestehende Waffenhandlungen gueltig (Art. 9 SR 514.544.2)"
    reference = "SR 514.544.2 Art. 9"

    def formula(organisation, period, parameters):
        # Nach bisherigem Recht betriebene Geschaeftsraeume duerfen noch bis
        # zum 31. Dezember 2026 weitergefuehrt werden
        bisheriges_recht = organisation('waffenhandlung_betrieben_nach_bisherigem_recht', period)
        # Period year must be <= 2026
        jahr = period.start.year
        return bisheriges_recht * (jahr <= 2026)
