"""SR 425.15 Art. 6

Generated from: ch/425/de/425.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dienstleistung_typ_a(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dienstleistung nach Art. 3 Bst. a (Gutachten, Studien, Stellungnahmen, Auskuenfte)"
    reference = "SR 425.15 Art. 6 Abs. 1"


class stundenansatz_minimum(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimaler Stundenansatz in CHF"
    reference = "SR 425.15 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        typ_a = person('dienstleistung_typ_a', period)
        return where(typ_a, 150.0, 100.0)


class stundenansatz_maximum(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Stundenansatz in CHF"
    reference = "SR 425.15 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        typ_a = person('dienstleistung_typ_a', period)
        return where(typ_a, 400.0, 200.0)


class interessenswert(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Interessenswert der Angelegenheit in CHF (fuer Weiterverrechnung an gewerbliche Empfaenger)"
    reference = "SR 425.15 Art. 6 Abs. 2"


class kosten_weiterverrechenbar_an_gewerblichen_empfaenger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kosten koennen an gewerblichen Empfaenger weiterverrechnet werden"
    reference = "SR 425.15 Art. 6 Abs. 2"


class stundenansatz_zuschlag_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zuschlag auf Stundenansaetze in Prozent bei Weiterverrechnung an gewerbliche Empfaenger"
    reference = "SR 425.15 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        weiterverrechenbar = person('kosten_weiterverrechenbar_an_gewerblichen_empfaenger', period)
        wert = person('interessenswert', period)
        # bis 500'000: max 40%; 500'000-1'000'000: 70%; ueber 1'000'000: 100%
        zuschlag = where(wert > 1000000, 100.0,
                   where(wert > 500000, 70.0, 40.0))
        return where(weiterverrechenbar, zuschlag, 0.0)
