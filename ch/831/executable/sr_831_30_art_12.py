"""SR 831.30 Art. 12

Generated from: ch/831/de/831.30.md

Art. 12: Beginn und Ende des Anspruchs auf jaehrliche Ergaenzungsleistungen -
Start and end of entitlement to annual supplementary benefits.

Abs. 1: Entitlement exists from the beginning of the month in which the
application was submitted, provided all legal conditions are met.

Abs. 2: If the application is submitted within 6 months of admission to
a home/hospital, entitlement exists from the beginning of the month
of admission, provided all conditions are met.

Abs. 3: Entitlement ends at the end of the month in which one of the
conditions ceases to be met.

Abs. 4: The Federal Council regulates back-payments; it may shorten the
period set in Art. 24 Abs. 1 ATSG.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_anmeldung_monat(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Monat der EL-Anmeldung (Format YYYY-MM)"
    reference = "SR 831.30 Art. 12 Abs. 1"


class el_heimeintritt_monat(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Monat des Heim- oder Spitaleintritts (Format YYYY-MM)"
    reference = "SR 831.30 Art. 12 Abs. 2"


class el_anmeldung_innert_6_monaten_nach_heimeintritt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anmeldung innert 6 Monaten nach Heim-/Spitaleintritt eingereicht"
    reference = "SR 831.30 Art. 12 Abs. 2"


class el_voraussetzung_dahingefallen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Eine der Voraussetzungen fuer EL-Anspruch ist dahingefallen (Art. 12 Abs. 3 ELG)"
    reference = "SR 831.30 Art. 12 Abs. 3"


class el_anspruch_besteht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "EL-Anspruch besteht im laufenden Monat (Art. 12 ELG)"
    reference = "SR 831.30 Art. 12"

    def formula(person, period, parameters):
        voraussetzungen = person('el_voraussetzungen_art4_bis_6_erfuellt', period)
        dahingefallen = person('el_voraussetzung_dahingefallen', period)
        return voraussetzungen * not_(dahingefallen)
