"""SR 425.15 Art. 10

Generated from: ch/425/de/425.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class teuerung_seit_letzter_anpassung_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Teuerung gemaess Landesindex der Konsumentenpreise seit Inkrafttreten oder letzter Anpassung in Prozent"
    reference = "SR 425.15 Art. 10"


class stundenansatz_anpassung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "EJPD darf Stundenansaetze auf naechsten Jahresanfang an Teuerung anpassen"
    reference = "SR 425.15 Art. 10"

    def formula(person, period, parameters):
        teuerung = person('teuerung_seit_letzter_anpassung_prozent', period)
        return teuerung >= 5.0
