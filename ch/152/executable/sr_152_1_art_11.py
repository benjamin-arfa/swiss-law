"""SR 152.1 Art. 11

Generated from: ch/152/de/152.1.md

Verlaengerte Schutzfrist fuer Personendaten: 50 Jahre, endet 3 Jahre
nach Tod der betroffenen Person.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class archivgut_enthaelt_personendaten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Archivgut nach Personennamen erschlossen ist und besonders schuetzenswerte Personendaten enthaelt"
    reference = "SR 152.1 Art. 11 Abs. 1"


class betroffene_person_hat_zugestimmt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die betroffene Person der Einsichtnahme zugestimmt hat"
    reference = "SR 152.1 Art. 11 Abs. 1"


class jahre_seit_tod_betroffene_person(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahre seit dem Tod der betroffenen Person (-1 wenn noch lebend)"
    reference = "SR 152.1 Art. 11 Abs. 2"


class verlaengerte_schutzfrist_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die verlaengerte 50-jaehrige Schutzfrist abgelaufen ist"
    reference = "SR 152.1 Art. 11"

    def formula(person, period, parameters):
        hat_personendaten = person('archivgut_enthaelt_personendaten', period)
        zugestimmt = person('betroffene_person_hat_zugestimmt', period)
        datum = person('datum_juengstes_dokument', period)
        aktuell = person('aktuelles_jahr', period)
        jahre_tod = person('jahre_seit_tod_betroffene_person', period)

        frist_50_jahre = (aktuell - datum) >= 50
        tod_3_jahre = (jahre_tod >= 0) * (jahre_tod >= 3)

        # Schutzfrist endet: 50 Jahre abgelaufen ODER 3 Jahre nach Tod ODER Zustimmung
        return hat_personendaten * (frist_50_jahre + tod_3_jahre + zugestimmt > 0) + (1 - hat_personendaten)
