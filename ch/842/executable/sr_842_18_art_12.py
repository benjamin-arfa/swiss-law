"""SR 842.18 Art. 12

Generated from: ch/842/de/842.18.md

Verzugszinse (Late payment interest): When WBG pays late on interest or
amortization, a default interest of 1% above the PUBLICA max rate (Art. 11 Abs. 1)
is charged from the due date.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

VERZUGSZINS_AUFSCHLAG_PP = 1.0  # 1 Prozentpunkt ueber Hoechstzinssatz


class ist_zahlung_verspaetet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist die Zahlung von Zinsen oder Amortisationen verspaetet"
    reference = "SR 842.18 Art. 12"


class verfallener_betrag_chf(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Verfallener Betrag (Zinsen und Kapitalzahlungen) in CHF"
    reference = "SR 842.18 Art. 12"


class verzugszinssatz_pct(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Verzugszinssatz bei verspaeteter Zahlung (Prozent)"
    reference = "SR 842.18 Art. 12"

    def formula(person, period):
        # 1% ueber dem Hoechstzinssatz nach Art. 11 Abs. 1
        hoechstzins = person('hoechstzinssatz_publica_darlehen_pct', period)
        return hoechstzins + VERZUGSZINS_AUFSCHLAG_PP


class verzugszins_monatlich_chf(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Monatlicher Verzugszins bei verspaeteter Zahlung (CHF)"
    reference = "SR 842.18 Art. 12"

    def formula(person, period):
        ist_verspaetet = person('ist_zahlung_verspaetet', period)
        betrag = person('verfallener_betrag_chf', period)
        zinssatz = person('verzugszinssatz_pct', period.this_year)
        # Monatlicher Anteil des Jahreszinssatzes
        return ist_verspaetet * betrag * zinssatz / 100 / 12
