"""SR 151.34 Art. 5

Generated from: ch/151/de/151.34.md

Zugang mit Hilfsmitteln: Maximalgewicht und -dimensionen fuer Rollstuehle.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rollstuhl_gesamtgewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtgewicht des Rollstuhls in kg"
    reference = "SR 151.34 Art. 5 Abs. 1 Bst. a"


class rollstuhl_laenge_mm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Laenge des Rollstuhls in mm"
    reference = "SR 151.34 Art. 5 Abs. 1 Bst. a Ziff. 1"


class rollstuhl_breite_mm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Breite des Rollstuhls in mm"
    reference = "SR 151.34 Art. 5 Abs. 1 Bst. a Ziff. 2"


class rollstuhl_zugang_gewaehrleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Zugang fuer den Rollstuhl gewaehrleistet sein muss"
    reference = "SR 151.34 Art. 5 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        gewicht = person('rollstuhl_gesamtgewicht_kg', period)
        laenge = person('rollstuhl_laenge_mm', period)
        breite = person('rollstuhl_breite_mm', period)
        # Max 300 kg, Laenge 1200+50=1250 mm, Breite 700+100=800 mm
        return (gewicht <= 300) * (laenge <= 1250) * (breite <= 800)
