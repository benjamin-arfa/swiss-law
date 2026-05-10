"""SR 425.15 Art. 9

Generated from: ch/425/de/425.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_gericht_oder_kantonale_behoerde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein Gericht oder eine kantonale Behoerde"
    reference = "SR 425.15 Art. 9 Abs. 1"


class ist_internationale_organisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine internationale Organisation"
    reference = "SR 425.15 Art. 9 Abs. 2"


class kosten_weiterverrechenbar_an_nicht_ermaessigungsberechtigte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kosten koennen an nicht ermaessigungsberechtigte Personen weiterverrechnet werden"
    reference = "SR 425.15 Art. 9 Abs. 3"


class ermaessigung_stundenansatz_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ermaessigung der Stundenansaetze in Prozent"
    reference = "SR 425.15 Art. 9"

    def formula(person, period, parameters):
        gericht = person('ist_gericht_oder_kantonale_behoerde', period)
        weiterverrechenbar = person('kosten_weiterverrechenbar_an_nicht_ermaessigungsberechtigte', period)
        # 50% Ermaessigung fuer Gerichte/kantonale Behoerden, aber nicht bei Weiterverrechnung
        return where(gericht * not_(weiterverrechenbar), 50.0, 0.0)
