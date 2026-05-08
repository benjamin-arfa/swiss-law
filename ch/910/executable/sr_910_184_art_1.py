"""SR 910.184 Art. 1

Generated from: ch/910/de/910.184.md

Laenderliste: Biologische Erzeugnisse aus Laendern, die mit den
entsprechenden Spezifikationen in Anhang 1 aufgefuehrt sind,
duerfen als biologisch gekennzeichnet vermarktet werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class herkunftsland_in_laenderliste_bio(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Herkunftsland in der Laenderliste nach Anhang 1 der Bio-Verordnung BLW aufgefuehrt ist"
    reference = "SR 910.184 Art. 1"


class darf_als_biologisch_vermarktet_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das biologische Erzeugnis als biologisch gekennzeichnet vermarktet werden darf"
    reference = "SR 910.184 Art. 1"

    def formula(person, period, parameters):
        return person('herkunftsland_in_laenderliste_bio', period)
