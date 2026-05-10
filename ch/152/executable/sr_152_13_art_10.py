"""SR 152.13 Art. 10 - Einsichtnahme nach Ablauf der Schutzfrist (Access After Protection Period)

Generated from: ch/152/de/152.13.md

After expiry of the protection period, any person may access the archived material.
Access must take place on the premises of the Federal Administrative Court.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einsichtnahme_nach_schutzfrist_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Einsichtnahme nach Ablauf der Schutzfrist gewaehrt wird"
    reference = "SR 152.13 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        abgelaufen = person('schutzfrist_abgelaufen_bvger', period)
        verlaengert = person('schutzfrist_verlaengert_bvger', period)
        return abgelaufen * (1 - verlaengert)
