"""SR 513.52 Art. 5

Generated from: ch/513/de/513.52.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class rkd_grundausbildung_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der RKD Grundausbildung in Tagen (Art. 5 Abs. 1 SR 513.52)"
    reference = "SR 513.52 Art. 5"

    def formula(person, period, parameters):
        # Rekrutenschule RKD: allgemeine Grundausbildung (19 Tage)
        # + funktionsbezogene Grundausbildung (19 Tage) = 38 Tage
        return 19 + 19


class rkd_hat_kaderfunktion(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat eine Kaderfunktion im RKD"


class rkd_geleistete_ausbildungsdienste(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl geleisteter Ausbildungsdienste der Formationen"


class rkd_mindestausbildungsdienste_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mindestanzahl Ausbildungsdienste erfuellt (Art. 5 Abs. 2-3 SR 513.52)"
    reference = "SR 513.52 Art. 5"

    def formula(person, period, parameters):
        hat_kaderfunktion = person('rkd_hat_kaderfunktion', period)
        geleistete = person('rkd_geleistete_ausbildungsdienste', period)
        # Abs. 2: mindestens 6 Ausbildungsdienste
        # Abs. 3: Kader muss alle vorgeschriebenen leisten (hier als >= 6 modelliert)
        return geleistete >= 6
