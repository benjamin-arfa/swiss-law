"""SR 832.312.15 Art. 2 – Krane (Definition)

Generated from: ch/832/de/832.312.15.md

Krane sind Hebegeräte mit Tragfähigkeit >= 1000 kg oder Lastmoment >= 40000 Nm,
motorischem Hubwerk, horizontal verfahrbarem Kranhaken.
Kategorien: A (Fahrzeugkrane), B (Turmdrehkrane), C (übrige Krane).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

MIN_TRAGFAEHIGKEIT_KG = 1000
MIN_LASTMOMENT_NM = 40000
# Grenzwerte für Kategorie A bei Lastwagenladekranen (seit 1. Sept. 2023)
LWK_LASTMOMENT_GRENZE_NM = 400000
LWK_AUSLEGERLAENGE_GRENZE_M = 22


class tragfaehigkeit_kranhaken_kg(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Tragfähigkeit am Kranhaken (kg)"
    reference = "SR 832.312.15 Art. 2 Abs. 1 lit. a"


class lastmoment_nm(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Lastmoment des Gerätes (Nm)"
    reference = "SR 832.312.15 Art. 2 Abs. 1 lit. a"


class hat_motorisches_hubwerk(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gerät verfügt über ein motorisch angetriebenes Hubwerk"
    reference = "SR 832.312.15 Art. 2 Abs. 1 lit. b"


class kranhaken_horizontal_verfahrbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kranhaken kann horizontal in mindestens einer Achse frei verfahren werden"
    reference = "SR 832.312.15 Art. 2 Abs. 1 lit. c"


class ist_personenhebegeraet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gerät zum Heben von Personen (kein Kran)"
    reference = "SR 832.312.15 Art. 2 Abs. 3 lit. a"


class ist_baumaschine_erdbewegung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Baumaschine für Erdbewegungsarbeiten mit Lasthaken (kein Kran)"
    reference = "SR 832.312.15 Art. 2 Abs. 3 lit. b"


class ist_kran(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gerät qualifiziert als Kran im Sinne der Kranverordnung"
    reference = "SR 832.312.15 Art. 2"

    def formula(person, period, parameters):
        tragfaehigkeit = person('tragfaehigkeit_kranhaken_kg', period)
        lastmoment = person('lastmoment_nm', period)
        hubwerk = person('hat_motorisches_hubwerk', period)
        horizontal = person('kranhaken_horizontal_verfahrbar', period)
        personen = person('ist_personenhebegeraet', period)
        baumaschine = person('ist_baumaschine_erdbewegung', period)

        # Abs. 1: Alle drei Merkmale müssen erfüllt sein
        merkmal_a = (tragfaehigkeit >= MIN_TRAGFAEHIGKEIT_KG) + (lastmoment >= MIN_LASTMOMENT_NM)
        merkmale_erfuellt = merkmal_a * hubwerk * horizontal

        # Abs. 3: Ausnahmen
        return merkmale_erfuellt * not_(personen) * not_(baumaschine)
