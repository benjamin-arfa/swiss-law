"""SR 642.21 Art. 32 - Verwirkung des Rueckerstattungsanspruchs (Forfeiture of Refund)

Generated from: ch/642/de/642.21.md

Art. 32 Abs. 1: The refund claim expires if not filed within 3 years
after the end of the calendar year in which the taxable benefit became due.

Art. 32 Abs. 2: If the withholding tax is paid only after an objection by
the ESTV and the 3-year period has already elapsed or fewer than 60 days
remain, a new 60-day period begins upon payment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vstg_faelligkeitsjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Kalenderjahr, in dem die steuerbare Leistung faellig wurde"
    reference = "SR 642.21 Art. 32 Abs. 1"


class vstg_antrag_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Rueckerstattungsantrag eingereicht wurde"
    reference = "SR 642.21 Art. 32 Abs. 1"


class vstg_nachtraegliche_entrichtung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Steuer erst nach ESTV-Beanstandung entrichtet wurde"
    reference = "SR 642.21 Art. 32 Abs. 2"


class vstg_rueckerstattung_verwirkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Anspruch auf Rueckerstattung verwirkt ist"
    reference = "SR 642.21 Art. 32"

    def formula(person, period, parameters):
        import numpy as np
        faelligkeitsjahr = person('vstg_faelligkeitsjahr', period)
        antrag = person('vstg_antrag_eingereicht', period)
        nachtraeglich = person('vstg_nachtraegliche_entrichtung', period)

        p = parameters(period).sr_642_21
        frist = p.rueckerstattungsfrist_jahre

        aktuelles_jahr = period.start.year
        jahre_seit_faelligkeit = aktuelles_jahr - faelligkeitsjahr

        # Art. 32(1): expired if > 3 years and no application filed
        frist_abgelaufen = jahre_seit_faelligkeit > frist

        # Art. 32(2): if paid late after ESTV objection, new 60-day period
        # (modeled as: not forfeited if late payment triggered extension)
        verlaengerung = nachtraeglich * frist_abgelaufen

        return frist_abgelaufen * np.logical_not(antrag) * np.logical_not(verlaengerung)
