"""SR 842.18 Art. 8

Generated from: ch/842/de/842.18.md

Kostenmiete (Cost-based rent): WBG must rent subsidized apartments at cost.
Allowed cost components: interest on invested capital, land lease, amortization,
maintenance, admin, risk surcharge, public charges. Equity interest capped at
reference mortgage rate (Referenzzinssatz).
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class zinsen_fremd_und_eigenkapital_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zinsen fuer das investierte Fremd- und Eigenkapital (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 2 lit. a"


class baurechtszins_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Baurechtszins (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 2 lit. b"


class amortisationen_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amortisationen (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 2 lit. c"


class unterhaltskosten_und_erneuerungsfonds_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Unterhaltskosten sowie Einlagen in den Erneuerungsfonds (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 2 lit. d"


class verwaltungskosten_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Verwaltungskosten (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 2 lit. e"


class risikozuschlag_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Risikozuschlag (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 2 lit. f"


class oeffentliche_abgaben_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mit der Sache verbundene Lasten und oeffentliche Abgaben (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 2 lit. g"


class selbstkosten_wbg_wohnung_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamte Selbstkosten der WBG-Wohnung pro Jahr (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 2"

    def formula(person, period):
        return (
            person('zinsen_fremd_und_eigenkapital_chf', period) +
            person('baurechtszins_chf', period) +
            person('amortisationen_chf', period) +
            person('unterhaltskosten_und_erneuerungsfonds_chf', period) +
            person('verwaltungskosten_chf', period) +
            person('risikozuschlag_chf', period) +
            person('oeffentliche_abgaben_chf', period)
        )


class referenzzinssatz_hypotheken_pct(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Referenzzinssatz fuer Hypotheken nach Art. 12a VMWG (Prozent)"
    reference = "SR 842.18 Art. 8 Abs. 4"


class eigenkapital_wbg_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Von der WBG investiertes Eigenkapital (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 4"


class max_eigenkapitalverzinsung_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Verzinsung des Eigenkapitals der WBG (CHF)"
    reference = "SR 842.18 Art. 8 Abs. 4"

    def formula(person, period):
        # Eigenkapital darf hoechstens zum Referenzzinssatz verzinst werden
        eigenkapital = person('eigenkapital_wbg_chf', period)
        referenzzins = person('referenzzinssatz_hypotheken_pct', period)
        return eigenkapital * referenzzins / 100
