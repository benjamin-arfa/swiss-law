"""SR 152.31 Art. 16

Generated from: ch/152/de/152.31.md

Fee tariff and information about expected costs: tariff in Annex 1.
10-day deadline for applicant to confirm request after being informed
of intended fee. Request deemed withdrawn if no confirmation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class gebuehrenerhebung_angekuendigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Behoerde die beabsichtigte Gebuehrenerhebung mitgeteilt hat"
    reference = "SR 152.31 Art. 16 Abs. 2"


class frist_bestaetigung_gesuch_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist in Tagen fuer Bestaetigung des Zugangsgesuchs nach Gebuehrenankuendigung"
    reference = "SR 152.31 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        return 10


class gesuch_bestaetigung_nach_gebuehreninfo(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die gesuchstellende Person das Gesuch nach Gebuehreninfo bestaetigt hat"
    reference = "SR 152.31 Art. 16 Abs. 2"


class gesuch_zurueckgezogen_keine_bestaetigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Gesuch als zurueckgezogen gilt weil keine Bestaetigung erfolgte"
    reference = "SR 152.31 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        angekuendigt = person('gebuehrenerhebung_angekuendigt', period)
        bestaetigt = person('gesuch_bestaetigung_nach_gebuehreninfo', period)
        return angekuendigt * not_(bestaetigt)
