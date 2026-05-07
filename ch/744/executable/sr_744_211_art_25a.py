"""SR 744.211 Art. 25a

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class gebuehren_nach_bav_verordnung_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gebühren richten sich nach der Gebührenverordnung BAV (SR 742.102)"
    reference = "SR 744.211 Art. 25a"

    def formula(person, period, parameters):
        # Art. 25a delegates fee determination entirely to the BAV Fee Ordinance
        # of 25 November 1998 (SR 742.102); this variable marks applicability
        return True
