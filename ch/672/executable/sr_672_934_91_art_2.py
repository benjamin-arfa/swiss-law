"""SR 672.934.91 Art. 2

Generated from: ch/672/de/672.934.91.md

Bundesbeschluss über die Genehmigung und die Umsetzung eines
Zusatzabkommens zum Doppelbesteuerungsabkommen zwischen der Schweiz und Frankreich (2024)
Art. 2 - Annahme der Gesetzesänderung im Anhang
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_fr_2023_gesetzesaenderung_angenommen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Änderung des Bundesgesetzes im Anhang zum Zusatzabkommen DBA CH-FR wird angenommen"
    reference = "SR 672.934.91 Art. 2"

    def formula_2024(person, period, parameters):
        return True
