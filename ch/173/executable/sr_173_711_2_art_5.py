"""SR 173.711.2 Art. 5

Generated from: ch/173/de/173.711.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class richter_alter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter des Richters/der Richterin"
    reference = "SR 173.711.2 Art. 5"

class richter_erfahrung_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Monate Richtererfahrung (hauptamtlich an oberem Gericht oder Strafverfolgung)"
    reference = "SR 173.711.2 Art. 5"

class richter_lohn_reduktion_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Lohnreduktion in Prozent gegenueber Hoechstbetrag Lohnklasse 33 (Art. 5 Abs. 3)"
    reference = "SR 173.711.2 Art. 5"

    def formula(person, period, parameters):
        alter = person('richter_alter', period)
        erfahrung = person('richter_erfahrung_monate', period)
        # Art. 5 Abs. 2: Hoechstbetrag bei Alter >= 45 UND Erfahrung >= 48 Monate
        # Art. 5 Abs. 3: -7.5% wenn ein Kriterium nicht erfuellt, -15% wenn beide nicht erfuellt
        kriterium_alter = alter >= 45
        kriterium_erfahrung = erfahrung >= 48
        beide_erfuellt = kriterium_alter * kriterium_erfahrung
        eines_erfuellt = (kriterium_alter + kriterium_erfahrung) > 0
        return where(beide_erfuellt, 0.0,
               where(eines_erfuellt, 7.5, 15.0))
