"""BS 300.100 § 7

Generated from: ch/bs/de/300.100.md

§ 7 Spitaeler: The canton guarantees and finances inpatient and outpatient
treatment according to federal social insurance law. The Regierungsrat
commissions needs-based public-service obligations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bs_spital_stationaere_behandlung_gewaehrleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Stationaere und ambulante Behandlung gemaess Sozialversicherungsrecht gewaehrleistet (BS 300.100 § 7 Abs. 1)"
    reference = "BS 300.100 § 7 Abs. 1"
