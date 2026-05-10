"""SR 744.103 Art. 6

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wohnsitz_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat Wohnsitz in der Schweiz"
    reference = "SR 744.103 Art. 6 Abs. 3"

    def formula(person, period, parameters):
        return person('wohnsitz_schweiz', period)


class arbeitsort_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat Arbeitsort in der Schweiz"
    reference = "SR 744.103 Art. 6 Abs. 3"

    def formula(person, period, parameters):
        return person('arbeitsort_schweiz', period)


class fachausweis_wohnsitz_oder_arbeitsort_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person erfüllt Wohnsitz- oder Arbeitsortbedingung für Fachausweis (Art. 6 Abs. 3)"
    reference = "SR 744.103 Art. 6 Abs. 3"

    def formula(person, period, parameters):
        # Fachausweis nur an Personen mit Wohnsitz oder Arbeitsort in der Schweiz
        hat_wohnsitz = person('wohnsitz_in_schweiz', period)
        hat_arbeitsort = person('arbeitsort_in_schweiz', period)
        return hat_wohnsitz + hat_arbeitsort


class berechtigt_zur_pruefungszulassung_art6(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist zur Prüfung zum Nachweis der fachlichen Eignung zuzulassen (SR 744.103 Art. 6)"
    reference = "SR 744.103 Art. 6"

    def formula(person, period, parameters):
        # Art. 6 Abs. 3: Fachausweis wird nur ausgestellt an Personen
        # mit Wohnsitz oder Arbeitsort in der Schweiz
        wohnsitz_oder_arbeitsort = person('fachausweis_wohnsitz_oder_arbeitsort_erfuellt', period)
        return wohnsitz_oder_arbeitsort


class pruefungsgebuehr_genehmigungspflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Prüfungsgebühr ist vom BAV zu genehmigen (Art. 6 Abs. 5)"
    reference = "SR 744.103 Art. 6 Abs. 5"

    def formula(person, period, parameters):
        # Art. 6 Abs. 5: Prüfungsgebühr ist immer genehmigungspflichtig durch das BAV
        return True
