"""SR 429.1 Art. 4

Generated from: ch/429/de/429.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 4 - Erweiterte Dienstleistungen
# Regelt kommerzielle Verwertung meteorologischer Daten durch das Bundesamt.

# --- Input variables ---

class ist_erweiterte_dienstleistung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Dienstleistung ist eine erweiterte (kommerzielle) Dienstleistung nach Art. 4 MetG"
    reference = "SR 429.1 Art. 4 Abs. 1"


class zusammenhang_mit_grundangebot(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die erweiterte Dienstleistung steht in engem Zusammenhang mit dem Grundangebot"
    reference = "SR 429.1 Art. 4 Abs. 2"


class beeintraechtigt_grundangebot(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die erweiterte Dienstleistung beeintraechtigt das Grundangebot"
    reference = "SR 429.1 Art. 4 Abs. 2"


class gestehungskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gestehungskosten der erweiterten Dienstleistung in CHF"
    reference = "SR 429.1 Art. 4 Abs. 3"


class entgelt_erweiterte_dienstleistung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Entgelt (Preis) fuer die erweiterte Dienstleistung in CHF"
    reference = "SR 429.1 Art. 4 Abs. 3"


# --- Computed variables ---

class erweiterte_dienstleistung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die erweiterte Dienstleistung ist zulaessig (Art. 4 Abs. 2 MetG)"
    reference = "SR 429.1 Art. 4 Abs. 2"

    def formula(self, period, parameters):
        ist_erweitert = self('ist_erweiterte_dienstleistung', period)
        zusammenhang = self('zusammenhang_mit_grundangebot', period)
        beeintr = self('beeintraechtigt_grundangebot', period)
        return ist_erweitert * zusammenhang * (1 - beeintr)


class entgelt_mindestens_gestehungskosten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Entgelt liegt nicht unter den Gestehungskosten (Art. 4 Abs. 3 MetG)"
    reference = "SR 429.1 Art. 4 Abs. 3"

    def formula(self, period, parameters):
        entgelt = self('entgelt_erweiterte_dienstleistung', period)
        kosten = self('gestehungskosten', period)
        return entgelt >= kosten
