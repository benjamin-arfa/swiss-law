"""SR 142.318 Art. 12

Generated from: ch/142/de/142.318.md

Inkrafttreten und Geltungsdauer: Verordnung tritt am 2. April 2020 in Kraft,
Art. 4-6 am 6. April 2020. Mehrfach verlaengert, zuletzt bis 30. Juni 2024.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class covid19_verordnung_asyl_in_kraft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Covid-19-Verordnung Asyl in Kraft ist"
    reference = "SR 142.318 Art. 12"

    def formula_2020_04(person, period, parameters):
        return True


class covid19_verordnung_art4_6_in_kraft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Artikel 4-6 der Covid-19-Verordnung Asyl in Kraft sind"
    reference = "SR 142.318 Art. 12 Abs. 2"

    def formula_2020_04(person, period, parameters):
        # Art. 4-6 treten am 6. April 2020 in Kraft
        return True
