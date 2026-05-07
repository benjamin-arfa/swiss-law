"""SR 441.1 Art. 1

Generated from: ch/441/de/441.1.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class gegenstand_spg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gegenstand des Sprachengesetzes — regelt Amtssprachen, Verständigung, mehrsprachige Kantone, Rätoromanisch/Italienisch"
    reference = "SR 441.1, Art. 1"

    def formula(self, period, parameters):
        # Art. 1 is purely declaratory — defines the subject matter of the law
        # Always true if the law applies
        return True
