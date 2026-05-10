"""SR 429.1 Art. 3

Generated from: ch/429/de/429.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 3 - Grundangebot an Dienstleistungen
# Regelt das Grundangebot und die Gebuehrenfreiheit bzw. Gebuehrenerhebung.

# --- Input variables (Fakten, die extern geliefert werden muessen) ---

class ist_grundangebot_dienstleistung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Dienstleistung gehoert zum Grundangebot nach Art. 3 Abs. 1 MetG"
    reference = "SR 429.1 Art. 3 Abs. 1"


class ist_open_government_data(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten nach Art. 10 Abs. 1 EMBAG (Open Government Data)"
    reference = "SR 429.1 Art. 3 Abs. 3 lit. a"


class ist_wetterwarnung_oder_klimainfo(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wetter-/Klimainformation im Interesse der Allgemeinheit (Warnungen, Vorhersagen, Klimagrundlagen)"
    reference = "SR 429.1 Art. 3 Abs. 3 lit. b"


class ist_eingeschraenkter_nutzerkreis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten werden nur von einem eingeschraenkten Nutzerkreis verwendet und erfordern bedeutende zusaetzliche Mittel"
    reference = "SR 429.1 Art. 3 Abs. 4 lit. a"


class ist_spezialgesetzlicher_auftrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten/Dienstleistungen werden aufgrund spezialgesetzlicher Auftraege oder auf Anfrage generiert"
    reference = "SR 429.1 Art. 3 Abs. 4 lit. b"


# --- Computed variables ---

class grundangebot_unentgeltlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Leistung wird unentgeltlich erbracht (Art. 3 Abs. 3 MetG)"
    reference = "SR 429.1 Art. 3 Abs. 3"

    def formula(self, period, parameters):
        ist_ogd = self('ist_open_government_data', period)
        ist_warnung = self('ist_wetterwarnung_oder_klimainfo', period)
        return ist_ogd + ist_warnung > 0


class grundangebot_gebuehrenpflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuer die Leistung koennen Gebuehren erhoben werden (Art. 3 Abs. 4 MetG)"
    reference = "SR 429.1 Art. 3 Abs. 4"

    def formula(self, period, parameters):
        ist_grundangebot = self('ist_grundangebot_dienstleistung', period)
        eingeschraenkt = self('ist_eingeschraenkter_nutzerkreis', period)
        spezial = self('ist_spezialgesetzlicher_auftrag', period)
        unentgeltlich = self('grundangebot_unentgeltlich', period)
        # Gebuehren moeglich wenn Grundangebot, aber nicht unentgeltlich,
        # und entweder eingeschraenkter Nutzerkreis oder spezialgesetzlicher Auftrag
        return ist_grundangebot * (1 - unentgeltlich) * ((eingeschraenkt + spezial) > 0)
