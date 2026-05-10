"""SR 192.126 Art. 55

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_iv_eo_beitragspflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "AHV/IV/EO Beitragspflicht fuer private Hausangestellte (Art. 55)"
    reference = "SR 192.126 Art. 55"

    def formula(person, period, parameters):
        voraussetzungen = person('erfuellt_allgemeine_voraussetzungen', period)
        schweizer = person('hat_schweizer_buergerrecht', period)
        # Art. 55: Grundsaetzlich AHV/IV/EO-pflichtig, Ausnahmen fuer bestimmte Kategorien
        return voraussetzungen * 1

class ahv_arbeitgeber_anteil_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Arbeitgeberanteil AHV/IV/EO in Prozent"
    reference = "SR 192.126 Art. 55"

    def formula(person, period, parameters):
        # Gesetzliche Haelfte der AHV/IV/EO-Beitraege
        return person('ahv_iv_eo_beitragspflichtig', period) * 50
