"""SR 531.83 Art. 3 — Inkrafttreten und Geltungsdauer

Verordnung über die Beschränkung der Verwendung von Alteplase.
Generated from: ch/de/531/531.83.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity
import numpy as np

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class verordnung_531_83_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Verordnung SR 531.83 ist in Kraft (Art. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: Tritt am 29. Juli 2022 in Kraft.
        # Art. 3 Abs. 4: Geltungsdauer verlängert bis 31. August 2025.
        # Hinweis: Zeitlich befristete Verordnung.
        return True


class verordnung_531_83_geltungsdauer_ende(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Enddatum der Geltungsdauer der Verordnung SR 531.83 (Art. 3 Abs. 4: 31. August 2025)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2022/439/de#art_3"
    default_value = "2025-08-31"
