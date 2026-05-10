"""SR 142.206 Art. 13

Generated from: ch/142/de/142.206.md

Verfahren in dringenden Faellen: Bei unmittelbar drohender Lebensgefahr
im Zusammenhang mit terroristischer oder schwerer Straftat bearbeitet
die EAZ fedpol das Gesuch unverzueglich und ueberprueft nachtraeglich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ees_dringender_fall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein dringender Fall mit unmittelbar drohender Lebensgefahr vorliegt"
    reference = "SR 142.206 Art. 13"

    def formula_2022_05(person, period, parameters):
        return person('ees_unmittelbare_lebensgefahr', period)


class ees_unverzuegliche_bearbeitung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Gesuch unverzueglich von der EAZ fedpol bearbeitet wird"
    reference = "SR 142.206 Art. 13"

    def formula_2022_05(person, period, parameters):
        return person('ees_dringender_fall', period)


class ees_nachtraegliche_ueberpruefung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine nachtraegliche Ueberpruefung der Voraussetzungen erforderlich ist"
    reference = "SR 142.206 Art. 13"

    def formula_2022_05(person, period, parameters):
        return person('ees_dringender_fall', period)
