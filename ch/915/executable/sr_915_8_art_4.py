"""SR 915.8 Art. 4

Generated from: ch/915/de/915.8.md

FKINV - Art. 4: Gesuchseinreichung.
Das Gesuch ist beim BLW einzureichen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class fkinv_gesuch_beim_blw_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesuch um Finanzhilfen ist beim BLW eingereicht (Art. 4 Abs. 1)"
    reference = "SR 915.8 Art. 4 Abs. 1"
