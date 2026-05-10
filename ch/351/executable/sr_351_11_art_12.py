"""SR 351.11 Art. 12

Generated from: ch/351/de/351.11.md
Cost charging rules for international legal assistance.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class auslagen_rechtshilfe_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtauslagen bei Ausfuehrung des Rechtshilfeersuchens in CHF"
    reference = "SR 351.11 Art. 12 Abs. 1"


class arbeitsaufwand_tage(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Arbeitsaufwand in Arbeitstagen"
    reference = "SR 351.11 Art. 12 Abs. 2"


class schweiz_erhaelt_unentgeltliche_rechtshilfe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schweiz kann im ersuchenden Staat Rechtshilfe unentgeltlich erwirken"
    reference = "SR 351.11 Art. 12 Abs. 2"


class darf_auslagen_rueckerstatten_lassen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Darf Rueckerstattung aller Auslagen vom ersuchenden Staat verlangen"
    reference = "SR 351.11 Art. 12 Abs. 1"

    def formula(person, period):
        # Schweizer Behoerden koennen immer Auslagen zurueckfordern
        return True + person('auslagen_rechtshilfe_chf', period) * 0


class darf_arbeitsaufwand_verrechnen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Darf Arbeitsaufwand dem ersuchenden Staat in Rechnung stellen"
    reference = "SR 351.11 Art. 12 Abs. 2"

    def formula(person, period):
        aufwand = person('arbeitsaufwand_tage', period)
        unentgeltlich = person('schweiz_erhaelt_unentgeltliche_rechtshilfe', period)
        # Nur wenn mehr als 1 ganzer Arbeitstag UND Schweiz keine kostenlose Rechtshilfe erhaelt
        return (aufwand > 1.0) * not_(unentgeltlich)


class rechnung_wird_gestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wird eine Rechnung an den ersuchenden Staat gestellt"
    reference = "SR 351.11 Art. 12 Abs. 3"

    def formula(person, period):
        auslagen = person('auslagen_rechtshilfe_chf', period)
        # Fuer Gesamtkosten unter 200 Franken wird in keinem Fall Rechnung gestellt
        return auslagen >= 200.0
