"""SR 672.965.6 Art. 1

Generated from: ch/672/de/672.965.6.md

Bundesbeschluss über die Genehmigung eines Doppelbesteuerungsabkommens
zwischen der Schweiz und Katar
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_qa_abkommen_genehmigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Abkommen vom 24. September 2009 zwischen der Schweiz und Katar zur Vermeidung der Doppelbesteuerung ist genehmigt"
    reference = "SR 672.965.6 Art. 1 Abs. 1"

    def formula_2010(person, period, parameters):
        return True


class dba_ch_qa_bundesrat_ratifizierung_ermaechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat ist ermächtigt, das DBA CH-Katar zu ratifizieren"
    reference = "SR 672.965.6 Art. 1 Abs. 2"

    def formula_2010(person, period, parameters):
        return True
