"""SR 221.214.1 Art. 36b

Generated from: ch/221/fr/221.214.1.md

Criminal provision: intentional violation of aggressive advertising ban
punishable by fine up to 100,000 CHF.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lcc_publicite_agressive_intentionnelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Contravention intentionnelle a l'interdiction de publicite agressive"
    reference = "SR 221.214.1 Art. 36b"


class lcc_amende_max_publicite_agressive_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Amende maximale pour publicite agressive en CHF"
    reference = "SR 221.214.1 Art. 36b"

    def formula(person, period, parameters):
        return 100000.0
