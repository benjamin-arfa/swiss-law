"""SR 351.20 Art. 15

Generated from: ch/351/de/351.20.md
Cost rules for detention and transfer to international courts.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class haftkosten_ueberstellung_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten der Haft und der Ueberstellung an das Internationale Gericht in CHF"
    reference = "SR 351.20 Art. 15 Abs. 1"


class vermoegenswerte_verfolgte_person_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Vermoegenswerte der verfolgten Person in CHF"
    reference = "SR 351.20 Art. 15 Abs. 2"


class vermoegenswerte_herausgabe_gericht_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Vermoegenswerte die dem Internationalen Gericht herauszugeben sind in CHF"
    reference = "SR 351.20 Art. 15 Abs. 2"


class verwendbare_vermoegenswerte_fuer_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Vermoegenswerte die zur Kostendeckung verwendet werden koennen in CHF"
    reference = "SR 351.20 Art. 15 Abs. 2"

    def formula(person, period):
        vermoegen = person('vermoegenswerte_verfolgte_person_chf', period)
        herausgabe = person('vermoegenswerte_herausgabe_gericht_chf', period)
        kosten = person('haftkosten_ueberstellung_chf', period)
        # Vermoegenswerte abzueglich der an das Gericht herauszugebenden
        verfuegbar = max_(vermoegen - herausgabe, 0)
        return min_(verfuegbar, kosten)
