"""SR 152.3 Art. 12

Generated from: ch/152/de/152.3.md

Stellungnahme der Behoerde: Fristen von 20 Tagen, Verlaengerung um 20 Tage.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuch_betrifft_umfangreiche_dokumente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesuch umfangreiche, komplexe oder schwer beschaffbare Dokumente betrifft"
    reference = "SR 152.3 Art. 12 Abs. 2"


class frist_stellungnahme_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist fuer die Stellungnahme der Behoerde in Tagen"
    reference = "SR 152.3 Art. 12"

    def formula(person, period, parameters):
        umfangreich = person('gesuch_betrifft_umfangreiche_dokumente', period)
        # 20 Tage normal, 40 Tage bei umfangreichen Dokumenten
        return 20 + umfangreich * 20
