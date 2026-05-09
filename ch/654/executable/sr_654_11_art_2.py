"""SR 654.11 Art. 2 - Wahlmoeglichkeiten

Generated from: ch/654/de/654.11.md

Where the OECD guidelines provide options for the CbC report,
these may be exercised by each reporting entity.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class oecd_wahlmoeglichkeit_genutzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der berichtende Rechtstraeger hat eine OECD-Wahlmoeglichkeit in Anspruch genommen"
    reference = "SR 654.11 Art. 2"
