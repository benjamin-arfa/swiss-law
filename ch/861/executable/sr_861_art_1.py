"""SR 861 Art. 1

Generated from: ch/de/861.md

Purpose of the KBFHG: improve compatibility of family and work/education.
Federal financial aid for creating childcare places, increasing cantonal
subsidies, and projects for better alignment of care offers.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kbfhg_zweck_vereinbarkeit_familie_erwerbstaetigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bund die bessere Vereinbarkeit von Familie und Erwerbstaetigkeit oder Ausbildung anstrebt"
    reference = "SR 861 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return True


class finanzhilfe_schaffung_betreuungsplaetze(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Finanzhilfen fuer die Schaffung von familienergaenzenden Betreuungsplaetzen gewaehrt werden"
    reference = "SR 861 Art. 1 Abs. 2 Bst. a"


class finanzhilfe_erhoehung_subventionen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Finanzhilfen fuer die Erhoehung kantonaler und kommunaler Subventionen gewaehrt werden"
    reference = "SR 861 Art. 1 Abs. 2 Bst. b"


class finanzhilfe_projekte_abstimmung_beduerfnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Finanzhilfen fuer Projekte zur besseren Abstimmung des Betreuungsangebotes auf Elternbeduerfnisse gewaehrt werden"
    reference = "SR 861 Art. 1 Abs. 2 Bst. c"
