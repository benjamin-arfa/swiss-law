"""SR 251.5 Art. 3

Generated from: ch/251/de/251.5.md

Basisbetrag: Der Basisbetrag der Sanktion bildet je nach Schwere und Art
des Verstosses bis zu 10 Prozent des Umsatzes der letzten drei Geschaeftsjahre
auf den relevanten Maerkten in der Schweiz.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class umsatz_relevante_maerkte_schweiz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Umsatz auf den relevanten Maerkten in der Schweiz in den letzten drei Geschaeftsjahren"
    reference = "SR 251.5 Art. 3"


class schwere_verstoss_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prozentsatz je nach Schwere und Art des Verstosses (0 bis 10)"
    reference = "SR 251.5 Art. 3"


class sanktion_basisbetrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Basisbetrag der Sanktion (bis zu 10% des Umsatzes auf relevanten Maerkten)"
    reference = "SR 251.5 Art. 3"

    def formula(person, period, parameters):
        umsatz = person('umsatz_relevante_maerkte_schweiz', period)
        prozent = person('schwere_verstoss_prozent', period)
        # Prozent darf maximal 10 sein
        effektiv_prozent = min_(prozent, 10)
        return umsatz * effektiv_prozent / 100
