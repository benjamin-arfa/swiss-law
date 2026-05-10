"""BS 300.100 § 12

Generated from: ch/bs/de/300.100.md

§ 12 Zahnkliniken: Dental clinics must treat economically disadvantaged
BS residents. The base tariff is the UVG dental tariff. Economically
disadvantaged BS residents receive a reduction based on their financial
situation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bs_zahnklinik_behandlungspflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Zahnklinik ist zur Behandlung verpflichtet (BS 300.100 § 12 Abs. 1)"
    reference = "BS 300.100 § 12 Abs. 1"

    def formula(person, period, parameters):
        wohnsitz = person('bs_wohnsitz_bs', period.this_year)
        schwaecher = person('bs_wirtschaftlich_schwaecher_gestellt', period.this_year)
        return wohnsitz * schwaecher


class bs_zahnklinik_tarifbasis_uvg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Basistarif ist der UVG-Zahnarzttarif (BS 300.100 § 12 Abs. 2)"
    reference = "BS 300.100 § 12 Abs. 2"

    def formula(person, period, parameters):
        # UVG dental tariff always applies as base tariff in BS dental clinics
        return person('bs_zahnklinik_behandlungspflicht', period)


class bs_zahnklinik_tarifreduktion(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Tarifreduktion in Zahnklinik (BS 300.100 § 12 Abs. 2)"
    reference = "BS 300.100 § 12 Abs. 2"

    def formula(person, period, parameters):
        wohnsitz = person('bs_wohnsitz_bs', period.this_year)
        schwaecher = person('bs_wirtschaftlich_schwaecher_gestellt', period.this_year)
        return wohnsitz * schwaecher
