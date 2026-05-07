"""SR 654.1 Art. 12 - Sanction administrative en cas de defaut

Generated from: ch/654/fr/654.1.md

Administrative sanction: CHF 200 per day of delay, up to
CHF 50,000 total.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class jours_retard_declaration(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Nombre de jours de retard entre l'expiration du delai et la reception de la declaration"
    reference = "SR 654.1 Art. 12"


class sanction_administrative_retard_declaration(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Montant de la sanction administrative pour defaut de declaration pays par pays (CHF)"
    reference = "SR 654.1 Art. 12"

    def formula(self, period, parameters):
        jours = self('jours_retard_declaration', period)
        montant_par_jour = 200.0
        plafond = 50_000.0
        montant_brut = jours * montant_par_jour
        return min_(montant_brut, plafond)
