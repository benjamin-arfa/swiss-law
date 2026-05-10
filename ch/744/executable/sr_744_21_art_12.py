"""SR 744.21 Art. 12

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bundesgesetzgebung_motorfahrzeugverkehr_gilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Technische Ausrüstung und Strassenverkehr unterliegen der Bundesgesetzgebung über den Motorfahrzeugverkehr"
    reference = "SR 744.21 Art. 12"

    def formula(person, period, parameters):
        # Federal motor vehicle legislation applies by default to all vehicles on the road.
        # Exceptions defined elsewhere in SR 744.21 may override this.
        return True


class ausnahme_von_motorfahrzeugvorschriften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausnahme von den Vorschriften der Bundesgesetzgebung über den Motorfahrzeugverkehr gemäss SR 744.21"
    reference = "SR 744.21 Art. 12 Satz 2"

    def formula(person, period, parameters):
        # Exceptions are reserved as specified in SR 744.21.
        # This variable is false unless a specific exception article sets it true.
        return False


class technische_ausruestung_regelung_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anwendbare Regelung für technische Ausrüstung: Bundesgesetzgebung gilt, sofern keine Ausnahme nach SR 744.21 greift"
    reference = "SR 744.21 Art. 12"

    def formula(person, period, parameters):
        bundesrecht_gilt = person('bundesgesetzgebung_motorfahrzeugverkehr_gilt', period)
        ausnahme = person('ausnahme_von_motorfahrzeugvorschriften', period)
        return bundesrecht_gilt * ~ausnahme
