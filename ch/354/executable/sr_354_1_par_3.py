"""SR 354.1 § 3

Generated from: ch/354/de/354.1.md
Cost categories for cantonal police transports.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transportkategorie(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Transportkategorie (1=empfangender Kanton, 2=Bund, 3=absendender Kanton)"
    reference = "SR 354.1 § 3"

    def formula(person, period):
        requirierte_person = person('ist_requirierte_person', period)
        ausgewiesene_aus_ausland = person('ist_ausgewiesene_person_aus_ausland', period)
        abschiebung_ins_ausland = person('ist_abschiebung_ins_ausland', period)

        # Kategorie I: empfangender Kanton traegt Kosten
        kategorie_1 = requirierte_person + ausgewiesene_aus_ausland

        # Kategorie II: Bund traegt Kosten (Abschiebung ins Ausland)
        kategorie_2 = abschiebung_ins_ausland

        # Kategorie III: absendender Kanton (alle uebrigen)
        return where(kategorie_1 > 0, 1, where(kategorie_2, 2, 3))


class ist_requirierte_person(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person wurde von einem Kanton requiriert oder dessen Strafverfolgung obliegt ihm"
    reference = "SR 354.1 § 3 Kat. I lit. a"


class ist_ausgewiesene_person_aus_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausgewiesene Schweizer Angehoerige treffen vom Ausland an der Grenze ein"
    reference = "SR 354.1 § 3 Kat. I lit. b"


class ist_abschiebung_ins_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Abschiebung oder Heimschaffung aus der Schweiz nach dem Ausland"
    reference = "SR 354.1 § 3 Kat. II"


class kostentraeger(Variable):
    value_type = str
    max_length = 30
    entity = Person
    definition_period = YEAR
    label = "Wer traegt die Fahrkosten des Polizeitransports"
    reference = "SR 354.1 § 3"

    def formula(person, period):
        kategorie = person('transportkategorie', period)
        # 1 = empfangender Kanton, 2 = Bund, 3 = absendender Kanton
        return where(kategorie == 1, 'empfangender_kanton',
                     where(kategorie == 2, 'bund', 'absendender_kanton'))
