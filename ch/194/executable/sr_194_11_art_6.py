"""SR 194.11 Art. 6 - Finanzielle Unterstuetzung

Generated from: ch/194/de/194.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class massnahme_hat_schweiz_zum_gegenstand(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Massnahme hat thematisch die Schweiz zum Gegenstand"
    reference = "SR 194.11 Art. 6 Abs. 1 lit. a"


class massnahme_vermittelt_grundbotschaften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Massnahme vermittelt die Grundbotschaften gemaess Art. 2 Abs. 2 des Gesetzes"
    reference = "SR 194.11 Art. 6 Abs. 1 lit. b"


class massnahme_dient_aussenpolitischen_interessen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Massnahme dient den aussenpolitischen Interessen der Schweiz"
    reference = "SR 194.11 Art. 6 Abs. 1 lit. c"


class gesuch_schriftlich_eingereicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Gesuch um finanzielle Unterstuetzung wurde dem EDA vorgaengig schriftlich eingereicht"
    reference = "SR 194.11 Art. 6 Abs. 2"


# Computed variables

class finanzielle_unterstuetzung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Massnahme kann finanziell unterstuetzt werden"
    reference = "SR 194.11 Art. 6 Abs. 1"

    def formula(self, period, parameters):
        schweiz = self('massnahme_hat_schweiz_zum_gegenstand', period)
        botschaften = self('massnahme_vermittelt_grundbotschaften', period)
        interessen = self('massnahme_dient_aussenpolitischen_interessen', period)
        gesuch = self('gesuch_schriftlich_eingereicht', period)
        return schweiz * botschaften * interessen * gesuch
