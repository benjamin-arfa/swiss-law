"""SR 823.113 Art. 7

Generated from: ch/823/de/823.113.md

Bewilligungsgebühr für Personalverleihbetriebe:
- Bewilligungsgebühr: 750–1650 CHF je nach Aufwand
- Änderungsgebühr: 220–850 CHF je nach Aufwand
- Rückzug des Gesuchs: Gebühr bis zur maximalen Höhe

Note: Same fee structure as Art. 1 (Arbeitsvermittlungsstellen),
parameters reused from sr_823_113_art_1.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufwand_behoerde_personalverleih(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufwandfaktor der Bewilligungsbehörde für Personalverleih (0.0 bis 1.0)"
    reference = "SR 823.113 Art. 7 Abs. 1"


class bewilligungsgebuehr_personalverleih(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bewilligungsgebühr für Personalverleihbetriebe (750–1650 CHF)"
    reference = "SR 823.113 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        aufwand = person('aufwand_behoerde_personalverleih', period)
        min_gebuehr = parameters(period).sr_823_113.bewilligungsgebuehr_min
        max_gebuehr = parameters(period).sr_823_113.bewilligungsgebuehr_max
        return min_gebuehr + aufwand * (max_gebuehr - min_gebuehr)


class aenderungsgebuehr_personalverleih(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Änderungsgebühr für Personalverleihbetriebe (220–850 CHF)"
    reference = "SR 823.113 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        aufwand = person('aufwand_behoerde_personalverleih', period)
        min_gebuehr = parameters(period).sr_823_113.aenderungsgebuehr_min
        max_gebuehr = parameters(period).sr_823_113.aenderungsgebuehr_max
        return min_gebuehr + aufwand * (max_gebuehr - min_gebuehr)
