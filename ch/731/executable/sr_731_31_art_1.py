"""SR 731.31 Art. 1

Generated from: ch/731/de/731.31.md

Purpose, subject matter and scope of the FiREVO.
Applies exclusively to electricity companies that are legal entities
under private law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_geltungsbereich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen faellt in den Geltungsbereich der FiREVO (SR 731.31 Art. 1 Abs. 3)"
    reference = "SR 731.31 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        """Art. 1 Abs. 3: Applies only to electricity companies that are
        private-law legal entities."""
        ist_elektrizitaetswirtschaft = person('ist_elektrizitaetswirtschaft', period)
        ist_privatrecht = person('ist_privatrechtlich', period)
        return ist_elektrizitaetswirtschaft * ist_privatrecht
