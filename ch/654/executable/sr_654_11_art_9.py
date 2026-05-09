"""SR 654.11 Art. 9 - Antraege auf Aussetzung des automatischen Austauschs

Generated from: ch/654/de/654.11.md

Requests for suspension of the automatic exchange of CbC reports with a
partner state must be addressed to the State Secretariat for
International Finance (SIF).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class antrag_aussetzung_an_sif_gerichtet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Antrag auf Aussetzung wurde an das Staatssekretariat fuer internationale Finanzfragen gerichtet"
    reference = "SR 654.11 Art. 9"
