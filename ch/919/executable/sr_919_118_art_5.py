"""SR 919.118 Art. 5

Generated from: ch/919/de/919.118.md

Bestimmung des landwirtschaftlichen Arbeitsverdienstes.

Abs. 1: Arbeitsverdienst wird auf der Grundlage einer vollzeitlich beschaeftigten
Person berechnet. Teilzeitpersonen im Verhaeltnis zu 280 Arbeitstagen.
Eine Person kann nicht mehr als einer Arbeitseinheit entsprechen.

Abs. 2: Arbeitsverdienst = landwirtschaftliches Einkommen - (Eigenkapital * Zinssatz).
Zinssatz = mittlerer Zinssatz fuer Bundesobligationen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class arbeitseinheiten_person(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Arbeitseinheiten einer Person (max 1.0, Basis 280 Arbeitstage)"
    reference = "SR 919.118 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        arbeitstage_auf_betrieb = person('arbeitstage_auf_betrieb', period)
        basis_arbeitstage = 280
        raw = arbeitstage_auf_betrieb / basis_arbeitstage
        return min_(raw, 1.0)


class landwirtschaftlicher_arbeitsverdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Landwirtschaftlicher Arbeitsverdienst pro Arbeitseinheit (CHF)"
    reference = "SR 919.118 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        landw_einkommen = person('landwirtschaftliches_einkommen', period)
        eigenkapital = person('eingesetztes_eigenkapital', period)
        zinssatz = parameters(period).sr_919_118.zinssatz_bundesobligationen
        zinsabzug = eigenkapital * zinssatz
        arbeitsverdienst = landw_einkommen - zinsabzug
        arbeitseinheiten = person('arbeitseinheiten_person', period)
        return where(arbeitseinheiten > 0, arbeitsverdienst / arbeitseinheiten, 0)


class arbeitstage_auf_betrieb(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Arbeitstage auf dem landwirtschaftlichen Betrieb"
    reference = "SR 919.118 Art. 5 Abs. 1"


class landwirtschaftliches_einkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Landwirtschaftliches Einkommen (CHF)"
    reference = "SR 919.118 Art. 5 Abs. 2"


class eingesetztes_eigenkapital(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eingesetztes Eigenkapital im Landwirtschaftsbetrieb (CHF)"
    reference = "SR 919.118 Art. 5 Abs. 2"
