"""SR 221.213.221 Art. 1 – Grundlagen der Pachtzinsberechnung

Generated from: ch/221/de/221.213.221.md

Für die Verzinsung des Ertragswertes gilt der Satz von 3.05 Prozent.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ertragswert_verzinsungssatz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Verzinsungssatz des Ertragswertes für landwirtschaftliche Pachtzinsberechnung"
    reference = "SR 221.213.221 Art. 1 Abs. 1"
    # 3.05% seit 1. April 2018 (AS 2018 1003)
    default_value = 0.0305
