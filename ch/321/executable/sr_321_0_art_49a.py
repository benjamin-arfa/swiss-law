"""SR 321.0 Art. 49a

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_auslaender(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist Auslaender (kein Schweizer Buerger)"
    reference = "SR 321.0 Art. 49a Abs. 1"


class verurteilung_wegen_katalogtat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person wird wegen einer Katalogtat nach Art. 49a Abs. 1 verurteilt"
    reference = "SR 321.0 Art. 49a Abs. 1"


class schwerer_persoenlicher_haertefall(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Landesverweisung bewirkt einen schweren persoenlichen Haertefall"
    reference = "SR 321.0 Art. 49a Abs. 2"


class oeffentliches_interesse_ueberwiegt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das oeffentliche Interesse an der Landesverweisung ueberwiegt"
    reference = "SR 321.0 Art. 49a Abs. 2"


class obligatorische_landesverweisung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Obligatorische Landesverweisung (5-15 Jahre)"
    reference = "SR 321.0 Art. 49a Abs. 1"

    def formula(person, period, parameters):
        auslaender = person('ist_auslaender', period)
        katalogtat = person('verurteilung_wegen_katalogtat', period)
        haertefall = person('schwerer_persoenlicher_haertefall', period)
        oeffentlich = person('oeffentliches_interesse_ueberwiegt', period)

        # Grundsatz: obligatorische Landesverweisung
        grundsatz = auslaender * katalogtat

        # Ausnahme: Haertefall, wenn oeffentliches Interesse nicht ueberwiegt
        ausnahme = haertefall * not_(oeffentlich)

        return grundsatz * not_(ausnahme)


class landesverweisung_dauer_min_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestdauer der obligatorischen Landesverweisung (5 Jahre)"
    reference = "SR 321.0 Art. 49a Abs. 1"
    default_value = 5


class landesverweisung_dauer_max_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Hoechstdauer der obligatorischen Landesverweisung (15 Jahre)"
    reference = "SR 321.0 Art. 49a Abs. 1"
    default_value = 15
