"""SR 672.934.91 Art. 1

Generated from: ch/672/de/672.934.91.md

Bundesbeschluss über die Genehmigung und die Umsetzung eines
Zusatzabkommens zum Doppelbesteuerungsabkommen zwischen der Schweiz und Frankreich (2024)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_fr_2023_zusatzabkommen_genehmigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zusatzabkommen vom 27. Juni 2023 zum geänderten DBA CH-FR (SR 0.672.934.91) ist genehmigt"
    reference = "SR 672.934.91 Art. 1 Abs. 1"

    def formula_2024(person, period, parameters):
        return True


class dba_ch_fr_2023_bundesrat_ratifizierung_ermaechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat ist ermächtigt, das Zusatzabkommen zum DBA CH-FR (2023) zu ratifizieren"
    reference = "SR 672.934.91 Art. 1 Abs. 2"

    def formula_2024(person, period, parameters):
        return True
