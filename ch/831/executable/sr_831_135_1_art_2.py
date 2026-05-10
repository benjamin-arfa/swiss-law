"""SR 831.135.1 Art. 2

Generated from: ch/831/de/831.135.1.md

Art. 2: Anspruch auf Hilfsmittel - Entitlement to aids.

Abs. 1: Residents of Switzerland receiving AHV old-age pensions who
depend on aids for their activities, mobility, contact with the
environment, or self-care are entitled to benefits listed in the annex.

Abs. 2: Unless the annex specifies otherwise, the insurance pays a
cost contribution of 75% of the net price.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hva_bezieht_altersrente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person bezieht eine Altersrente der AHV"
    reference = "SR 831.135.1 Art. 2 Abs. 1"


class hva_wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person hat Wohnsitz in der Schweiz"
    reference = "SR 831.135.1 Art. 2 Abs. 1"


class hva_auf_hilfsmittel_angewiesen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist auf Hilfsmittel angewiesen (Aufgabenbereich, Fortbewegung, Kontakt, Selbstsorge)"
    reference = "SR 831.135.1 Art. 2 Abs. 1"


class hva_anspruch_hilfsmittel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Hilfsmittel der AHV (Art. 2 HVA)"
    reference = "SR 831.135.1 Art. 2"

    def formula(person, period, parameters):
        rente = person('hva_bezieht_altersrente', period)
        wohnsitz = person('hva_wohnsitz_schweiz', period)
        angewiesen = person('hva_auf_hilfsmittel_angewiesen', period)
        return rente * wohnsitz * angewiesen


class hva_nettopreis_hilfsmittel(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Nettopreis des beantragten Hilfsmittels"
    reference = "SR 831.135.1 Art. 2 Abs. 2"


class hva_kostenbeitrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kostenbeitrag der Versicherung an Hilfsmittel (75% des Nettopreises, Art. 2 Abs. 2 HVA)"
    reference = "SR 831.135.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        anspruch = person('hva_anspruch_hilfsmittel', period)
        nettopreis = person('hva_nettopreis_hilfsmittel', period)
        return anspruch * nettopreis * 0.75
