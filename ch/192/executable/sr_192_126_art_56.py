"""SR 192.126 Art. 56

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bvg_pflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berufliche Vorsorge (BVG) Pflicht fuer private Hausangestellte (Art. 56)"
    reference = "SR 192.126 Art. 56"

    def formula(person, period, parameters):
        voraussetzungen = person('erfuellt_allgemeine_voraussetzungen', period)
        # Art. 56: BVG-pflichtig nach allgemeinen Regeln
        return voraussetzungen * 1
