"""SR 221.213.221 Art. 3 – Verzinsung (Gewerbe)

Generated from: ch/221/de/221.213.221.md

Die Verzinsung beträgt 3.05 Prozent des Ertragswertes des Gewerbes
unter Einschluss der Gebäude und allfälliger Dauerkulturen,
einschliesslich der Grundinfrastruktur.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

VERZINSUNGSSATZ = 0.0305  # 3.05% seit 1. April 2018


class ertragswert_gewerbe(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ertragswert des landwirtschaftlichen Gewerbes inkl. Gebäude und Dauerkulturen (CHF)"
    reference = "SR 221.213.221 Art. 3"


class verzinsung_gewerbe(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Verzinsung des Ertragswertes des Gewerbes (CHF)"
    reference = "SR 221.213.221 Art. 3"

    def formula(person, period, parameters):
        ertragswert = person('ertragswert_gewerbe', period)
        return ertragswert * VERZINSUNGSSATZ
