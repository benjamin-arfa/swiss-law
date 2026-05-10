"""SR 232.119 Art. 1

Generated from: ch/232/de/232.119.md

Art. 1 defines what qualifies as a "watch" (Uhr) under the ordinance
on the use of the Swiss name for watches.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_uhr_am_handgelenk(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zeitmessinstrument ist zum Tragen am Handgelenk bestimmt"
    reference = "SR 232.119 Art. 1 Abs. 1 lit. a"


class hauptfunktion_ist_zeitmessung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Die Hauptfunktion des Instruments ist die Zeitmessung"
    reference = "SR 232.119 Art. 1 Abs. 1 lit. b"


class werk_breite_laenge_durchmesser_mm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Breite, Laenge oder Durchmesser des Werks in mm"
    reference = "SR 232.119 Art. 1 Abs. 1 lit. b Ziff. 1"


class werk_dicke_mm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Dicke des Werks (mit Boden und Bruecke) in mm"
    reference = "SR 232.119 Art. 1 Abs. 1 lit. b Ziff. 2"


class ist_uhr_nach_sr_232_119(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gilt als Uhr im Sinne von SR 232.119 Art. 1"
    reference = "SR 232.119 Art. 1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 1 lit. a: Zeitmessinstrument am Handgelenk
        am_handgelenk = person('ist_uhr_am_handgelenk', period)

        # Art. 1 Abs. 1 lit. b: Hauptfunktion Zeitmessung UND Werk innerhalb Groessenlimits
        hauptfunktion = person('hauptfunktion_ist_zeitmessung', period)
        breite = person('werk_breite_laenge_durchmesser_mm', period)
        dicke = person('werk_dicke_mm', period)

        groesse_ok = (breite <= 60) + (dicke <= 14)  # either dimension criterion
        nach_groesse = hauptfunktion * (groesse_ok > 0)

        return am_handgelenk + nach_groesse > 0
