"""SR 443.1 Art. 24b

Generated from: ch/443/de/443.1.md

Investitionspflicht: Min 4% der Bruttoeinnahmen fuer unabhaengiges Schweizer
Filmschaffen. Ersatzabgabe wenn im 4-Jahres-Mittel nicht erreicht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bruttoeinnahmen_filmanbieter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bruttoeinnahmen des Film-/Fernsehdienst-Anbieters in CH (CHF)"
    reference = "SR 443.1 Art. 24b Abs. 1"


class aufwendungen_schweizer_filmschaffen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufwendungen fuer unabhaengiges Schweizer Filmschaffen (CHF)"
    reference = "SR 443.1 Art. 24b Abs. 1"


class investitionspflicht_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Geschuldeter Investitionsbetrag (4% der Bruttoeinnahmen)"
    reference = "SR 443.1 Art. 24b Abs. 1"

    def formula(person, period, parameters):
        einnahmen = person('bruttoeinnahmen_filmanbieter', period)
        return einnahmen * 0.04


class investitionspflicht_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Investitionspflicht erfuellt ist"
    reference = "SR 443.1 Art. 24b Abs. 1"

    def formula(person, period, parameters):
        pflicht = person('investitionspflicht_betrag', period)
        aufwendungen = person('aufwendungen_schweizer_filmschaffen', period)
        return aufwendungen >= pflicht
