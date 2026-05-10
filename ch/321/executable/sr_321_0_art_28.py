"""SR 321.0 Art. 28

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class geldstrafe_anzahl_tagessaetze(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Tagessaetze der Geldstrafe (3-180)"
    reference = "SR 321.0 Art. 28 Abs. 1"


class geldstrafe_tagessatz_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoehe eines Tagessatzes in Franken (in der Regel 30-3000, ausnahmsweise bis 10)"
    reference = "SR 321.0 Art. 28 Abs. 2"


class geldstrafe_tagessatz_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mindestwert eines Tagessatzes (in der Regel 30, ausnahmsweise 10 Franken)"
    reference = "SR 321.0 Art. 28 Abs. 2"
    default_value = 30.0


class geldstrafe_tagessatz_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstwert eines Tagessatzes (3000 Franken)"
    reference = "SR 321.0 Art. 28 Abs. 2"
    default_value = 3000.0


class geldstrafe_gesamtbetrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtbetrag der Geldstrafe (Anzahl Tagessaetze x Tagessatzbetrag)"
    reference = "SR 321.0 Art. 28"

    def formula(person, period, parameters):
        anzahl = person('geldstrafe_anzahl_tagessaetze', period)
        betrag = person('geldstrafe_tagessatz_betrag', period)
        return anzahl * betrag
