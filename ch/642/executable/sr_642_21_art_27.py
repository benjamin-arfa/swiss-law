"""SR 642.21 Art. 27 - Auslaendische Anteilsinhaber (Foreign Unit Holders)

Generated from: ch/642/de/642.21.md

Art. 27: Foreign holders of units in collective investment schemes
(KAG) are entitled to a refund of the withholding tax deducted from
the income of those units, provided at least 80% of the income
originates from foreign sources.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vstg_anteil_auslaendische_quellen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Ertraege aus auslaendischen Quellen an den Gesamtertraegen (0-1)"
    reference = "SR 642.21 Art. 27"
    default_value = 0.0


class vstg_ist_auslaendischer_anteilsinhaber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person auslaendischer Inhaber von KAG-Anteilen ist"
    reference = "SR 642.21 Art. 27"


class vstg_rueckerstattung_auslaendische_anteilsinhaber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Rueckerstattung fuer auslaendische KAG-Anteilsinhaber"
    reference = "SR 642.21 Art. 27"

    def formula(person, period, parameters):
        ist_auslaender = person('vstg_ist_auslaendischer_anteilsinhaber', period)
        anteil = person('vstg_anteil_auslaendische_quellen', period)
        schwelle = parameters(period).sr_642_21.auslaendische_quellen_schwelle
        return ist_auslaender * (anteil >= schwelle)
