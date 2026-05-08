"""SR 371 Art. 13 - Rechtswirkungen der Aufhebung (Legal Effects of Annulment)

Generated from: ch/de/371.md
The annulment of convictions does not give rise to any claim for damages
or satisfaction, neither for the sentences nor for ancillary penalties
or indirect consequences.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class anspruch_schadenersatz_rehabilitierung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf Schadenersatz oder Genugtuung aus der Aufhebung von Strafurteilen"
    reference = "SR 371 Art. 13"

    def formula(person, period, parameters):
        # Kein Anspruch auf Schadenersatz oder Genugtuung
        return False
