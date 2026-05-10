"""SR 282.11 Art. 37 - Steuer- und Abgabenerhebung durch die Beiratschaft

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class steuererhoehung_notwendig_und_zweckmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Steuererhoehung ist notwendig und nach den gegebenen Verhaeltnissen zweckmaessig und tragbar"
    reference = "SR 282.11 Art. 37 Abs. 1"


class zustimmung_kantonsregierung_steuer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Kantonsregierung hat der Steuererhoehung oder -einfuehrung zugestimmt"
    reference = "SR 282.11 Art. 37 Abs. 1"


class schuldnerin_zur_steuereinfuehrung_ermaechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schuldnerin waere nach kantonalem Recht zur Einfuehrung der Steuer ermaechtigt"
    reference = "SR 282.11 Art. 37 Abs. 2"


# Computed variables

class beiratschaft_darf_steuern_erhoehen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Beiratschaft darf bestehende Steuern und Abgaben erhoehen"
    reference = "SR 282.11 Art. 37 Abs. 1"

    def formula(self, period, parameters):
        notwendig = self('steuererhoehung_notwendig_und_zweckmaessig', period)
        zustimmung = self('zustimmung_kantonsregierung_steuer', period)
        return notwendig * zustimmung


class beiratschaft_darf_steuern_einfuehren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Beiratschaft darf neue Steuern und Abgaben einfuehren"
    reference = "SR 282.11 Art. 37 Abs. 2"

    def formula(self, period, parameters):
        notwendig = self('steuererhoehung_notwendig_und_zweckmaessig', period)
        zustimmung = self('zustimmung_kantonsregierung_steuer', period)
        ermaechtigt = self('schuldnerin_zur_steuereinfuehrung_ermaechtigt', period)
        return notwendig * zustimmung * ermaechtigt
