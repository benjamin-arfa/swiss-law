"""SR 641.81 Art. 15 - Verjährung (Statute of limitations)

Heavy Vehicle Tax Act (SVAG) - Limitation periods.
Art. 15:
  Abs. 1: Tax claim prescribes 5 years after end of calendar year it became due
  Abs. 2: Refund claim prescribes 5 years after payment
  Abs. 4: Absolute limitation: 15 years

Generated from: ch/641/de/641.81.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class svag_abgabeforderung_faellig_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Calendar year in which the tax claim became due (SR 641.81 Art. 15)"
    reference = "SR 641.81 Art. 15"
    default_value = 0


class svag_abgabeforderung_verjaehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the tax claim is time-barred (SR 641.81 Art. 15 Abs. 1)"
    reference = "SR 641.81 Art. 15"

    def formula(person, period, parameters):
        faellig_jahr = person("svag_abgabeforderung_faellig_jahr", period)
        aktuelles_jahr = period.start.year
        verjaeherungsfrist = 5
        absolute_frist = 15

        # Regular limitation: 5 years after end of calendar year
        regulaer_verjaehrt = (aktuelles_jahr - faellig_jahr) > verjaeherungsfrist

        # Absolute limitation: 15 years in any case
        absolut_verjaehrt = (aktuelles_jahr - faellig_jahr) > absolute_frist

        return regulaer_verjaehrt + absolut_verjaehrt > 0


class svag_rueckforderung_verjaehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Whether the refund claim is time-barred - 5 years after payment (SR 641.81 Art. 15 Abs. 2)"
    reference = "SR 641.81 Art. 15"

    def formula(person, period, parameters):
        zahlung_jahr = person("svag_zahlung_nichtschuld_jahr", period)
        aktuelles_jahr = period.start.year
        return (aktuelles_jahr - zahlung_jahr) > 5


class svag_zahlung_nichtschuld_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Year of payment of unowed tax amount (SR 641.81 Art. 15 Abs. 2)"
    reference = "SR 641.81 Art. 15"
    default_value = 0
