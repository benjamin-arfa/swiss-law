"""SR 150.1 Art. 12

Generated from: ch/150/de/150.1.md

Finanzierung: Der Bund kommt fuer die Mittel auf. Mitglieder haben
Anspruch auf Auslagenersatz. Bundesrat regelt Entschaedigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_anspruch_auslagenersatz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Kommissionsmitglied Anspruch auf Auslagenersatz hat"
    reference = "SR 150.1 Art. 12 Abs. 2"
    default_value = True
