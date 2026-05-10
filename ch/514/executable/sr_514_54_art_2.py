"""SR 514.54 Art. 2

Generated from: ch/514/de/514.54.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_feuerwaffe_hergestellt_vor_1870(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Feuerwaffe wurde vor 1870 hergestellt"


class ist_hieb_stich_waffe_hergestellt_vor_1900(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hieb-, Stich- oder andere Waffe wurde vor 1900 hergestellt"


class ist_antike_waffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gegenstand gilt als antike Waffe (Art. 2 Abs. 2 SR 514.54)"
    reference = "SR 514.54 Art. 2"

    def formula(person, period, parameters):
        # Als antike Waffen gelten:
        # - vor 1870 hergestellte Feuerwaffen
        # - vor 1900 hergestellte Hieb-, Stich- und andere Waffen
        feuerwaffe_alt = person('ist_feuerwaffe_hergestellt_vor_1870', period)
        andere_waffe_alt = person('ist_hieb_stich_waffe_hergestellt_vor_1900', period)
        return feuerwaffe_alt + andere_waffe_alt


class waffengesetz_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Waffengesetz ist anwendbar (Art. 2 SR 514.54)"
    reference = "SR 514.54 Art. 2"

    def formula(person, period, parameters):
        # Fuer antike Waffen gelten nur Art. 27 und 28 + Strafbestimmungen
        # Das Gesetz gilt nicht fuer Armee, NDB, Zoll- und Polizeibehoerden
        antik = person('ist_antike_waffe', period)
        # Volle Anwendbarkeit nur wenn nicht antik
        # (bei antiken Waffen gilt eingeschraenkt Art. 27/28)
        return antik == False
