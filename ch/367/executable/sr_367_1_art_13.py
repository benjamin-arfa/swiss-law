"""SR 367.1 Art. 13

Generated from: ch/367/de/367.1.md

Beschlussfassung in den Versammlungen und Ausschuessen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class ist_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Mitglied ein Kanton (im Gegensatz zu Bund/KSSD)"
    reference = "SR 367.1 Art. 13 Abs. 1"


class anzahl_anwesende_stimmen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl anwesende stimmberechtigte Stimmen in einer Sitzung"
    reference = "SR 367.1 Art. 13 Abs. 3"


class gesamtstimmen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtzahl der Stimmen im Organ"
    reference = "SR 367.1 Art. 13 Abs. 2"


class ist_strategische_versammlung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Handelt es sich um die strategische Versammlung"
    reference = "SR 367.1 Art. 13 Abs. 1"


# --- Computed variables ---

class stimmen_pro_mitglied(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Stimmen pro Mitglied"
    reference = "SR 367.1 Art. 13 Abs. 1"

    def formula(person, period):
        ist_strat_vers = person('ist_strategische_versammlung', period)
        ist_kt = person('ist_kanton', period)
        # In strategischer Versammlung: Kantone 2 Stimmen, EJPD/KSSD je 1
        # In allen anderen Organen: jedes Mitglied 1 Stimme
        return where(ist_strat_vers * ist_kt, 2, 1)


class beschlussfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist das Organ beschlussfaehig (mindestens Haelfte der Stimmen vertreten)"
    reference = "SR 367.1 Art. 13 Abs. 2"

    def formula(person, period):
        anwesend = person('anzahl_anwesende_stimmen', period)
        gesamt = person('gesamtstimmen', period)
        return anwesend >= (gesamt / 2)
