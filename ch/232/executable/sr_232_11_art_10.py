"""SR 232.11 Art. 10

Generated from: ch/232/de/232.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class marke_hinterlegungsdatum_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr des Hinterlegungsdatums der Marke"
    reference = "SR 232.11 Art. 10 Abs. 1"


class marke_letzte_verlaengerung_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der letzten Verlängerung der Markeneintragung"
    reference = "SR 232.11 Art. 10 Abs. 2"


class marke_gueltigkeitsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gültigkeitsdauer der Markeneintragung in Jahren"
    reference = "SR 232.11 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        # Die Eintragung ist während zehn Jahren gültig
        return person.filled_array(10)


class marke_verlaengerungsantrag_gestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verlängerungsantrag wurde gestellt"
    reference = "SR 232.11 Art. 10 Abs. 2"


class marke_verlaengerungsgebuehr_bezahlt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verlängerungsgebühr wurde bezahlt"
    reference = "SR 232.11 Art. 10 Abs. 2"


class marke_eintragung_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Markeneintragung ist im aktuellen Jahr gültig"
    reference = "SR 232.11 Art. 10"

    def formula(person, period, parameters):
        hinterlegung = person('marke_hinterlegungsdatum_jahr', period)
        letzte_verlaengerung = person('marke_letzte_verlaengerung_jahr', period)
        aktuelles_jahr = period.start.year
        # Gültig für 10 Jahre ab Hinterlegung oder letzter Verlängerung
        basis_jahr = max_(hinterlegung, letzte_verlaengerung)
        return (aktuelles_jahr - basis_jahr) <= 10
