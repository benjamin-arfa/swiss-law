"""SR 672.934.9 Art. 1

Generated from: ch/672/de/672.934.9.md

Bundesbeschluss über die Genehmigung eines Zusatzabkommens
zum Doppelbesteuerungsabkommen zwischen der Schweiz und Frankreich (2010)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_fr_2009_zusatzabkommen_genehmigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zusatzabkommen vom 27. August 2009 zum DBA CH-FR (SR 0.672.934.91) ist genehmigt"
    reference = "SR 672.934.9 Art. 1 Abs. 1"

    def formula_2010(person, period, parameters):
        return True


class dba_ch_fr_2009_bundesrat_ratifizierung_ermaechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat ist ermächtigt, das Zusatzabkommen zum DBA CH-FR zu ratifizieren"
    reference = "SR 672.934.9 Art. 1 Abs. 2"

    def formula_2010(person, period, parameters):
        return True
