"""SR 642.132 Art. 4

Generated from: ch/642/de/642.132.md

Art. 4: Conclusion of investigation; costs, compensation
(Abschluss der Untersuchung; Kosten, Entschaedigungen)

Abs. 1: The report is delivered simultaneously to the accused and
the responsible cantonal tax administrations. Where a legal basis
exists, it is also sent to other federal agencies with fiscal claims.

Abs. 2: If the investigation is discontinued for lack of offences,
costs may be imposed on the accused (Art. 183 Abs. 4 DBG). The
accused may claim compensation per Art. 99-100 VStrR within one year
of notification of discontinuation.

Procedural article with a time limit (1 year for compensation claims).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class steuer_untersuchung_eingestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Steuerliche Sonderuntersuchung wurde mangels Widerhandlungen eingestellt"
    reference = "SR 642.132 Art. 4 Abs. 2"


class steuer_entschaedigungsanspruch_frist_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer Entschaedigungsbegehren (1 Jahr) ist abgelaufen"
    reference = "SR 642.132 Art. 4 Abs. 2"
