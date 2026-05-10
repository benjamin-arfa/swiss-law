"""SR 221.214.1 Art. 32a

Generated from: ch/221/fr/221.214.1.md

Sanctions for participatory credit brokers: fine up to 100,000 CHF;
consumer owes no interest or fees.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lcc_courtier_participatif_contrevient(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le courtier en credit participatif contrevient aux art. 25-31"
    reference = "SR 221.214.1 Art. 32a al. 1"


class lcc_amende_max_courtier_participatif_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Amende maximale pour courtier en credit participatif en CHF"
    reference = "SR 221.214.1 Art. 32a al. 1"

    def formula(person, period, parameters):
        return 100000.0


class lcc_consommateur_exonere_interets_frais(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le consommateur ne doit ni interets ni frais (courtier sanctionne)"
    reference = "SR 221.214.1 Art. 32a al. 2"

    def formula(person, period, parameters):
        return person('lcc_courtier_participatif_contrevient', period)
