"""SR 711.4 Art. 7

Generated from: ch/711/de/711.4.md

Occupational pension (berufliche Vorsorge) for commission members.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class schaetzungskommission_vorsorge_pflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Versicherungspflicht berufliche Vorsorge fuer Kommissionsmitglied"
    reference = "SR 711.4 Art. 7"

    def formula(person, period, parameters):
        """Art. 7: If BVG insurance obligation is met, members are insured.

        Full-time members: under Vorsorgereglement Bund (SR 172.220.141.1)
        Part-time members: under Honorarbeziehende Reglement (SR 172.220.141.2)
        """
        # Prerequisite: BVG insurance obligation must be met
        bvg_pflicht = person('bvg_versicherungspflicht', period)
        return bvg_pflicht
