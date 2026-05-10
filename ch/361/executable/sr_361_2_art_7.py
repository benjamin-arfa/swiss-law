"""SR 361.2 Art. 7

Generated from: ch/361/de/361.2.md

Weitergabe von Daten: Amtshilfe aus dem IPAS an andere Behoerden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ipas_empfaenger_ist_berechtigte_behoerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Empfaenger ist eine der in Art. 7 Abs. 1 aufgefuehrten Behoerden"
    reference = "SR 361.2 Art. 7 Abs. 1"


class ipas_daten_fuer_empfaenger_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten sind zur Erfuellung der gesetzlichen Aufgabe der anfragenden Behoerde erforderlich"
    reference = "SR 361.2 Art. 7 Abs. 1"


class ipas_weitergabe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Weitergabe von IPAS-Daten an andere Behoerde ist zulaessig"
    reference = "SR 361.2 Art. 7"

    def formula(person, period, parameters):
        berechtigte = person('ipas_empfaenger_ist_berechtigte_behoerde', period)
        erforderlich = person('ipas_daten_fuer_empfaenger_erforderlich', period)
        return berechtigte * erforderlich
