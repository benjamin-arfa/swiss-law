"""SR 0.641.751.411 Art. 8 - Emission trading system exclusion

Art. 8: LI companies subject to the LI Emissions Trading Act
(Emissionshandelsgesetz) cannot commit to Swiss authorities to reduce
greenhouse gas emissions. Taxes already collected are refunded by OFDF
upon proof and attestation from LI authority.

Generated from: ch/0/fr/0.641.751.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class soumis_echanges_droits_emission_li(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Company subject to LI Emissions Trading Act (Art. 8)"
    default_value = False


class interdit_engagement_reduction_ch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Company barred from Swiss emission reduction commitments (Art. 8)"

    def formula(person, period, parameters):
        return person("soumis_echanges_droits_emission_li", period)


class remboursement_taxes_deja_percues(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Taxes already collected to be refunded by OFDF (Art. 8)"
    default_value = 0
