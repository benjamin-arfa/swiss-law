"""SR 221.214.1 Art. 16

Generated from: ch/221/fr/221.214.1.md

Right of revocation for consumer credit: 14-day withdrawal period
starting from receipt of contract copy.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class lcc_date_reception_contrat(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = MONTH
    label = "Date de reception de l'exemplaire du contrat de credit par le consommateur"
    reference = "SR 221.214.1 Art. 16 al. 2"


class lcc_delai_revocation_jours(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Delai de revocation du contrat de credit a la consommation en jours"
    reference = "SR 221.214.1 Art. 16 al. 1"

    def formula(person, period, parameters):
        return 14


class lcc_revocation_exercee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le consommateur a exerce son droit de revocation par ecrit"
    reference = "SR 221.214.1 Art. 16 al. 1"


class lcc_pret_verse_avant_fin_delai(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le pret a ete verse avant la fin du delai de revocation"
    reference = "SR 221.214.1 Art. 16 al. 3"


class lcc_consommateur_doit_rembourser_sans_interets(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Le consommateur doit rembourser le montant sans interets ni frais (apres revocation)"
    reference = "SR 221.214.1 Art. 16 al. 3 renvoi art. 15 al. 2"

    def formula(person, period, parameters):
        revocation = person('lcc_revocation_exercee', period)
        pret_verse = person('lcc_pret_verse_avant_fin_delai', period)
        return revocation * pret_verse
