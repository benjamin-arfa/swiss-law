"""SR 831.20 Art. 6

Generated from: ch/831/de/831.20.md

Art. 6: Versicherungsmaessige Voraussetzungen - Insurance prerequisites:
- Abs. 1: Swiss and foreign nationals as well as stateless persons are
  entitled to benefits.
- Abs. 2: Foreign nationals require domicile/habitual residence in
  Switzerland AND either at least 1 full year of contributions at onset of
  disability OR 10 years uninterrupted residence.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_ist_schweizer_buerger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ist Schweizer Staatsangehoerige/r"
    reference = "SR 831.20 Art. 6 Abs. 1"


class iv_wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hat Wohnsitz und gewoehnlichen Aufenthalt in der Schweiz"
    reference = "SR 831.20 Art. 6 Abs. 2"


class iv_beitragsjahre_bei_eintritt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Volle Beitragsjahre bei Eintritt der Invaliditaet"
    reference = "SR 831.20 Art. 6 Abs. 2"


class iv_aufenthaltsjahre_schweiz(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Ununterbrochene Aufenthaltsjahre in der Schweiz"
    reference = "SR 831.20 Art. 6 Abs. 2"


class iv_versicherungsvoraussetzung_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Versicherungsmaessige Voraussetzungen fuer IV-Leistungen erfuellt (Art. 6 IVG)"
    reference = "SR 831.20 Art. 6"

    def formula(person, period, parameters):
        schweizer = person('iv_ist_schweizer_buerger', period.this_year)
        wohnsitz = person('iv_wohnsitz_schweiz', period)
        beitragsjahre = person('iv_beitragsjahre_bei_eintritt', period.this_year)
        aufenthalt = person('iv_aufenthaltsjahre_schweiz', period.this_year)

        # Swiss nationals: entitled per Abs. 1
        # Foreign nationals: domicile in CH + (1 year contributions OR 10 years residence)
        auslaender_berechtigt = (
            wohnsitz *
            ((beitragsjahre >= 1) + (aufenthalt >= 10))
        )
        return schweizer + (schweizer == 0) * auslaender_berechtigt
