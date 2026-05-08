"""SR 836.1 Art. 3

Generated from: ch/836/de/836.1.md

Art. 3: Haushaltungszulage - Conditions for receiving the household allowance:
Abs. 1: Employees maintaining a household with spouse or children.
Abs. 2: If both spouses are entitled, only one allowance paid (50% each).
Abs. 3: Widowed employees without children: max 1 year after death of spouse.
Abs. 4: Entitlement begins first day of month household is established,
        ends at end of month household is dissolved.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class fuehrt_haushalt_mit_ehegatte_oder_kindern(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitnehmer führt gemeinsamen Haushalt mit Ehegatten oder Kindern (Art. 3 Abs. 1 lit. a)"
    reference = "SR 836.1 Art. 3 Abs. 1 lit. a"


class lebt_in_hausgemeinschaft_arbeitgeber(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitnehmer lebt in Hausgemeinschaft mit dem Arbeitgeber"
    reference = "SR 836.1 Art. 3 Abs. 1 lit. b"


class ehegatte_oder_kinder_fuehren_eigenen_haushalt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ehegatte oder Kinder führen eigenen Haushalt, für dessen Kosten der AN aufkommt"
    reference = "SR 836.1 Art. 3 Abs. 1 lit. b"


class ehegatte_und_kinder_in_hausgemeinschaft_arbeitgeber(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitnehmer lebt mit Ehegatte/Kindern in Hausgemeinschaft mit Arbeitgeber"
    reference = "SR 836.1 Art. 3 Abs. 1 lit. c"


class beide_ehegatten_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beide Ehegatten sind als landwirtschaftliche Arbeitnehmer bezugsberechtigt"
    reference = "SR 836.1 Art. 3 Abs. 2"


class ist_verwitwet_ohne_kinder(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist verwitwet und hat keine Kinder"
    reference = "SR 836.1 Art. 3 Abs. 3"


class monate_seit_tod_ehegatte(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Monate seit dem Tod des Ehegatten"
    reference = "SR 836.1 Art. 3 Abs. 3"


class anspruch_haushaltungszulage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf Haushaltungszulage (Art. 3 FLG)"
    reference = "SR 836.1 Art. 3"

    def formula(person, period, parameters):
        # Abs. 1 lit. a: gemeinsamer Haushalt mit Ehegatte/Kindern
        lit_a = person('fuehrt_haushalt_mit_ehegatte_oder_kindern', period)
        # Abs. 1 lit. b: Hausgemeinschaft mit AG, Familie hat eigenen Haushalt
        hausgemeinschaft = person('lebt_in_hausgemeinschaft_arbeitgeber', period)
        eigener_haushalt = person('ehegatte_oder_kinder_fuehren_eigenen_haushalt', period)
        lit_b = hausgemeinschaft * eigener_haushalt
        # Abs. 1 lit. c: mit Familie in Hausgemeinschaft mit AG
        lit_c = person('ehegatte_und_kinder_in_hausgemeinschaft_arbeitgeber', period)
        # Abs. 3: Verwitwet ohne Kinder, max 12 Monate
        verwitwet = person('ist_verwitwet_ohne_kinder', period)
        monate = person('monate_seit_tod_ehegatte', period)
        abs_3 = verwitwet * (monate <= 12)

        return lit_a + lit_b + lit_c + abs_3 > 0


class betrag_haushaltungszulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Monatlicher Betrag der Haushaltungszulage (Art. 2 Abs. 2 / Art. 3 FLG)"
    reference = "SR 836.1 Art. 3"

    def formula(person, period, parameters):
        anspruch = person('anspruch_haushaltungszulage', period)
        beide = person('beide_ehegatten_berechtigt', period)
        # Art. 2 Abs. 2: 100 CHF; Art. 3 Abs. 2: nur eine Zulage, je 50%
        voller_betrag = 100.0
        betrag = where(beide, voller_betrag / 2, voller_betrag)
        return anspruch * betrag
