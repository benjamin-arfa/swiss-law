"""SR 152.11 Art. 4

Generated from: ch/152/de/152.11.md

Eintritt der Anbietepflicht: spaetestens 5 Jahre nach letztem Aktenzuwachs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahr_letzter_aktenzuwachs(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahr des letzten Aktenzuwachses"
    reference = "SR 152.11 Art. 4 Abs. 1"


class stelle_benoetigt_unterlagen_weiterhin(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die anbietepflichtige Stelle die Unterlagen weiterhin benoetigt"
    reference = "SR 152.11 Art. 4 Abs. 2"


class anbietepflicht_eingetreten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Anbietepflicht eingetreten ist (5 Jahre seit letztem Aktenzuwachs)"
    reference = "SR 152.11 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        letzter_zuwachs = person('jahr_letzter_aktenzuwachs', period)
        aktuell = person('aktuelles_jahr', period)
        benoetigt = person('stelle_benoetigt_unterlagen_weiterhin', period)
        frist_abgelaufen = (aktuell - letzter_zuwachs) >= 5
        return frist_abgelaufen * (1 - benoetigt)
