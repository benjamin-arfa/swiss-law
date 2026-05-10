"""SR 351.93 Art. 21

Generated from: ch/351/de/351.93.md
Conditions for applying US procedural law during hearings in Switzerland.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class befragte_person_ist_amerikaner(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zu befragende Person besitzt amerikanische Staatsangehoerigkeit"
    reference = "SR 351.93 Art. 21 Abs. 1 lit. a"


class befragte_person_ist_schweizer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zu befragende Person ist zugleich Schweizer Buerger"
    reference = "SR 351.93 Art. 21 Abs. 1 lit. a"


class alle_beteiligten_stimmen_zu(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Alle Beteiligten stimmen der Anwendung US-Rechts schriftlich zu"
    reference = "SR 351.93 Art. 21 Abs. 1 lit. b"


class keine_wesentlichen_nachteile(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuer die Beteiligten sind keine wesentlichen Nachteile zu befuerchten"
    reference = "SR 351.93 Art. 21 Abs. 1 lit. b"


class gegenstand_wesentlich_fuer_verfahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gegenstand der Einvernahme ist wesentlich fuer den Ausgang des US-Verfahrens"
    reference = "SR 351.93 Art. 21 Abs. 2 lit. a"


class ch_protokoll_nicht_zulaessig_in_usa(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Protokoll nach CH-Recht wuerde vor US-Gericht als Beweis nicht zugelassen"
    reference = "SR 351.93 Art. 21 Abs. 2 lit. b"


class us_verfahrensrecht_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Amerikanisches Verfahrensrecht darf bei Einvernahme angewendet werden"
    reference = "SR 351.93 Art. 21"

    def formula(person, period):
        amerikaner = person('befragte_person_ist_amerikaner', period)
        schweizer = person('befragte_person_ist_schweizer', period)
        alle_zu = person('alle_beteiligten_stimmen_zu', period)
        keine_nachteile = person('keine_wesentlichen_nachteile', period)
        wesentlich = person('gegenstand_wesentlich_fuer_verfahren', period)
        nicht_zulaessig = person('ch_protokoll_nicht_zulaessig_in_usa', period)

        # Abs. 1 lit. a: Amerikaner und nicht zugleich Schweizer
        fall_a = amerikaner * not_(schweizer)

        # Abs. 1 lit. b: alle stimmen zu und keine Nachteile
        fall_b = alle_zu * keine_nachteile

        # Abs. 2: wesentlich und CH-Protokoll nicht zulaessig
        fall_c = wesentlich * nicht_zulaessig

        return fall_a + fall_b + fall_c
