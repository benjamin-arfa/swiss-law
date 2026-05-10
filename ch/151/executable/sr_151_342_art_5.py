"""SR 151.342 Art. 5

Generated from: ch/151/de/151.342.md

Kundeninformation und -kommunikation: Mindestgroessen fuer
Buchstaben und Piktogramme, Montagehoehe.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lesedistanz_meter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Lesedistanz in Metern (gemessen auf dem Sehstrahl)"
    reference = "SR 151.342 Art. 5 Abs. 4"


class mindestgroesse_grossbuchstaben_mm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestgroesse der Grossbuchstaben in mm"
    reference = "SR 151.342 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        distanz = person('lesedistanz_meter', period)
        return distanz * 25


class mindestgroesse_piktogramme_mm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestgroesse der Piktogramme und Gleisangaben in mm"
    reference = "SR 151.342 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        distanz = person('lesedistanz_meter', period)
        return distanz * 60


class max_hoehe_aushangfahrplan_cm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Hoehe der obersten Inhaltszeile von Aushangfahrplaenen (160 cm)"
    reference = "SR 151.342 Art. 5 Abs. 5"

    def formula(person, period, parameters):
        return 160.0
