"""SR 672.937.2 Art. 2

Generated from: ch/672/de/672.937.2.md

Bundesbeschluss über die Genehmigung eines Protokolls zur Änderung
des Doppelbesteuerungsabkommens zwischen der Schweiz und Griechenland
Art. 2 - Fakultatives Staatsvertragsreferendum
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_gr_beschluss_untersteht_referendum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschluss untersteht dem fakultativen Staatsvertragsreferendum (Art. 141 Abs. 1 Bst. d Ziff. 3 BV)"
    reference = "SR 672.937.2 Art. 2"

    def formula_2011(person, period, parameters):
        return True
