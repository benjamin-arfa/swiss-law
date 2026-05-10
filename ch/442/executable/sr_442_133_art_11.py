"""SR 442.133 Art. 11

Generated from: ch/442/de/442.133.md

Bemessung der Beitraege der Kantone an die Talente:
- Stufe Basis: 1'000 CHF
- Stufe Aufbau I: 1'500 CHF
- Stufe Aufbau II: 2'000 CHF
- Stufe PreCollege: 2'500 CHF
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class foerderstufe_talent(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Foerderstufe (1=Basis, 2=Aufbau I, 3=Aufbau II, 4=PreCollege)"
    reference = "SR 442.133 Art. 11 Abs. 1"


class beitrag_pro_talent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beitrag pro Talent und Jahr (CHF)"
    reference = "SR 442.133 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        stufe = person('foerderstufe_talent', period)
        return (
            (stufe == 1) * 1000
            + (stufe == 2) * 1500
            + (stufe == 3) * 2000
            + (stufe == 4) * 2500
        )
