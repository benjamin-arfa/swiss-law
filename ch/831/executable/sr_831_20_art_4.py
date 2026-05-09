"""SR 831.20 Art. 4

Generated from: ch/831/de/831.20.md

Art. 4 Invaliditaet (Disability):
1. Disability (Art. 8 ATSG) may result from congenital defects, illness or
   accident.
2. Disability is deemed to have occurred as soon as it has reached the type
   and severity required to establish entitlement to the respective benefit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_ursache_geburtsgebrechen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Invaliditaet ist Folge von Geburtsgebrechen"
    reference = "SR 831.20 Art. 4 Abs. 1"


class iv_ursache_krankheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Invaliditaet ist Folge von Krankheit"
    reference = "SR 831.20 Art. 4 Abs. 1"


class iv_ursache_unfall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Invaliditaet ist Folge eines Unfalls"
    reference = "SR 831.20 Art. 4 Abs. 1"


class iv_invaliditaet_eingetreten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Invaliditaet gilt als eingetreten (erforderliche Art und Schwere erreicht)"
    reference = "SR 831.20 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        geburtsgebrechen = person('iv_ursache_geburtsgebrechen', period.this_year)
        krankheit = person('iv_ursache_krankheit', period.this_year)
        unfall = person('iv_ursache_unfall', period.this_year)
        iv_grad = person('iv_invaliditaetsgrad_prozent', period.this_year)

        # Art. 4 Abs. 1: mindestens eine Ursache muss vorliegen
        hat_ursache = geburtsgebrechen + krankheit + unfall

        # Art. 4 Abs. 2: erforderliche Art und Schwere erreicht (min. 40% fuer Rente)
        return hat_ursache * (iv_grad >= 40)
