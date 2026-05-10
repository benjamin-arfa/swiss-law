"""SR 414.110 Art. 16

Generated from: ch/414/de/414.110.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_eidg_maturitaetsausweis(Variable):
    """Besitz eines eidg. oder eidg. anerkannten Maturitaetsausweises"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besitzt eidg. oder anerkannten Maturitaetsausweis"
    reference = "SR 414.110 Art. 16 Abs. 1 Bst. a"
    default_value = False


class hat_gleichwertigen_ausweis(Variable):
    """Besitz eines gleichwertigen Ausweises einer CH/LI Mittelschule"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besitzt gleichwertigen Ausweis einer CH/LI Mittelschule"
    reference = "SR 414.110 Art. 16 Abs. 1 Bst. a"
    default_value = False


class hat_anderen_anerkannten_abschluss(Variable):
    """Besitz eines von der Schulleitung anerkannten Abschlusses"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besitzt anderen von Schulleitung anerkannten Abschluss"
    reference = "SR 414.110 Art. 16 Abs. 1 Bst. b"
    default_value = False


class hat_fachhochschuldiplom(Variable):
    """Besitz eines Diploms einer schweizerischen Fachhochschule"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besitzt Diplom einer schweizerischen Fachhochschule"
    reference = "SR 414.110 Art. 16 Abs. 1 Bst. c"
    default_value = False


class hat_aufnahmepruefung_bestanden(Variable):
    """Hat die Aufnahmepruefung bestanden"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Aufnahmepruefung bestanden"
    reference = "SR 414.110 Art. 16 Abs. 1 Bst. d"
    default_value = False


class zulassung_eth_bachelor_erstes_semester(Variable):
    """Ob die Zulassung zum ersten Semester des Bachelorstudiums an ETH gegeben ist"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zulassung zum Bachelor-Erststemester an ETH"
    reference = "SR 414.110 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        matura = person('hat_eidg_maturitaetsausweis', period)
        gleichwertig = person('hat_gleichwertigen_ausweis', period)
        anderer_abschluss = person('hat_anderen_anerkannten_abschluss', period)
        fh_diplom = person('hat_fachhochschuldiplom', period)
        aufnahme = person('hat_aufnahmepruefung_bestanden', period)
        return matura + gleichwertig + anderer_abschluss + fh_diplom + aufnahme > 0
