"""SR 831.201 Art. 35bis

Generated from: ch/831/de/831.201.md

Ausschluss des Anspruchs auf Hilflosenentschaedigung:
- Abs. 1: Adults (>= 18) staying in an institution for integration measures
  for >= 24 days in a calendar month have NO entitlement for that month.
  Exception: Abs. 4 (severe sensory/physical disability social contacts).
- Abs. 2: Minors in institution have no entitlement for those specific days.
  Exception: Abs. 4 and Art. 42bis Abs. 4 IVG.
- Abs. 2bis: Minors in a medical institution under Art. 42bis Abs. 4 IVG
  must submit confirmation with IV invoice.
- Abs. 2ter: Minors paying their own institutional costs keep entitlement.
- Abs. 3: Institutional stay = days where IV covers institutional costs.
- Abs. 4: Exceptions do not apply to compensation for helplessness under
  Art. 37 Abs. 3 Bst. d (severe sensory/physical disability).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_alter_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Alter der versicherten Person in Jahren"
    reference = "SR 831.201 Art. 35bis Abs. 1"


class iv_aufenthalt_institution_tage_monat(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tage im Kalendermonat in einer Institution (IV-finanziert)"
    reference = "SR 831.201 Art. 35bis Abs. 1, 3"


class iv_traegt_heimkosten_selbst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die minderjaehrige Person die Kosten fuer den Heimaufenthalt selbst traegt"
    reference = "SR 831.201 Art. 35bis Abs. 2ter"


class iv_hilflosigkeit_wegen_sinnesschaedigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Hilflosenentschaedigung wegen schwerer Sinnesschaedigung/Koerpergebrechen (Art. 37 Abs. 3 Bst. d)"
    reference = "SR 831.201 Art. 35bis Abs. 4 / Art. 37 Abs. 3 Bst. d"


class iv_hilflosenentschaedigung_ausgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Anspruch auf Hilflosenentschaedigung wegen Institutionsaufenthalt ausgeschlossen ist"
    reference = "SR 831.201 Art. 35bis"

    def formula(person, period, parameters):
        import numpy as np
        alter = person('iv_alter_jahre', period)
        tage = person('iv_aufenthalt_institution_tage_monat', period)
        selbstzahler = person('iv_traegt_heimkosten_selbst', period)
        sinnesschaedigung = person('iv_hilflosigkeit_wegen_sinnesschaedigung', period)

        # Abs. 4: Exception - never excluded for severe sensory/physical disability
        # Abs. 1: Adults >= 18 in institution >= 24 days -> excluded
        erwachsen_ausschluss = (alter >= 18) & (tage >= 24)

        # Abs. 2: Minors in institution -> excluded for those days (simplified: any days)
        # Abs. 2ter: Minors paying own costs keep entitlement
        minderjaehrig_ausschluss = (alter < 18) & (tage > 0) & ~selbstzahler

        ausschluss = (erwachsen_ausschluss | minderjaehrig_ausschluss)

        # Abs. 4: Not excluded for Art. 37 Abs. 3 Bst. d cases
        return ausschluss & ~sinnesschaedigung
