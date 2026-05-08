"""SR 916.010.2 Art. 1

Generated from: ch/916/fr/916.010.2.md

Principe — Les éléments conceptuels et règles d'application de l'identité visuelle
commune doivent être utilisés pour toutes les applications graphiques des supports
de communication soutenus par la Confédération.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR


class communication_soutenue_par_confederation(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Communication measure is financially supported by the Confederation"
    reference = "SR 916.010.2 Art. 1 al. 1"


class utilise_identite_visuelle_commune(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Uses the common visual identity elements as per annex"
    reference = "SR 916.010.2 Art. 1 al. 1"


class identite_visuelle_obligatoire(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Common visual identity elements are mandatory for this communication"
    reference = "SR 916.010.2 Art. 1"

    def formula_2008(organisation, period, parameters):
        soutenue = organisation('communication_soutenue_par_confederation', period)
        # Obligation applies only to Confederation-supported communications
        return soutenue
