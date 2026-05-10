"""SR 120.423 Art. 2

Generated from: ch/120/de/120.423.md

Aktualisierung der Anhaenge: Das Generalsekretariat des VBS und die
Gruppe Verteidigung beantragen mindestens alle fuenf Jahre die
Aktualisierung der jeweiligen Anhaenge.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class aktualisierungsintervall_anhaenge_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestintervall in Jahren fuer die Aktualisierung der Anhaenge"
    reference = "SR 120.423 Art. 2 Abs. 1-2"

    def formula(person, period, parameters):
        return parameters(period).aktualisierungsintervall_anhaenge


class aenderungsfrist_anhang_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist in Monaten fuer Anpassung nach Aenderung des uebergeordneten Anhangs PSPV"
    reference = "SR 120.423 Art. 2 Abs. 3-4"

    def formula(person, period, parameters):
        return parameters(period).aenderungsfrist_anhang_monate
