"""SR 746.1 Art. 3

Generated from: ch/746/de/746.1.md

Verweigerung oder Einschraenkung der Plangenehmigung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class plangenehmigung_zu_verweigern(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Plangenehmigung ist zu verweigern oder nur unter Auflagen zu erteilen"
    reference = "SR 746.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: Verweigerung wenn Gefaehrdung von Personen/Sachen,
        # Stoerung oeffentlicher Werke, wesentliche oeffentliche Interessen,
        # Sicherheit des Landes, oder Anforderungen nach Art. 4 nicht erfuellt.
        gefaehrdet_personen_sachen = person('rohrleitung_gefaehrdet_personen_sachen', period)
        stoert_oeffentliches_werk = person('rohrleitung_stoert_oeffentliches_werk', period)
        sicherheit_landes = person('rohrleitung_betrifft_landessicherheit', period)
        anforderungen_art4 = ~person('erfuellt_anforderungen_art4_rlg', period)
        return (gefaehrdet_personen_sachen
                + stoert_oeffentliches_werk
                + sicherheit_landes
                + anforderungen_art4)


class rohrleitung_gefaehrdet_personen_sachen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bau oder Betrieb der Rohrleitungsanlage gefaehrdet Personen, Sachen oder wichtige Rechtsgueter"
    reference = "SR 746.1 Art. 3 Abs. 1 lit. a"


class rohrleitung_stoert_oeffentliches_werk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rohrleitungsanlage stoert bestehendes oeffentliches Werk oder verhindert geplantes Werk"
    reference = "SR 746.1 Art. 3 Abs. 1 lit. b"


class rohrleitung_betrifft_landessicherheit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheit des Landes oder Unabhaengigkeit/Neutralitaet der Schweiz erfordern Verweigerung"
    reference = "SR 746.1 Art. 3 Abs. 1 lit. d"


class erfuellt_anforderungen_art4_rlg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmung erfuellt die Anforderungen nach Art. 4 RLG"
    reference = "SR 746.1 Art. 4"
