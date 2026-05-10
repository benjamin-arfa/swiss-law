"""SR 442.11 Art. 6

Generated from: ch/442/de/442.11.md

Unterstuetzung kultureller Organisationen: Professionelle Kulturschaffende
finanzieren mindestens die Haelfte des Lebensunterhalts oder setzen mindestens
die Haelfte der Normalarbeitszeit fuer kuenstlerische Taetigkeit ein.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anteil_einkommen_aus_kunst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil des Lebensunterhalts aus kuenstlerischer Taetigkeit (0-1)"
    reference = "SR 442.11 Art. 6 Abs. 2"


class anteil_arbeitszeit_fuer_kunst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Normalarbeitszeit fuer kuenstlerische Taetigkeit (0-1)"
    reference = "SR 442.11 Art. 6 Abs. 2"


class ist_professioneller_kulturschaffender(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als professioneller Kulturschaffender gilt"
    reference = "SR 442.11 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        einkommen = person('anteil_einkommen_aus_kunst', period)
        arbeitszeit = person('anteil_arbeitszeit_fuer_kunst', period)
        return (einkommen >= 0.5) + (arbeitszeit >= 0.5)


class ist_kulturell_taetiger_laie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als kulturell taetiger Laie gilt"
    reference = "SR 442.11 Art. 6 Abs. 3"

    def formula(person, period, parameters):
        professionell = person('ist_professioneller_kulturschaffender', period)
        hat_regelmaessige_taetigkeit = person('anteil_arbeitszeit_fuer_kunst', period) > 0
        return hat_regelmaessige_taetigkeit * (1 - professionell)
