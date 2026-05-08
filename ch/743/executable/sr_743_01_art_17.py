"""SR 743.01 Art. 17

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Betriebsbewilligung.
Voraussetzungen: Sicherheitsnachweis, grundlegende Anforderungen,
Plangenehmigung-Auflagen, Versicherungsnachweis, Betriebs-/Bergungsorganisation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_sicherheitsnachweis_erbracht(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob der Sicherheitsnachweis und die Sicherheitsgutachten vorliegen"
    reference = "SR 743.01 Art. 17 Abs. 3 Bst. a"


class seilbahn_betrieb_grundlegende_anforderungen(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die grundlegenden Anforderungen fuer den Betrieb erfuellt sind"
    reference = "SR 743.01 Art. 17 Abs. 3 Bst. b"


class seilbahn_auflagen_plangenehmigung_erfuellt(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Auflagen der Plangenehmigung und Konzession erfuellt sind"
    reference = "SR 743.01 Art. 17 Abs. 3 Bst. c"


class seilbahn_versicherungsnachweis_vorhanden(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob ein Versicherungsnachweis gemaess Art. 21 vorliegt"
    reference = "SR 743.01 Art. 17 Abs. 3 Bst. d"


class seilbahn_betriebs_und_bergungsorganisation(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob Betriebs-/Instandhaltungs-/Bergungsorganisation und Personal vorhanden sind"
    reference = "SR 743.01 Art. 17 Abs. 3 Bst. e"


class seilbahn_betriebsbewilligung_erteilt(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Betriebsbewilligung erteilt wird"
    reference = "SR 743.01 Art. 17 Abs. 3"

    def formula(organisation, period, parameters):
        sicherheit = organisation('seilbahn_sicherheitsnachweis_erbracht', period)
        anforderungen = organisation('seilbahn_betrieb_grundlegende_anforderungen', period)
        auflagen = organisation('seilbahn_auflagen_plangenehmigung_erfuellt', period)
        versicherung = organisation('seilbahn_versicherungsnachweis_vorhanden', period)
        organisation_vorhanden = organisation('seilbahn_betriebs_und_bergungsorganisation', period)
        return sicherheit * anforderungen * auflagen * versicherung * organisation_vorhanden
