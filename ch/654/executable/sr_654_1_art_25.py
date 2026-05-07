"""SR 654.1 Art. 25 - Declaration inexacte ou incomplete

Generated from: ch/654/fr/654.1.md

Penalty for intentionally providing inaccurate or incomplete
CbC reports: fine up to CHF 100,000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class declaration_intentionnellement_inexacte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'entite a donne intentionnellement des indications inexactes ou incompletes dans la declaration"
    reference = "SR 654.1 Art. 25 al. 1"


class amende_declaration_inexacte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Montant de l'amende pour declaration inexacte ou incomplete (CHF, max 100'000)"
    reference = "SR 654.1 Art. 25 al. 1"


class amende_maximale_declaration_inexacte(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amende maximale pour declaration inexacte ou incomplete (CHF)"
    reference = "SR 654.1 Art. 25 al. 1"
    default_value = 100_000.0


class renonciation_poursuite_entreprise(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Renonciation a poursuivre les personnes punissables et condamnation de l'entreprise a leur place"
    reference = "SR 654.1 Art. 25 al. 2"

    def formula(self, period, parameters):
        inexacte = self('declaration_intentionnellement_inexacte', period)
        amende = self('amende_declaration_inexacte', period)
        seuil_renonciation = 25_000.0
        return inexacte * (amende <= seuil_renonciation)
