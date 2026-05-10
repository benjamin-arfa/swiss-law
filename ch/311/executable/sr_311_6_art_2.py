"""SR 311.6 Art. 2

Generated from: ch/311/de/311.6.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesicht_verhuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat die Person ihr Gesicht so verhuellt, dass die Gesichtszuege nicht erkennbar sind"
    reference = "SR 311.6 Art. 2 Abs. 1"


class verhuelllung_in_sakralstaette(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verhuelllung in Sakralstaetten"
    reference = "SR 311.6 Art. 2 Abs. 2 lit. a"


class verhuelllung_gesundheitsschutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verhuelllung zum Schutz oder zur Wiederherstellung der Gesundheit"
    reference = "SR 311.6 Art. 2 Abs. 2 lit. b"


class verhuelllung_persoenliche_sicherheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verhuelllung zur Gewaehrleistung der persoenlichen Sicherheit"
    reference = "SR 311.6 Art. 2 Abs. 2 lit. c"


class verhuelllung_klimaschutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verhuelllung zum Schutz vor klimatischen Bedingungen"
    reference = "SR 311.6 Art. 2 Abs. 2 lit. d"


class verhuelllung_brauchtum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verhuelllung zur Pflege des einheimischen Brauchtums"
    reference = "SR 311.6 Art. 2 Abs. 2 lit. e"


class verhuelllung_kuenstlerisch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verhuelllung bei kuenstlerischen und unterhaltenden Darbietungen"
    reference = "SR 311.6 Art. 2 Abs. 2 lit. f"


class verhuelllung_werbezwecke(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verhuelllung zu Werbezwecken"
    reference = "SR 311.6 Art. 2 Abs. 2 lit. g"


class verhuelllung_behoerdlich_bewilligt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verhuelllung behoerdlich bewilligt (Art. 2 Abs. 3)"
    reference = "SR 311.6 Art. 2 Abs. 3"


class verhuelllung_ausnahme_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Liegt eine Ausnahme vom Verhuellungsverbot vor"
    reference = "SR 311.6 Art. 2 Abs. 2-3"

    def formula(person, period, parameters):
        sakral = person('verhuelllung_in_sakralstaette', period)
        gesundheit = person('verhuelllung_gesundheitsschutz', period)
        sicherheit = person('verhuelllung_persoenliche_sicherheit', period)
        klima = person('verhuelllung_klimaschutz', period)
        brauchtum = person('verhuelllung_brauchtum', period)
        kunst = person('verhuelllung_kuenstlerisch', period)
        werbung = person('verhuelllung_werbezwecke', period)
        bewilligt = person('verhuelllung_behoerdlich_bewilligt', period)
        return sakral + gesundheit + sicherheit + klima + brauchtum + kunst + werbung + bewilligt > 0


class gesichtsverhuelllung_verboten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Gesichtsverhuelllung verboten (Art. 2 Abs. 1, keine Ausnahme)"
    reference = "SR 311.6 Art. 2"

    def formula(person, period, parameters):
        verhuellt = person('gesicht_verhuellt', period)
        ausnahme = person('verhuelllung_ausnahme_anwendbar', period)
        anwendbar = person('bvvg_anwendbar', period)
        return verhuellt * not_(ausnahme) * anwendbar
