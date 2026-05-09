"""SR 857.51 Art. 1

Generated from: ch/857/de/857.51.md

Organisation der Schwangerschaftsberatungsstellen.
Kantone organisieren die gesetzlich vorgeschriebenen Beratungsstellen,
regeln Anerkennung, Finanzierung und Beaufsichtigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class schwangerschaftsberatungsstelle_vom_kanton_organisiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ist die Schwangerschaftsberatungsstelle vom Kanton organisiert?"
    reference = "SR 857.51 Art. 1 Abs. 1"


class schwangerschaftsberatungsstelle_anerkannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ist die Schwangerschaftsberatungsstelle vom Kanton anerkannt?"
    reference = "SR 857.51 Art. 1 Abs. 2"


class schwangerschaftsberatungsstelle_auch_sexual_ehe_familienberatung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Erfuellt die Beratungsstelle auch Aufgaben der Sexual-, Ehe- und Familienberatung?"
    reference = "SR 857.51 Art. 1 Abs. 3"
