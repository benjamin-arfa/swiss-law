"""SR 744.10 Art. 11

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strassentransport_ohne_bewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tätigkeit als Strassentransportunternehmen ohne Zulassungsbewilligung"
    reference = "SR 744.10 Art. 11 Abs. 1-2"

    def formula(person, period, parameters):
        return person('strassentransport_taetig', period) * ~person('strassentransport_zulassungsbewilligung', period)


class strassentransport_taetig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person führt Tätigkeit als Strassentransportunternehmen im Personen- oder Güterverkehr aus"
    reference = "SR 744.10 Art. 11 Abs. 1"


class strassentransport_zulassungsbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person besitzt gültige Zulassungsbewilligung als Strassentransportunternehmen"
    reference = "SR 744.10 Art. 11 Abs. 1"


class strassentransport_handlung_vorsaetzlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Handlung wurde vorsätzlich begangen"
    reference = "SR 744.10 Art. 11 Abs. 1-2"


class strassentransport_bewilligung_widerhandlung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person handelt der Zulassungsbewilligung zuwider (vorsätzlich oder fahrlässig)"
    reference = "SR 744.10 Art. 11 Abs. 3"


class strassentransport_art8a_verstoss(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person verstösst gegen das Verbot nach Artikel 8a (vorsätzlich oder fahrlässig)"
    reference = "SR 744.10 Art. 11 Abs. 3bis"


class strassentransport_busse_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Höhe der Busse bei Übertretung nach SR 744.10 Art. 11 (in CHF)"
    reference = "SR 744.10 Art. 11"

    def formula(person, period, parameters):
        ohne_bewilligung = person('strassentransport_ohne_bewilligung', period)
        vorsaetzlich = person('strassentransport_handlung_vorsaetzlich', period)
        widerhandlung = person('strassentransport_bewilligung_widerhandlung', period)
        art8a_verstoss = person('strassentransport_art8a_verstoss', period)

        # Art. 11 Abs. 1: vorsätzlich ohne Bewilligung → Busse bis 100 000 CHF
        busse_abs1 = where(ohne_bewilligung * vorsaetzlich, 100_000.0, 0.0)

        # Art. 11 Abs. 2: fahrlässig ohne Bewilligung → Busse bis 50 000 CHF
        busse_abs2 = where(ohne_bewilligung * ~vorsaetzlich, 50_000.0, 0.0)

        # Art. 11 Abs. 3: Widerhandlung gegen Zulassungsbewilligung → Busse (kein Höchstbetrag spezifiziert)
        busse_abs3 = where(widerhandlung, 1.0, 0.0)  # applicability flag; amount set by court

        # Art. 11 Abs. 3bis: Verstoss gegen Verbot nach Art. 8a → Busse
        busse_abs3bis = where(art8a_verstoss, 1.0, 0.0)  # applicability flag; amount set by court

        return max_(busse_abs1, max_(busse_abs2, max_(busse_abs3, busse_abs3bis)))


class strassentransport_strafbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat eine strafbare Übertretung nach SR 744.10 Art. 11 begangen"
    reference = "SR 744.10 Art. 11"

    def formula(person, period, parameters):
        ohne_bewilligung = person('strassentransport_ohne_bewilligung', period)
        widerhandlung = person('strassentransport_bewilligung_widerhandlung', period)
        art8a_verstoss = person('strassentransport_art8a_verstoss', period)

        return ohne_bewilligung + widerhandlung + art8a_verstoss
