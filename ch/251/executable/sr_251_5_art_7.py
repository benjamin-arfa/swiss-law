"""SR 251.5 Art. 7

Generated from: ch/251/de/251.5.md

Maximale Sanktion: Die Sanktion betraegt in keinem Fall mehr als
10 Prozent des in den letzten drei Geschaeftsjahren in der Schweiz
erzielten Umsatzes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class umsatz_schweiz_drei_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtumsatz des Unternehmens in der Schweiz in den letzten drei Geschaeftsjahren"
    reference = "SR 251.5 Art. 7"


class sanktion_endgueltig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Endgueltige Sanktion nach Anwendung des Maximums von 10% des Schweizer Umsatzes"
    reference = "SR 251.5 Art. 7"

    def formula(person, period, parameters):
        betrag = person('sanktion_nach_mildernd', period)
        umsatz = person('umsatz_schweiz_drei_jahre', period)
        maximum = umsatz * 0.10
        return min_(betrag, maximum)
