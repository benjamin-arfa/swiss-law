"""SR 451.1 Art. 5

Generated from: ch/451/de/451.1.md
Beitragsbemessung - Hoechstbeitraege fuer Denkmalpflege, Archaeologie, Ortsbildschutz
und Schutz der historischen Verkehrswege.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bedeutung_objekt(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Bedeutung des zu schuetzenden Objekts (national, regional, lokal)"
    reference = "SR 451.1 Art. 5 Abs. 1 Bst. a"
    default_value = "lokal"


class beitragsberechtigte_aufwendungen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beitragsberechtigte Aufwendungen in CHF"
    reference = "SR 451.1 Art. 6"


class ist_denkmalpflege_bereich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bereich Denkmalpflege, Archaeologie, Ortsbildschutz oder historische Verkehrswege"
    reference = "SR 451.1 Art. 5 Abs. 3"


class unentbehrliche_massnahmen_nicht_finanzierbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unerlaessliche Massnahmen koennen andernfalls nicht finanziert werden"
    reference = "SR 451.1 Art. 5 Abs. 4"


class hoechstbeitrag_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstbeitrag in Prozent der beitragsberechtigten Aufwendungen"
    reference = "SR 451.1 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        bedeutung = person('bedeutung_objekt', period)
        ist_denkmalpflege = person('ist_denkmalpflege_bereich', period)
        ausnahme = person('unentbehrliche_massnahmen_nicht_finanzierbar', period)

        # Standardsaetze nach Art. 5 Abs. 3
        prozent_national = where(ist_denkmalpflege, 25.0, 0.0)
        prozent_regional = where(ist_denkmalpflege, 20.0, 0.0)
        prozent_lokal = where(ist_denkmalpflege, 15.0, 0.0)

        prozent = select(
            [bedeutung == 'national', bedeutung == 'regional', bedeutung == 'lokal'],
            [prozent_national, prozent_regional, prozent_lokal],
        )

        # Ausnahme nach Art. 5 Abs. 4: bis 45%
        return where(ausnahme * ist_denkmalpflege, min_(prozent + 20.0, 45.0), prozent)


class finanzhilfe_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Berechneter Finanzhilfebetrag in CHF"
    reference = "SR 451.1 Art. 5"

    def formula(person, period, parameters):
        aufwendungen = person('beitragsberechtigte_aufwendungen', period)
        prozent = person('hoechstbeitrag_prozent', period)
        return aufwendungen * prozent / 100.0
