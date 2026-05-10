"""SR 195.1 Art. 14

Generated from: ch/195/de/195.1.md

Streichung des Eintrags und Vernichtung der Daten: Gruende fuer die
Streichung aus dem Auslandschweizerregister.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_wohnsitz_in_schweiz_begruendet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in der Schweiz Wohnsitz begruendet hat"
    reference = "SR 195.1 Art. 14 Abs. 1 lit. a"


class hat_schweizer_staatsangehoerigkeit_verloren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nicht mehr die Schweizer Staatsangehoerigkeit besitzt"
    reference = "SR 195.1 Art. 14 Abs. 1 lit. b"


class ist_minderjaehrig_ohne_bestaetigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die als Minderjaehrige eingetragene Person nach Volljaehrigkeit trotz Aufforderung nicht innert 90 Tagen bestaetigt hat"
    reference = "SR 195.1 Art. 14 Abs. 1 lit. c"


class ist_verstorben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person verstorben ist"
    reference = "SR 195.1 Art. 14 Abs. 1 lit. d"


class nicht_erreichbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nicht oder nicht mehr unter der angegebenen Adresse erreichbar ist"
    reference = "SR 195.1 Art. 14 Abs. 1 lit. e"


class fuer_verschollen_erklaert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person fuer verschollen erklaert wurde"
    reference = "SR 195.1 Art. 14 Abs. 1 lit. f"


class eintrag_wird_gestrichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Eintrag im Auslandschweizerregister gestrichen wird"
    reference = "SR 195.1 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        a = person('hat_wohnsitz_in_schweiz_begruendet', period)
        b = person('hat_schweizer_staatsangehoerigkeit_verloren', period)
        c = person('ist_minderjaehrig_ohne_bestaetigung', period)
        d = person('ist_verstorben', period)
        e = person('nicht_erreichbar', period)
        f = person('fuer_verschollen_erklaert', period)
        return a + b + c + d + e + f > 0
