"""SR 958.2 Art. 1

Generated from: ch/958/fr/958.2.md

Obligation d'obtenir une reconnaissance pour les plates-formes de négociation étrangères.
Foreign trading platforms must obtain FINMA recognition if they trade participation
securities of Swiss-domiciled companies that are also listed/traded in Switzerland.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class handelsplatz_handelt_ch_beteiligungspapiere(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "The foreign trading platform trades participation securities of Swiss-domiciled companies"
    reference = "SR 958.2 Art. 1 al. 1 let. a"


class beteiligungspapiere_an_ch_boerse_kotiert(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "The participation securities are listed at a Swiss stock exchange or traded on a Swiss platform"
    reference = "SR 958.2 Art. 1 al. 1 let. b"


class ausnahme_vor_30_nov_2018_kotiert(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Exception: securities were listed abroad before 30 Nov 2018 with issuer consent and obligations"
    reference = "SR 958.2 Art. 1 al. 2"


class anerkennungspflicht_auslaendischer_handelsplatz(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Foreign trading platform must obtain FINMA recognition (SR 958.2 Art. 1)"
    reference = "SR 958.2 Art. 1"

    def formula_2019(organisation, period, parameters):
        handelt_ch = organisation('handelsplatz_handelt_ch_beteiligungspapiere', period)
        kotiert_ch = organisation('beteiligungspapiere_an_ch_boerse_kotiert', period)
        ausnahme = organisation('ausnahme_vor_30_nov_2018_kotiert', period)

        return handelt_ch * kotiert_ch * not_(ausnahme)
