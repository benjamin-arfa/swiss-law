"""SR 360.2 Art. 11

Generated from: ch/360/de/360.2.md

Zugriff im Allgemeinen: Aufzaehlung zugriffsberechtigter Stellen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_stelle_in_zugriffsliste(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Stelle ist in der Liste der zugriffsberechtigten Stellen nach Art. 11 Abs. 1"
    reference = "SR 360.2 Art. 11 Abs. 1"


class nes_aufgabe_erfordert_zugriff(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesetzlicher Auftrag erfordert Zugriff auf NES"
    reference = "SR 360.2 Art. 11 Abs. 1"


class nes_online_zugriff_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Online-Zugriff auf das NES ist berechtigt"
    reference = "SR 360.2 Art. 11"

    def formula(person, period, parameters):
        in_liste = person('nes_stelle_in_zugriffsliste', period)
        aufgabe = person('nes_aufgabe_erfordert_zugriff', period)
        return in_liste * aufgabe
