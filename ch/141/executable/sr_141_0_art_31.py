"""SR 141.0 Art. 31 - Minderjaehrige Kinder

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_des_kindes(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter des minderjaehrigen Kindes in Jahren"
    reference = "SR 141.0 Art. 31"


class kind_muss_eigenen_willen_erklaeren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das minderjaehrige Kind muss seinen eigenen Willen auf Erwerb des Schweizer Buergerrechts schriftlich erklaeren"
    reference = "SR 141.0 Art. 31 Abs. 2"

    def formula(self, period, parameters):
        alter = self('alter_des_kindes', period)
        return alter >= 16
