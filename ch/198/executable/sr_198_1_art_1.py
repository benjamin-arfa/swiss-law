"""SR 198.1 Art. 1

Generated from: ch/198/de/198.1.md

Geltungsbereich: This law applies to activities in the Antarctic territory
as defined by Article VI of the Antarctic Treaty of 1 December 1959,
including expeditions, travel, supply trips and flights, construction,
modification, demolition or operation of scientific stations and other
facilities.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_taetigkeit_in_antarktis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Taetigkeit findet im Gebiet der Antarktis nach Art. VI des Antarktis-Vertrags statt"
    reference = "SR 198.1 Art. 1"


class ist_expedition(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Taetigkeit ist eine Expedition"
    reference = "SR 198.1 Art. 1"


class ist_versorgungsfahrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Taetigkeit ist eine Versorgungsfahrt oder ein Versorgungsflug"
    reference = "SR 198.1 Art. 1"


class ist_stationsbetrieb(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Taetigkeit betrifft Bau, Umbau, Abbau oder Betrieb wissenschaftlicher Stationen"
    reference = "SR 198.1 Art. 1"


class antarktis_gesetz_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Antarktis-Gesetz ist auf die Taetigkeit anwendbar"
    reference = "SR 198.1 Art. 1"

    def formula(person, period, parameters):
        in_antarktis = person('ist_taetigkeit_in_antarktis', period)
        return in_antarktis
