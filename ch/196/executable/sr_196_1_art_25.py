"""SR 196.1 Art. 25

Generated from: ch/196/de/196.1.md

Verletzung der Vermoegenssperre: Strafbestimmung fuer unbewilligte Zahlungen
oder Uebertragungen aus gesperrten Konten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_vermoegenssperre_vorsaetzlich_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person vorsaetzlich ohne Bewilligung Zahlungen aus gesperrten Konten getaetigt oder Vermoegenswerte freigegeben hat"
    reference = "SR 196.1 Art. 25 Abs. 1"


class hat_vermoegenssperre_fahrlaessig_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person fahrlaessig die Vermoegenssperre verletzt hat"
    reference = "SR 196.1 Art. 25 Abs. 2"


class maximale_freiheitsstrafe_art_25_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Freiheitsstrafe in Jahren bei vorsaetzlicher Verletzung der Vermoegenssperre"
    reference = "SR 196.1 Art. 25 Abs. 1"

    def formula(person, period, parameters):
        vorsatz = person('hat_vermoegenssperre_vorsaetzlich_verletzt', period)
        return vorsatz * 3


class maximale_busse_art_25(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse in CHF bei fahrlaessiger Verletzung der Vermoegenssperre"
    reference = "SR 196.1 Art. 25 Abs. 2"

    def formula(person, period, parameters):
        fahrlaessig = person('hat_vermoegenssperre_fahrlaessig_verletzt', period)
        return fahrlaessig * 250000
