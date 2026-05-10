"""SR 235.1 Art. 14

Generated from: ch/235/de/235.1.md

Informationspflicht beim Beschaffen von besonders schuetzenswerten
Personendaten und Persoenlichkeitsprofilen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_beschaffung_besonders_schuetzenswert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Besonders schuetzenswerte Personendaten oder Persoenlichkeitsprofile werden beschafft"
    reference = "SR 235.1 Art. 14 Abs. 1"


class dsg_daten_bei_dritten_beschafft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten werden bei Dritten (nicht bei der betroffenen Person) beschafft"
    reference = "SR 235.1 Art. 14 Abs. 1"


class dsg_betroffene_bereits_informiert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Betroffene Person wurde bereits informiert"
    reference = "SR 235.1 Art. 14 Abs. 4"


class dsg_speicherung_bekanntgabe_gesetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Speicherung oder Bekanntgabe der Daten ist ausdruecklich im Gesetz vorgesehen"
    reference = "SR 235.1 Art. 14 Abs. 4 lit. a"


class dsg_information_unverhaeltnismaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Information ist nicht moeglich oder nur mit unverhaeltnismaessigem Aufwand"
    reference = "SR 235.1 Art. 14 Abs. 4 lit. b"


class dsg_informationspflicht_art14(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Informationspflicht nach Art. 14 DSG besteht"
    reference = "SR 235.1 Art. 14"

    def formula(person, period, parameters):
        besonders = person('dsg_beschaffung_besonders_schuetzenswert', period)
        bereits_informiert = person('dsg_betroffene_bereits_informiert', period)
        bei_dritten = person('dsg_daten_bei_dritten_beschafft', period)
        gesetzlich = person('dsg_speicherung_bekanntgabe_gesetzlich', period)
        unverhaeltnismaessig = person('dsg_information_unverhaeltnismaessig', period)

        # Informationspflicht bei Beschaffung besonders schuetzenswerter Daten
        # Entfaellt wenn: bereits informiert, oder bei Dritten beschafft und
        # gesetzlich vorgesehen oder unverhaeltnismaessig
        ausnahme_dritte = bei_dritten * (gesetzlich + unverhaeltnismaessig > 0)
        return besonders * not_(bereits_informiert) * not_(ausnahme_dritte)
