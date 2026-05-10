"""SR 823.113 Art. 1

Generated from: ch/823/de/823.113.md

Bewilligungsgebühr für Arbeitsvermittlungsstellen:
- Bewilligungsgebühr: 750–1650 CHF je nach Aufwand
- Änderungsgebühr: 220–850 CHF je nach Aufwand
- Gemeinnützige Institutionen: Herabsetzung oder Erlass möglich
- Rückzug des Gesuchs: Gebühr bis zur maximalen Höhe der Bewilligungsgebühr
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_gemeinnuetzige_institution(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Arbeitsvermittlungsstelle einer gemeinnützigen Institution gehört"
    reference = "SR 823.113 Art. 1 Abs. 3"


class aufwand_bewilligungsbehoerde(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufwandfaktor der Bewilligungsbehörde (0.0 bis 1.0)"
    reference = "SR 823.113 Art. 1 Abs. 1"


class bewilligungsgebuehr_arbeitsvermittlung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bewilligungsgebühr für Arbeitsvermittlungsstellen (750–1650 CHF)"
    reference = "SR 823.113 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        aufwand = person('aufwand_bewilligungsbehoerde', period)
        min_gebuehr = parameters(period).sr_823_113.bewilligungsgebuehr_min
        max_gebuehr = parameters(period).sr_823_113.bewilligungsgebuehr_max
        gebuehr = min_gebuehr + aufwand * (max_gebuehr - min_gebuehr)
        gemeinnuetzig = person('ist_gemeinnuetzige_institution', period)
        return np.where(gemeinnuetzig, 0, gebuehr)


class aenderungsgebuehr_arbeitsvermittlung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebühr bei Änderungen der Bewilligung (220–850 CHF)"
    reference = "SR 823.113 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        aufwand = person('aufwand_bewilligungsbehoerde', period)
        min_gebuehr = parameters(period).sr_823_113.aenderungsgebuehr_min
        max_gebuehr = parameters(period).sr_823_113.aenderungsgebuehr_max
        return min_gebuehr + aufwand * (max_gebuehr - min_gebuehr)
