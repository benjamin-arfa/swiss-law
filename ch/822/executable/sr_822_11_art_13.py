"""SR 822.11 Art. 13

Generated from: ch/822/de/822.11.md

Art. 13: Lohnzuschlag fuer Ueberzeitarbeit
- Abs. 1: Lohnzuschlag von mindestens 25% fuer Ueberzeitarbeit;
  fuer Bueropersonal/technische Angestellte/Verkaufspersonal erst ab
  60 Stunden Ueberzeit im Kalenderjahr
- Abs. 2: Kein Zuschlag wenn durch Freizeit gleicher Dauer ausgeglichen
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arg_ueberzeit_durch_freizeit_ausgeglichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = False
    label = "Ueberzeitarbeit wird durch Freizeit gleicher Dauer ausgeglichen"
    reference = "SR 822.11 Art. 13 Abs. 2"


class arg_ueberzeit_zuschlagspflichtige_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zuschlagspflichtige Ueberzeitstunden im Kalenderjahr"
    reference = "SR 822.11 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        ueberzeit_total = person('arg_ueberzeit_stunden_jahr', period)
        ausgeglichen = person('arg_ueberzeit_durch_freizeit_ausgeglichen', period)
        buero = person('arg_bueropersonal_oder_angestellte', period.first_month)
        # If compensated by time off, no surcharge
        # For office/technical staff: surcharge only above 60h/year
        freibetrag = where(buero, 60.0, 0.0)
        zuschlagspflichtig = max_(ueberzeit_total - freibetrag, 0.0)
        return where(ausgeglichen, 0.0, zuschlagspflichtig)


class arg_ueberzeit_lohnzuschlag_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    default_value = 25.0
    label = "Lohnzuschlag fuer Ueberzeitarbeit in Prozent (mindestens 25%)"
    reference = "SR 822.11 Art. 13 Abs. 1"
