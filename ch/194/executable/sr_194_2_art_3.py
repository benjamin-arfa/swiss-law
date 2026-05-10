"""SR 194.2 Art. 3 - Auftrag

Generated from: ch/194/de/194.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class leistungsvereinbarung_maximale_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer der Leistungsvereinbarung in Jahren"
    reference = "SR 194.2 Art. 3 Abs. 2"

    def formula(self, period, parameters):
        # Die Leistungsvereinbarung kann jeweils fuer hoechstens vier Jahre geschlossen werden
        return 4


class leistungsvereinbarung_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Vereinbarte Dauer der Leistungsvereinbarung in Jahren"
    reference = "SR 194.2 Art. 3 Abs. 2"


class leistungsvereinbarung_dauer_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Dauer der Leistungsvereinbarung ist zulaessig"
    reference = "SR 194.2 Art. 3 Abs. 2"

    def formula(self, period, parameters):
        dauer = self('leistungsvereinbarung_dauer_jahre', period)
        max_dauer = self('leistungsvereinbarung_maximale_dauer_jahre', period)
        return dauer <= max_dauer


class beauftragung_gilt_nicht_als_oeffentlicher_auftrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Beauftragung gilt nicht als oeffentlicher Auftrag im Sinne von Art. 9 BoeB"
    reference = "SR 194.2 Art. 3 Abs. 1bis"

    def formula(self, period, parameters):
        # Gilt kraft Gesetz nicht als oeffentlicher Auftrag
        return 1
