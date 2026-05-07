"""SR 455.102.4 Art. 3

Generated from: ch/455/de/455.102.4.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class belastungskategorie(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Belastungskategorie des Tieres (0-3) nach Art. 3 SR 455.102.4"
    reference = "SR 455.102.4 Art. 3"
    # 0 = keine Belastung
    # 1 = leichte Belastung
    # 2 = mittlere Belastung
    # 3 = starke Belastung


class ist_leichte_belastung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Belastende Auspraegung kann durch Pflege/Haltung/Fuetterung kompensiert werden ohne Eingriffe (Art. 3 Abs. 2 SR 455.102.4)"
    reference = "SR 455.102.4 Art. 3 Abs. 2"


# Input variables for compensation assessment
class kompensierbar_durch_pflege(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Belastung kompensierbar durch geeignete Pflege, Haltung oder Fuetterung"
    reference = "SR 455.102.4 Art. 3 Abs. 2"


class erfordert_eingriff_am_tier(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Belastung erfordert Eingriffe am Tier"
    reference = "SR 455.102.4 Art. 3 Abs. 2"


class erfordert_regelmaessige_medizinische_pflege(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Belastung erfordert regelmaessige medizinische Pflegemassnahmen"
    reference = "SR 455.102.4 Art. 3 Abs. 2"


class belastung_ist_leicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Leichte Belastung nach Art. 3 Abs. 2 SR 455.102.4"
    reference = "SR 455.102.4 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        kompensierbar = person('kompensierbar_durch_pflege', period)
        kein_eingriff = not_(person('erfordert_eingriff_am_tier', period))
        keine_med_pflege = not_(person('erfordert_regelmaessige_medizinische_pflege', period))
        return kompensierbar * kein_eingriff * keine_med_pflege
