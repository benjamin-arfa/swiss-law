"""SR 611.031 Art. 6

Generated from: ch/611/de/611.031.md

Gottfried-Keller-Stiftung - Art. 6: Wahl und Zusammensetzung der Kommission.
Bundesrat wählt Mitglieder für 4 Jahre. 5 Mitglieder total.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class gks_kommission_amtsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer der Mitglieder der GKS-Kommission in Jahren (Art. 6 Abs. 1)"
    reference = "SR 611.031 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        # Art. 6 Abs. 1: vier Jahre, Wiederwahl möglich
        return 4


class gks_kommission_anzahl_mitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der GKS-Kommission (Art. 6 Abs. 2)"
    reference = "SR 611.031 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        # Art. 6 Abs. 2: Präsident/in, Vizepräsident/in und drei weitere = 5
        return 5
