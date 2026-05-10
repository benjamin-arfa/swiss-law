"""SR 446.2 Art. 18

Generated from: ch/446/de/446.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jugendschutzregelung_genuegt_anforderungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die fuer verbindlich erklaerte Jugendschutzregelung genuegt noch den Anforderungen"
    reference = "SR 446.2 Art. 18 Abs. 1"


class branchenorg_hat_aenderung_ohne_verbindlicherklaerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Branchenorganisation hat Aenderung in Kraft gesetzt ohne Verbindlicherklaerung durch Bundesrat"
    reference = "SR 446.2 Art. 18 Abs. 2"


class verbindlicherklaerung_widerrufen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verbindlicherklaerung wurde widerrufen (genuegt Anforderungen nicht mehr)"
    reference = "SR 446.2 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        genuegt = person('jugendschutzregelung_genuegt_anforderungen', period)
        return not_(genuegt)


class verbindlicherklaerung_hinfaellig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verbindlicherklaerung ist hinfaellig (nicht genehmigte Aenderung)"
    reference = "SR 446.2 Art. 18 Abs. 2"

    def formula(person, period, parameters):
        return person('branchenorg_hat_aenderung_ohne_verbindlicherklaerung', period)
