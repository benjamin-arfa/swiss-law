"""SR 981 Art. 10

Generated from: ch/de/981.md

Administrative and legal assistance: federal and cantonal authorities
and organizations performing administrative tasks are obligated to
provide free assistance.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class amts_und_rechtshilfe_verpflichtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Behoerden des Bundes und der Kantone zur unentgeltlichen Amts- und Rechtshilfe verpflichtet sind"
    reference = "SR 981 Art. 10"

    def formula(person, period, parameters):
        return True
