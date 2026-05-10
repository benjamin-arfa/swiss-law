"""SR 170.321 Art. 7

Generated from: ch/170/de/170.321.md

Ermächtigung bei politischem Delikt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bundesrat_beschliesst_strafverfolgung_politisches_delikt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bundesrat beschliesst die Strafverfolgung bei politischem Delikt (Art. 7 VV-VG)"
    reference = "SR 170.321, Art. 7"


class ejpd_ermaechtigung_gilt_als_erteilt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Ermächtigung des EJPD gilt als erteilt (Art. 7 VV-VG)"
    reference = "SR 170.321, Art. 7"

    def formula(person, period, parameters):
        return person('bundesrat_beschliesst_strafverfolgung_politisches_delikt', period)
