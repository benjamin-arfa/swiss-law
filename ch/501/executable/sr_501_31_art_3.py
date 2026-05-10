"""SR 501.31 Art. 3 - Leitung des KSD

Generated from: ch/501/de/501.31.md

Die Leitung des KSD obliegt dem Bundesamt fuer Bevoelkerungsschutz (BABS).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ksd_leitung_durch_babs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Leitung des KSD dem BABS obliegt"
    reference = "SR 501.31 Art. 3"

    def formula(person, period, parameters):
        return True
