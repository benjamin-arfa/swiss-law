"""SR 857.5 Art. 1

Generated from: ch/857/de/857.5.md

Schwangerschaftsberatungsstellen (Pregnancy counseling centers).

Art. 1 Abs. 1: Persons directly involved in a pregnancy have a right to
free counseling and assistance.
Art. 1 Abs. 3-4: Cantons must establish counseling centers with sufficient
staff and financial resources.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schwangerschaftsberatung_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf unentgeltliche Schwangerschaftsberatung und Hilfe"
    reference = "SR 857.5 Art. 1 Abs. 1"

    def formula_1984(person, period, parameters):
        return person('schwangerschaft_unmittelbar_beteiligt', period)


class schwangerschaft_unmittelbar_beteiligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ist die Person unmittelbar an einer Schwangerschaft beteiligt?"
    reference = "SR 857.5 Art. 1 Abs. 1"
