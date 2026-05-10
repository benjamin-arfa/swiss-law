"""SR 170.32 Art. 19b

Generated from: ch/170/de/170.32.md

Kausalhaftung des Bundes bei unrichtiger/unrechtmässiger Datenerfassung durch
einen anderen Schengen/Dublin-Staat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class daten_unrichtig_durch_anderen_staat(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ein anderer Schengen/Dublin-Staat hat Daten unrichtig oder unrechtmässig erfasst (Art. 19b Abs. 1 Bst. a VG)"
    reference = "SR 170.32, Art. 19b Abs. 1 Bst. a"


class schaden_durch_unrichtige_daten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Schaden wurde aufgrund der unrichtigen Daten in amtlicher Tätigkeit verursacht (Art. 19b Abs. 1 Bst. b VG)"
    reference = "SR 170.32, Art. 19b Abs. 1 Bst. b"


class bund_haftet_ohne_widerrechtlichkeitsnachweis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund haftet ohne Nachweis einer Widerrechtlichkeit (Art. 19b Abs. 1 VG)"
    reference = "SR 170.32, Art. 19b Abs. 1"

    def formula(person, period, parameters):
        daten_falsch = person('daten_unrichtig_durch_anderen_staat', period)
        schaden = person('schaden_durch_unrichtige_daten', period)
        return daten_falsch * schaden
