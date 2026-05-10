"""SR 817.041 Art. 1

Generated from: ch/817/de/817.041.md

Einfuhrverbot für bestimmte, nicht sichere Lebensmittel.
The import of food products listed in the annex is prohibited.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lebensmittel_einfuhr_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ist die Einfuhr des Lebensmittels verboten?"
    reference = "SR 817.041 Art. 1"

    def formula_2020_10(person, period, parameters):
        return person('lebensmittel_auf_verbotsliste', period)


class lebensmittel_auf_verbotsliste(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ist das Lebensmittel im Anhang der Verordnung aufgeführt?"
    reference = "SR 817.041 Art. 1"
