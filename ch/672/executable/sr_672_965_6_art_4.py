"""SR 672.965.6 Art. 4

Generated from: ch/672/de/672.965.6.md

Bundesbeschluss über die Genehmigung eines Doppelbesteuerungsabkommens
zwischen der Schweiz und Katar
Art. 4 - Fakultatives Staatsvertragsreferendum
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_qa_beschluss_untersteht_referendum(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschluss untersteht dem fakultativen Staatsvertragsreferendum (Art. 141 Abs. 1 Bst. d Ziff. 3 BV)"
    reference = "SR 672.965.6 Art. 4"

    def formula_2010(person, period, parameters):
        return True
