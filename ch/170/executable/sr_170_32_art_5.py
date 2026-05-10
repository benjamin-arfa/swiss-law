"""SR 170.32 Art. 5

Generated from: ch/170/de/170.32.md

Schadenersatz bei Tötung oder Körperverletzung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class toetung_eingetreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der geschädigte Mensch ist gestorben (Art. 5 Abs. 1 VG)"
    reference = "SR 170.32, Art. 5 Abs. 1"


class koerperverletzung_eingetreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Körperverletzung ist eingetreten (Art. 5 Abs. 2 VG)"
    reference = "SR 170.32, Art. 5 Abs. 2"


class bestattungskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Entstandene Bestattungskosten in CHF (Art. 5 Abs. 1 VG)"
    reference = "SR 170.32, Art. 5 Abs. 1"


class heilungskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten der versuchten Heilung in CHF (Art. 5 Abs. 1 VG)"
    reference = "SR 170.32, Art. 5 Abs. 1"


class versorger_verloren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Andere Personen haben durch die Tötung ihren Versorger verloren (Art. 5 Abs. 1 VG)"
    reference = "SR 170.32, Art. 5 Abs. 1"


class versorgerschaden(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Versorgerschaden in CHF (Art. 5 Abs. 1 VG)"
    reference = "SR 170.32, Art. 5 Abs. 1"


class arbeitsunfaehigkeit_grad(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Grad der Arbeitsunfähigkeit (0.0 bis 1.0) (Art. 5 Abs. 2 VG)"
    reference = "SR 170.32, Art. 5 Abs. 2"


class schadenersatz_toetung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schadenersatz bei Tötung in CHF (Art. 5 Abs. 1 VG)"
    reference = "SR 170.32, Art. 5 Abs. 1"

    def formula(person, period, parameters):
        toetung = person('toetung_eingetreten', period)
        bestattung = person('bestattungskosten', period)
        heilung = person('heilungskosten', period)
        versorger = person('versorger_verloren', period)
        versorgerschaden_betrag = person('versorgerschaden', period)
        return toetung * (bestattung + heilung + versorger * versorgerschaden_betrag)


class schadenersatz_koerperverletzung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schadenersatz bei Körperverletzung in CHF (Art. 5 Abs. 2 VG)"
    reference = "SR 170.32, Art. 5 Abs. 2"

    def formula(person, period, parameters):
        verletzung = person('koerperverletzung_eingetreten', period)
        heilung = person('heilungskosten', period)
        return verletzung * heilung
