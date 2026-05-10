"""SR 837.174 Art. 8 – Festsetzung des Beitragssatzes

Generated from: ch/837/de/837.174.md

Der Beitragssatz für die Risiken Tod und Invalidität beträgt
0.25 Prozent des koordinierten Tageslohnes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bvg_beitragssatz_arbeitslose(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beitragssatz für Risiken Tod und Invalidität (Anteil)"
    reference = "SR 837.174 Art. 8 Abs. 1"
    # 0.25 Prozent seit 1. Jan. 2019 (AS 2018 4689)
    default_value = 0.0025


class bvg_beitrag_arbeitslose_tag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Täglicher BVG-Beitrag für arbeitslose Person (CHF)"
    reference = "SR 837.174 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        koord_lohn = person('koordinierter_tageslohn_berechnet', period)
        satz = person('bvg_beitragssatz_arbeitslose', period.this_year)
        return koord_lohn * satz
