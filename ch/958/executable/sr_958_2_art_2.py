"""SR 958.2 Art. 2

Generated from: ch/958/fr/958.2.md

Procédure — FINMA grants recognition when the foreign trading platform is subject
to appropriate regulation/supervision and is not domiciled in a jurisdiction that
restricts trading of Swiss participation securities on Swiss platforms.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class handelsplatz_angemessene_regulierung(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Foreign trading platform is subject to appropriate regulation and supervision"
    reference = "SR 958.2 Art. 2 al. 1 let. a"


class handelsplatz_keine_einschraenkende_jurisdiktion(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Platform is not domiciled in a jurisdiction restricting Swiss securities trading"
    reference = "SR 958.2 Art. 2 al. 1 let. b"


class handelsplatz_anerkennung_erteilt(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "FINMA grants recognition to the foreign trading platform"
    reference = "SR 958.2 Art. 2"

    def formula_2019(organisation, period, parameters):
        regulierung = organisation('handelsplatz_angemessene_regulierung', period)
        keine_einschraenkung = organisation('handelsplatz_keine_einschraenkende_jurisdiktion', period)

        return regulierung * keine_einschraenkung
