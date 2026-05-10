"""SR 952.02 Art. 3 — Nichtbanken

Generated from: ch/952/de/952.02.md

Koerperschaften und Anstalten des oeffentlichen Rechts sowie Kassen,
fuer die eine solche Koerperschaft vollumfaenglich haftet, gelten nicht
als Banken, auch wenn sie gewerbsmaessig Publikumseinlagen entgegennehmen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bankv_ist_oeffentlichrechtliche_koerperschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut ist Koerperschaft/Anstalt des oeffentlichen Rechts"
    reference = "SR 952.02 Art. 3"


class bankv_vollumfaenglich_gehaftet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Oeffentlichrechtliche Koerperschaft haftet vollumfaenglich"
    reference = "SR 952.02 Art. 3"


class bankv_gilt_als_nichtbank(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Institut gilt als Nichtbank nach Art. 3 BankV"
    reference = "SR 952.02 Art. 3"

    def formula(person, period, parameters):
        ist_koerperschaft = person('bankv_ist_oeffentlichrechtliche_koerperschaft', period)
        gehaftet = person('bankv_vollumfaenglich_gehaftet', period)
        return ist_koerperschaft * gehaftet
