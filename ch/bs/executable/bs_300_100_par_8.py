"""BS 300.100 § 8

Generated from: ch/bs/de/300.100.md

§ 8 Pflegeheime: The canton provides needs-based nursing home places in
cooperation with private institutions. It is responsible for determining
care needs for home entry. It pays contributions to care costs per federal
social insurance law, and may contribute to construction/renovation costs.
Nursing homes on the list must accept care-dependent BS residents.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bs_pflegebeduerftigkeit_festgestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Pflegebeduerftigkeit fuer Heimeintritt festgestellt (BS 300.100 § 8 Abs. 1bis)"
    reference = "BS 300.100 § 8 Abs. 1bis"


class bs_pflegeheim_beitrag_pflege(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf kantonale Beitraege an Pflegekosten (BS 300.100 § 8 Abs. 2)"
    reference = "BS 300.100 § 8 Abs. 2"

    def formula(person, period, parameters):
        wohnsitz = person('bs_wohnsitz_bs', period.this_year)
        pflegebeduerftigkeit = person('bs_pflegebeduerftigkeit_festgestellt', period)
        return wohnsitz * pflegebeduerftigkeit


class bs_pflegeheim_aufnahmepflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Pflegeheim auf Liste ist zur Aufnahme verpflichtet (BS 300.100 § 8 Abs. 5)"
    reference = "BS 300.100 § 8 Abs. 5"

    def formula(person, period, parameters):
        wohnsitz = person('bs_wohnsitz_bs', period.this_year)
        pflegebeduerftigkeit = person('bs_pflegebeduerftigkeit_festgestellt', period)
        return wohnsitz * pflegebeduerftigkeit
