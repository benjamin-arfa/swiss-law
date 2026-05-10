"""SR 170.32 Art. 8

Generated from: ch/170/de/170.32.md

Haftung des Beamten gegenüber dem Bund bei vorsätzlicher oder grobfahrlässiger
Dienstpflichtverletzung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schaden_dem_bund_zugefuegt(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Dem Bund unmittelbar zugefügter Schaden in CHF (Art. 8 VG)"
    reference = "SR 170.32, Art. 8"


class beamter_haftet_gegenueber_bund(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beamte haftet dem Bund für den Schaden (Art. 8 VG)"
    reference = "SR 170.32, Art. 8"

    def formula(person, period, parameters):
        ist_beamter = person('untersteht_verantwortlichkeitsgesetz', period)
        vorsatz = person('beamter_hat_vorsaetzlich_gehandelt', period)
        grob_fahrlaessig = person('beamter_hat_grobfahrlaessig_gehandelt', period)
        schaden = person('schaden_dem_bund_zugefuegt', period)
        return ist_beamter * (vorsatz + grob_fahrlaessig > 0) * (schaden > 0)
