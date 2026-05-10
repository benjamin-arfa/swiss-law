"""SR 672.934.9 Art. 2

Generated from: ch/672/de/672.934.9.md

Bundesbeschluss über die Genehmigung eines Zusatzabkommens
zum Doppelbesteuerungsabkommen zwischen der Schweiz und Frankreich (2010)
Art. 2 - Umsetzung der Amtshilfe
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class dba_ch_fr_2009_amtshilfe_gesetz_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Umsetzungsgesetz für die Amtshilfe nach OECD-Standard (DBA CH-FR) ist in Kraft"
    reference = "SR 672.934.9 Art. 2"


class dba_ch_fr_2009_amtshilfe_durch_verordnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat regelt Amtshilfe vorübergehend durch Verordnung (bis Inkrafttreten des Gesetzes)"
    reference = "SR 672.934.9 Art. 2"

    def formula(person, period, parameters):
        gesetz_in_kraft = person('dba_ch_fr_2009_amtshilfe_gesetz_in_kraft', period)
        return not_(gesetz_in_kraft)
