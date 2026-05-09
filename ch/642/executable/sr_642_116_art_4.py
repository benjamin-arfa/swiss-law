"""SR 642.116 Art. 4

Generated from: ch/642/de/642.116.md

Art. 4: Costs transferable to the two following tax periods
(Auf die beiden nachfolgenden Steuerperioden uebertragbare Kosten)

If energy-saving investment costs or demolition costs cannot be fully
offset in the year incurred, the remaining costs can be carried forward
to the next tax period (Abs. 1). If still not fully offset, they can be
carried forward one more period (Abs. 2).

Carry-forward occurs if net income is negative (Abs. 3).
No lump-sum deduction can be claimed in carry-forward periods (Abs. 4).
The right to carry forward remains upon change of domicile or property
transfer (Abs. 5).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class liegenschaft_uebertragbare_kosten_vorperiode(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aus der Vorperiode uebertragene Energiespar-/Rueckbaukosten (CHF)"
    reference = "SR 642.116 Art. 4 Abs. 1"
    default_value = 0


class liegenschaft_uebertragbare_kosten_vorvorperiode(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aus der Vorvorperiode uebertragene Energiespar-/Rueckbaukosten (CHF)"
    reference = "SR 642.116 Art. 4 Abs. 2"
    default_value = 0


class liegenschaft_reineinkommen_negativ(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Reineinkommen ist negativ (Voraussetzung fuer Kostenübertrag)"
    reference = "SR 642.116 Art. 4 Abs. 3"


class liegenschaft_energiespar_abzug_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamter abziehbarer Betrag fuer Energiespar-/Rueckbaukosten inkl. Vortraege (CHF)"
    reference = "SR 642.116 Art. 4"

    def formula(person, period, parameters):
        aktuelle_energiespar = person('liegenschaft_energiespar_investition_abzug', period)
        aktuelle_rueckbau = person('liegenschaft_rueckbaukosten_abzug', period)
        vortrag_1 = person('liegenschaft_uebertragbare_kosten_vorperiode', period)
        vortrag_2 = person('liegenschaft_uebertragbare_kosten_vorvorperiode', period)

        return aktuelle_energiespar + aktuelle_rueckbau + vortrag_1 + vortrag_2
