"""SR 161.1 Art. 2

Generated from: ch/161/de/161.1.md

Ausschluss vom Stimmrecht: Personen unter umfassender Beistandschaft
oder durch vorsorgebeauftragte Person vertreten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unter_umfassender_beistandschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person wegen dauernder Urteilsunfaehigkeit unter umfassender Beistandschaft steht"
    reference = "SR 161.1 Art. 2"


class durch_vorsorgebeauftragte_vertreten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person durch eine vorsorgebeauftragte Person vertreten wird"
    reference = "SR 161.1 Art. 2"


class vom_stimmrecht_ausgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person vom Stimmrecht ausgeschlossen ist"
    reference = "SR 161.1 Art. 2"

    def formula(person, period, parameters):
        beistandschaft = person('unter_umfassender_beistandschaft', period)
        vorsorge = person('durch_vorsorgebeauftragte_vertreten', period)
        return beistandschaft + vorsorge > 0
