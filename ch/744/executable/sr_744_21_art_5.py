"""SR 744.21 Art. 5

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_744_21_art_5_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.21 Art. 5 - Aufgehoben (Bahnreform 2)"
    reference = "SR 744.21 Art. 5"

    def formula(person, period, parameters):
        # Art. 5 was repealed by BG vom 20. März 2009 über die Bahnreform 2,
        # effective 1 January 2010 (AS 2009 5597 5629)
        return period.start.year < 2010
