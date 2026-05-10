"""SR 194.2 Art. 5 - Verpflichtungen des Beauftragten

Generated from: ch/194/de/194.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class beauftragter_betreibt_zweckmaessig_und_kostenguenstig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beauftragte betreibt die Foerderung zweckmaessig und kostenguenstig mit minimalem administrativem Aufwand"
    reference = "SR 194.2 Art. 5 Abs. 1 lit. a"


class beauftragter_waehlt_wirtschaftlich_guenstigstes_angebot(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beauftragte beruecksichtigt bei der Wahl der Massnahmen das wirtschaftlich guenstigste Angebot"
    reference = "SR 194.2 Art. 5 Abs. 1 lit. b"


class beauftragter_stimmt_massnahmen_ab(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beauftragte fuehrt Massnahmen in enger Abstimmung mit kantonalen Stellen und Bundesorganisationen durch"
    reference = "SR 194.2 Art. 5 Abs. 1 lit. c"


class beauftragter_hat_evaluationssystem(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beauftragte hat ein Evaluationssystem vorgesehen"
    reference = "SR 194.2 Art. 5 Abs. 1 lit. d"


class beauftragter_befolgt_beschaffungsrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beauftragte befolgt gegenueber Dritten die Bestimmungen des BoeB"
    reference = "SR 194.2 Art. 5 Abs. 1 lit. e"


# Computed variables

class beauftragter_erfuellt_verpflichtungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Beauftragte erfuellt alle gesetzlichen Verpflichtungen"
    reference = "SR 194.2 Art. 5 Abs. 1"

    def formula(self, period, parameters):
        a = self('beauftragter_betreibt_zweckmaessig_und_kostenguenstig', period)
        b = self('beauftragter_waehlt_wirtschaftlich_guenstigstes_angebot', period)
        c = self('beauftragter_stimmt_massnahmen_ab', period)
        d = self('beauftragter_hat_evaluationssystem', period)
        e = self('beauftragter_befolgt_beschaffungsrecht', period)
        return a * b * c * d * e
