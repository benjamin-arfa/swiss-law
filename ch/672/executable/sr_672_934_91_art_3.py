"""SR 672.934.91 Art. 3

Generated from: ch/672/de/672.934.91.md

Bundesbeschluss über die Genehmigung und die Umsetzung eines
Zusatzabkommens zum Doppelbesteuerungsabkommen zwischen der Schweiz und Frankreich (2024)
Art. 3 - Bundesbeteiligung am finanziellen Ausgleich (Genfer Grenzgänger)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# --- Input variables ---

class dba_ch_fr_2023_zusatzabkommen_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Zusatzabkommen zum DBA CH-FR (2023) ist für beide Parteien in Kraft getreten"
    reference = "SR 672.934.91 Art. 3 Abs. 3"


class dba_ch_fr_2023_jahr_inkrafttreten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr des Inkrafttretens des Zusatzabkommens zum DBA CH-FR (2023)"
    reference = "SR 672.934.91 Art. 3 Abs. 2"


class genfer_grenzgaenger_steuereinnahmen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Einnahmen aus Steuern auf Löhnen der in Genf arbeitenden Einwohner der Departemente Ain und Haute-Savoie (CHF)"
    reference = "SR 672.934.91 Art. 3 Abs. 2"


class anteil_direkte_bundessteuer(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der direkten Bundessteuer an den Steuereinnahmen der Genfer Grenzgänger"
    reference = "SR 672.934.91 Art. 3 Abs. 2"


class genfer_telearbeit_ausgleich_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Neuer Ausgleichsbetrag für Telearbeit, den Kanton Genf und Genfer Gemeinden schulden (CHF)"
    reference = "SR 672.934.91 Art. 3 Abs. 2"


# --- Computed variables ---

class bundesbeteiligung_genfer_ausgleich(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beteiligung des Bundes am Genfer finanziellen Ausgleich (CHF)"
    reference = "SR 672.934.91 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        steuereinnahmen = person('genfer_grenzgaenger_steuereinnahmen', period)
        anteil_bund = person('anteil_direkte_bundessteuer', period)
        max_telearbeit = person('genfer_telearbeit_ausgleich_betrag', period)
        beteiligung = steuereinnahmen * anteil_bund
        # Höchstens der Betrag des neuen Ausgleichs für Telearbeit
        return min_(beteiligung, max_telearbeit)


class bundesbeteiligung_genfer_ausgleich_geschuldet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Bundesbeteiligung am Genfer finanziellen Ausgleich ist geschuldet (ab Steuerjahr 2023, sofern Zusatzabkommen in Kraft)"
    reference = "SR 672.934.91 Art. 3 Abs. 3"

    def formula_2023(person, period, parameters):
        in_kraft = person('dba_ch_fr_2023_zusatzabkommen_in_kraft', period)
        return in_kraft
