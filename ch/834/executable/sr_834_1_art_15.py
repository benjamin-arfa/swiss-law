"""SR 834.1 Art. 15

Generated from: ch/834/de/834.1.md

Betriebszulage: 27 Prozent des Hoechstbetrages der Gesamtentschaedigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eo_ist_selbstaendig_betriebsfuehrer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person fuehrt einen Betrieb als Eigentuemer/Paechter/Nutzniesser (Art. 8 EOG)"
    reference = "SR 834.1 Art. 8"


class eo_betriebszulage_taeglich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegl. Betriebszulage (CHF)"
    reference = "SR 834.1 Art. 15"

    def formula_2005(person, period, parameters):
        import numpy as np

        ist_dienstleistend = person('eo_ist_dienstleistend', period)
        ist_betriebsfuehrer = person('eo_ist_selbstaendig_betriebsfuehrer', period)

        p = parameters(period).sr834_1
        hoechstbetrag = p.hoechstbetrag_gesamtentschaedigung
        satz = p.betriebszulage_anteil  # 0.27

        return np.where(
            ist_dienstleistend * ist_betriebsfuehrer,
            hoechstbetrag * satz,
            0.0
        )
