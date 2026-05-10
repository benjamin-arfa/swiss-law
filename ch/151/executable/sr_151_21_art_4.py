"""SR 151.21 Art. 4

Generated from: ch/151/de/151.21.md

Aufteilung der Unterstuetzungsbeitraege: 2/3 nichtschulisch, 1/3 schulisch.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesamtbetrag_projekte_dritter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtbetrag fuer Projekte Dritter (jaehrlicher Voranschlagskredit)"
    reference = "SR 151.21 Art. 4"


class anteil_nichtschulisch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil fuer Projekte im nichtschulischen Bereich (rund 2/3)"
    reference = "SR 151.21 Art. 4 Bst. a"

    def formula(person, period, parameters):
        gesamt = person('gesamtbetrag_projekte_dritter', period)
        return gesamt * 2 / 3


class anteil_schulisch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil fuer Projekte im schulischen Bereich (rund 1/3)"
    reference = "SR 151.21 Art. 4 Bst. b"

    def formula(person, period, parameters):
        gesamt = person('gesamtbetrag_projekte_dritter', period)
        return gesamt / 3
