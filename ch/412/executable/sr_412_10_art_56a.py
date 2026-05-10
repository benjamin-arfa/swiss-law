"""SR 412.10 Art. 56a

Generated from: ch/412/de/412.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anrechenbare_kursgebuehren(Variable):
    """Anrechenbare Kursgebuehren fuer vorbereitende Kurse"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Kursgebuehren in CHF"
    reference = "SR 412.10 Art. 56a Abs. 2"


class hat_vorbereitenden_kurs_absolviert(Variable):
    """Ob die Person einen vorbereitenden Kurs absolviert hat"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat vorbereitenden Kurs auf eidg. Pruefung absolviert"
    reference = "SR 412.10 Art. 56a Abs. 1"
    default_value = False


class bundesbeitrag_vorbereitungskurs(Variable):
    """Maximaler Bundesbeitrag: hoechstens 50% der anrechenbaren Kursgebuehren"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bundesbeitrag an Absolventinnen vorbereitender Kurse (max. 50%)"
    reference = "SR 412.10 Art. 56a Abs. 2"

    def formula(person, period, parameters):
        kursgebuehren = person('anrechenbare_kursgebuehren', period)
        hat_kurs = person('hat_vorbereitenden_kurs_absolviert', period)
        max_beitrag = kursgebuehren * 0.5
        return hat_kurs * max_beitrag
