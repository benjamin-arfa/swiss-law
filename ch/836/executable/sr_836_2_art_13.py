"""SR 836.2 Art. 13

Generated from: ch/836/de/836.2.md

Art. 13: Anspruch auf Familienzulagen als Arbeitnehmer.
Abs. 1: AHV-obligatorisch versicherte Arbeitnehmer, die von einem
dem FamZG unterstellten Arbeitgeber beschaeftigt werden, haben
Anspruch auf Familienzulagen. Anspruch entsteht und erlischt mit
dem Lohnanspruch. Art. 10 FamZV bleibt vorbehalten.
Abs. 1bis: Mindestlohn fuer Anspruch: 612 CHF/Monat (= 7350 CHF/Jahr,
Stand 2025). Unter diesem Betrag kein Anspruch als Arbeitnehmer,
aber ggf. als Nichterwerbstaetiger (Art. 19).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_ahv_obligatorisch_versichert(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist in der AHV obligatorisch versichert"
    reference = "SR 836.2 Art. 13 Abs. 1"


class monatslohn(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Monatlicher Bruttolohn"
    reference = "SR 836.2 Art. 13 Abs. 1bis"


class mindestlohn_familienzulage(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Mindestlohn fuer Anspruch auf Familienzulagen als Arbeitnehmer (Art. 13 Abs. 1bis)"
    reference = "SR 836.2 Art. 13 Abs. 1bis"

    def formula(person, period, parameters):
        # 7350 CHF/Jahr = 612.50 CHF/Monat (Stand 2025, entspricht
        # Art. 34d Abs. 1 AHVV, angepasst gemaess Art. 5 Abs. 4 FamZG)
        return 612.50


class hat_lohnanspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hat im aktuellen Monat einen Lohnanspruch"
    reference = "SR 836.2 Art. 13 Abs. 1"


class anspruch_familienzulage_arbeitnehmer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf Familienzulagen als Arbeitnehmer (Art. 13 FamZG)"
    reference = "SR 836.2 Art. 13"

    def formula(person, period, parameters):
        ahv_versichert = person('ist_ahv_obligatorisch_versichert', period)
        unterstellt = person('unterstellt_famzg', period)
        lohn = person('monatslohn', period)
        mindestlohn = person('mindestlohn_familienzulage', period)
        lohnanspruch = person('hat_lohnanspruch', period)

        # Abs. 1: AHV-versichert + unterstellter Arbeitgeber + Lohnanspruch
        # Abs. 1bis: Mindestlohn muss erreicht werden
        return ahv_versichert * unterstellt * lohnanspruch * (lohn >= mindestlohn)
