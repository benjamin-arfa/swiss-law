"""SR 861 Art. 5

Generated from: ch/de/861.md

Assessment and duration of financial aid: maximum one-third of costs,
max CHF 5000 per place per year for day-care; degressive subsidy
increase support (65%/35%/10%); maximum 3 years duration.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class finanzhilfe_max_anteil_kita(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstanteil der Finanzhilfen an Investitions- und Betriebskosten fuer Kindertagesstaetten"
    reference = "SR 861 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return 1.0 / 3.0


class finanzhilfe_max_pro_platz_jahr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstbetrag der Finanzhilfe pro Platz und Jahr (CHF)"
    reference = "SR 861 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        return 5000.0


class finanzhilfe_max_anteil_tagesfamilien(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstanteil der Finanzhilfen an Kosten fuer Tagesfamilien-Koordination"
    reference = "SR 861 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        return 1.0 / 3.0


class finanzhilfe_max_anteil_innovationsprojekt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstanteil der Finanzhilfen an Kosten des Innovationsprojekts inkl. Evaluation"
    reference = "SR 861 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        return 1.0 / 3.0


class subventionserhoehung_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Laufendes Jahr der Subventionserhoehung (1, 2 oder 3)"
    reference = "SR 861 Art. 5 Abs. 3bis"


class finanzhilfe_anteil_subventionserhoehung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Finanzhilfe an der Subventionserhoehung im laufenden Jahr"
    reference = "SR 861 Art. 5 Abs. 3bis"

    def formula(person, period, parameters):
        jahr = person('subventionserhoehung_jahr', period)
        return (
            (jahr == 1) * 0.65
            + (jahr == 2) * 0.35
            + (jahr == 3) * 0.10
        )


class finanzhilfe_max_anteil_abstimmungsprojekt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstanteil der Finanzhilfen an Kosten des Abstimmungsprojekts inkl. Evaluation"
    reference = "SR 861 Art. 5 Abs. 3ter"

    def formula(person, period, parameters):
        return 0.5


class finanzhilfe_max_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Dauer der Finanzhilfen in Jahren"
    reference = "SR 861 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        return 3
