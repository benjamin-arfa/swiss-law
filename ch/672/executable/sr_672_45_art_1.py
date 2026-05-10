"""SR 672.45 Art. 1

Generated from: ch/672/de/672.45.md

Verordnung des EFD über die Verzinsung ausstehender Quellensteuerbeträge
Art. 1 - Verzugszins
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# --- Input variables ---

class quellensteuer_ueberweisung_verspaetet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Verspätete Überweisung der Einmalzahlungen, abgeltenden Steuern oder Abgeltungszahlungen gemäss Art. 24 Abs. 1 IQG"
    reference = "SR 672.45 Art. 1"


class quellensteuer_ausstehender_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Ausstehender Quellensteuerbetrag in CHF"
    reference = "SR 672.45 Art. 1"


# --- Computed variables ---

class quellensteuer_verzugszins_geschuldet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Verzugszins ist geschuldet bei verspäteter Überweisung (bestimmt sich nach SR 642.212)"
    reference = "SR 672.45 Art. 1"

    def formula(person, period, parameters):
        verspaetet = person('quellensteuer_ueberweisung_verspaetet', period)
        betrag = person('quellensteuer_ausstehender_betrag', period)
        return verspaetet * (betrag > 0)
