"""SR 631.011 Art. 7

Generated from: ch/631/de/631.011.md

Anmeldung des Grenzweidegangs: Die Tierhalterin oder der Tierhalter
muss das Eintreffen einer Herde der Zollstelle zwei Tage im Voraus melden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anmeldefrist_grenzweidegang_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Tage im Voraus, die der Grenzweidegang gemeldet wurde"
    reference = "SR 631.011 Art. 7 Abs. 1"


class anmeldung_grenzweidegang_fristgemaess(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Anmeldung des Grenzweidegangs fristgemaess (mind. 2 Tage vorher) erfolgt ist"
    reference = "SR 631.011 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        tage = person('anmeldefrist_grenzweidegang_tage', period)
        return tage >= 2
