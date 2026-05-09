"""SR 654.1 Art. 31 - Debut de l'obligation d'etablir la declaration

Generated from: ch/654/de/654.1.md

The obligation to prepare a CbC report arises with reporting tax periods
that begin at the earliest on the first day of the calendar year
following the entry into force of this law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity
import numpy as np

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class date_debut_periode_fiscale(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Date de debut de la periode fiscale de reporting"
    reference = "SR 654.1 Art. 31"


class obligation_declaration_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'obligation de declaration pays par pays est applicable pour cette periode fiscale"
    reference = "SR 654.1 Art. 31"

    def formula(self, period, parameters):
        # Law entered into force on 1 December 2017; obligation starts
        # for reporting periods beginning on or after 1 January 2018
        return period.start.year >= 2018
