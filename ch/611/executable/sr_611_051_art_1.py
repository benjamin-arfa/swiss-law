"""SR 611.051 Art. 1

Generated from: ch/611/de/611.051.md

Verordnung der Bundesversammlung über die Verpflichtungskreditbegehren
für Grundstücke und Bauten. Art. 1: Schwellenwert für besondere Botschaft
bei Verpflichtungskrediten (10 Mio. CHF).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class gesamtausgaben_projekt_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Für den Bund zu erwartende Gesamtausgaben pro Projekt in CHF"
    reference = "SR 611.051 Art. 1 Abs. 1"


class ist_eth_bereich_projekt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Projekt betrifft den ETH-Bereich"
    reference = "SR 611.051 Art. 1 Abs. 1"


class schwellenwert_besondere_botschaft_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schwellenwert für besondere Botschaft bei Verpflichtungskrediten in CHF"
    reference = "SR 611.051 Art. 1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 1: 10 Millionen Franken
        return 10_000_000


class erfordert_besondere_botschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Verpflichtungskreditbegehren muss mit besonderer Botschaft "
        "unterbreitet werden (Art. 1 Abs. 1)"
    )
    reference = "SR 611.051 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 1: Besondere Botschaft wenn > 10 Mio., ausgenommen ETH
        ausgaben = person('gesamtausgaben_projekt_chf', period)
        ist_eth = person('ist_eth_bereich_projekt', period)
        schwelle = person('schwellenwert_besondere_botschaft_chf', period)
        return (ausgaben > schwelle) * (1 - ist_eth)


class voranschlag_verfahren_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Verpflichtungskredit kann ohne besondere Botschaft mit Voranschlag "
        "oder Nachtrag angefordert werden (Art. 1 Abs. 2)"
    )
    reference = "SR 611.051 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        # Art. 1 Abs. 2: Wenn Ausgabe <= 10 Mio. CHF
        ausgaben = person('gesamtausgaben_projekt_chf', period)
        schwelle = person('schwellenwert_besondere_botschaft_chf', period)
        ist_eth = person('ist_eth_bereich_projekt', period)
        landesverteidigung_geheim = person('ist_landesverteidigung_geheim', period)
        return (ausgaben <= schwelle) + ist_eth + landesverteidigung_geheim


class ist_landesverteidigung_geheim(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorhaben muss im Interesse der Landesverteidigung geheimgehalten werden"
    reference = "SR 611.051 Art. 1 Abs. 2"
