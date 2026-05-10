"""SR 672.934.9 Art. 3

Generated from: ch/672/de/672.934.9.md

Bundesbeschluss über die Genehmigung eines Zusatzabkommens
zum Doppelbesteuerungsabkommen zwischen der Schweiz und Frankreich (2010)
Art. 3 - Erklärung betreffend illegal beschaffte Daten
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_fr_2009_amtshilfegesuch_auf_illegalen_daten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Amtshilfegesuch beruht auf illegal beschafften Daten"
    reference = "SR 672.934.9 Art. 3 Abs. 1"


class dba_ch_fr_2009_keine_amtshilfe_bei_illegalen_daten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schweiz leistet keine Amtshilfe, wenn das Gesuch auf illegal beschafften Daten beruht; sie verlangt stattdessen Rechtshilfe"
    reference = "SR 672.934.9 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        illegale_daten = person('dba_ch_fr_2009_amtshilfegesuch_auf_illegalen_daten', period)
        return illegale_daten
