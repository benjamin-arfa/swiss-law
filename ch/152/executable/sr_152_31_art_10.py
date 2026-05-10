"""SR 152.31 Art. 10

Generated from: ch/152/de/152.31.md

Requests requiring particularly extensive processing: when the authority
cannot process the request without substantially impairing other tasks.
Must be processed within a reasonable time.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuch_erfordert_besonders_aufwendige_bearbeitung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Gesuch eine besonders aufwendige Bearbeitung erfordert"
    reference = "SR 152.31 Art. 10 Abs. 1"


class erfuellung_anderer_aufgaben_wesentlich_beeintraechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Erfuellung anderer Aufgaben durch die Bearbeitung wesentlich beeintraechtigt wuerde"
    reference = "SR 152.31 Art. 10 Abs. 1"


class bearbeitung_innert_angemessener_frist(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Gesuch innert einer angemessenen Frist behandelt wird"
    reference = "SR 152.31 Art. 10 Abs. 2"
