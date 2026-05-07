"""SR 651.1 Art. 18 - Frais

Generated from: ch/651/fr/651.1.md

Costs: requests are executed without fees. The FTA may charge costs
in exceptional cases when costs are exceptionally high and the
inappropriate behavior of the person contributed significantly.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class frais_ampleur_exceptionnelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Les frais atteignent une ampleur exceptionnelle"
    reference = "SR 651.1 Art. 18 al. 2 let. a"


class comportement_inapproprie_personne(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le comportement inapproprie de la personne a notablement contribue a engendrer ces frais"
    reference = "SR 651.1 Art. 18 al. 2 let. b"


class frais_factures_personne(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC peut facturer les frais a la personne concernee ou au detenteur des renseignements"
    reference = "SR 651.1 Art. 18 al. 2"

    def formula(self, period, parameters):
        exceptionnels = self('frais_ampleur_exceptionnelle', period)
        comportement = self('comportement_inapproprie_personne', period)
        # Both conditions must be met (cumulative)
        return exceptionnels * comportement
