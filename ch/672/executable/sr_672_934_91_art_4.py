"""SR 672.934.91 Art. 4

Generated from: ch/672/de/672.934.91.md

Bundesbeschluss über die Genehmigung und die Umsetzung eines
Zusatzabkommens zum Doppelbesteuerungsabkommen zwischen der Schweiz und Frankreich (2024)
Art. 4 - Referendum und Inkrafttreten
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_fr_2023_beschluss_untersteht_referendum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschluss untersteht dem fakultativen Referendum (Art. 141 Abs. 1 Bst. d Ziff. 3 und Art. 141a Abs. 2 BV)"
    reference = "SR 672.934.91 Art. 4 Abs. 1"

    def formula_2024(person, period, parameters):
        return True


class dba_ch_fr_2023_anhang_inkrafttreten_durch_bundesrat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bundesrat bestimmt das Inkrafttreten der Änderung des Bundesgesetzes im Anhang (1. Januar 2026)"
    reference = "SR 672.934.91 Art. 4 Abs. 2"

    def formula_2026(person, period, parameters):
        return True
