"""SR 704.1 Art. 1

Generated from: ch/704/de/704.1.md

Ueberpruefung und Anpassung der Plaene: Plans for foot and hiking path
networks must be reviewed every 10 years and adjusted if necessary.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class fwv_plan_ueberpruefung_intervall_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Intervall fuer die Ueberpruefung der Fuss- und Wanderwegplaene in Jahren"
    reference = "SR 704.1 Art. 1"

    def formula(person, period, parameters):
        return 10  # in der Regel alle zehn Jahre
