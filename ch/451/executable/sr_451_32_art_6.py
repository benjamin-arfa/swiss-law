"""SR 451.32 Art. 6

Generated from: ch/451/de/451.32.md
Hochmoorverordnung - Fristen: 3 Jahre, bzw. 6 Jahre fuer belastete Kantone.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_finanzschwacher_kanton_hochmoor(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kanton ist finanzschwach/mittelstark und durch Hochmoorschutz stark belastet"
    reference = "SR 451.32 Art. 6 Abs. 2"


class objekt_erhaltung_gefaehrdet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Objekt ist in seiner Erhaltung gefaehrdet"
    reference = "SR 451.32 Art. 6 Abs. 2"


class frist_schutzmassnahmen_hochmoor_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Schutzmassnahmen bei Hochmooren in Jahren"
    reference = "SR 451.32 Art. 6"

    def formula(person, period, parameters):
        finanzschwach = person('ist_finanzschwacher_kanton_hochmoor', period)
        gefaehrdet = person('objekt_erhaltung_gefaehrdet', period)
        # Abs. 1: 3 Jahre, Abs. 2: 6 Jahre fuer finanzschwache Kantone bei nicht gefaehrdeten Objekten
        return where(finanzschwach * not_(gefaehrdet), 6, 3)
