"""SR 173.711.2 Art. 6

Generated from: ch/173/de/173.711.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_praesident_gericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Praesident/in des Gerichts"
    reference = "SR 173.711.2 Art. 6"

class ist_vizepraesident_gericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Vizepraesident/in des Gerichts"
    reference = "SR 173.711.2 Art. 6"

class ist_kammervorsitzender(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Praesident/in einer Kammer oder Abteilung"
    reference = "SR 173.711.2 Art. 6"

class ist_kammervorsitzender_bvger_oder_vizekammer_bstger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Kammervorsitzende/r BVGer oder Vizekammervorsitzende/r BStGer"
    reference = "SR 173.711.2 Art. 6"

class praesidialzulage_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Praesidialzulage in CHF pro Jahr (Art. 6)"
    reference = "SR 173.711.2 Art. 6"

    def formula(person, period, parameters):
        praesident = person('ist_praesident_gericht', period)
        vizepraesident = person('ist_vizepraesident_gericht', period)
        kammervorsitzender = person('ist_kammervorsitzender', period)
        kammer_bvger = person('ist_kammervorsitzender_bvger_oder_vizekammer_bstger', period)
        # Art. 6: Hoechste Zulage gilt (Abs. 5)
        # Praesident: 30'000, Vizepraesident: 20'000, Kammer/Abteilung: 10'000, Kammer BVGer: 5'000
        return where(praesident, 30000,
               where(vizepraesident, 20000,
               where(kammervorsitzender, 10000,
               where(kammer_bvger, 5000, 0))))
