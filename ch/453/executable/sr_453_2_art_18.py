"""SR 453.2 Art. 18

Generated from: ch/453/de/453.2.md
Gebuehren - 60 Franken pro Sendung fuer Pruefung vorangemeldeter Sendungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_vorangemeldete_sendungen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl vorangemeldeter Sendungen im Jahr"
    reference = "SR 453.2 Art. 18 Abs. 2"


class gebuehren_sendungspruefung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehren fuer Pruefung vorangemeldeter Sendungen in CHF"
    reference = "SR 453.2 Art. 18 Abs. 2"

    def formula(person, period, parameters):
        anzahl = person('anzahl_vorangemeldete_sendungen', period)
        return anzahl * 60.0
