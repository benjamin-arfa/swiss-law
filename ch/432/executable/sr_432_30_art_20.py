"""SR 432.30 Art. 20

Generated from: ch/432/de/432.30.md

Steuern - Steuerbefreiung des SNM bei nichtgewerblichen Taetigkeiten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class taetigkeit_ist_gewerblich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit des SNM ist gewerblich (Art. 8)"
    reference = "SR 432.30 Art. 20 Abs. 3"


class snm_steuerbefreit_bund_kanton_gemeinde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SNM ist von Besteuerung durch Bund, Kantone und Gemeinden befreit"
    reference = "SR 432.30 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        return not_(person('taetigkeit_ist_gewerblich', period))


class snm_mehrwertsteuer_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mehrwertsteuer ist auf das SNM anwendbar (auch bei nichtgewerblicher Taetigkeit)"
    reference = "SR 432.30 Art. 20 Abs. 2 Bst. a"
    default_value = True


class snm_verrechnungssteuer_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verrechnungssteuer ist auf das SNM anwendbar (auch bei nichtgewerblicher Taetigkeit)"
    reference = "SR 432.30 Art. 20 Abs. 2 Bst. b"
    default_value = True


class snm_stempelabgaben_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Stempelabgaben sind auf das SNM anwendbar (auch bei nichtgewerblicher Taetigkeit)"
    reference = "SR 432.30 Art. 20 Abs. 2 Bst. c"
    default_value = True


class snm_gewinnsteuer_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewinnsteuer auf gewerbliche Taetigkeiten des SNM ist anwendbar"
    reference = "SR 432.30 Art. 20 Abs. 3"

    def formula(person, period, parameters):
        return person('taetigkeit_ist_gewerblich', period)
