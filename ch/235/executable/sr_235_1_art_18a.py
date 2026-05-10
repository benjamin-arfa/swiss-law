"""SR 235.1 Art. 18a

Generated from: ch/235/de/235.1.md

Informationspflicht beim Beschaffen von Personendaten durch Bundesorgane.
Similar structure to Art. 14 but for all personal data by federal organs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_bundesorgan_beschafft_daten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bundesorgan beschafft Personendaten"
    reference = "SR 235.1 Art. 18a Abs. 1"


class dsg_informationspflicht_bundesorgan(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bundesorgan hat Informationspflicht bei Beschaffung von Personendaten"
    reference = "SR 235.1 Art. 18a"

    def formula(person, period, parameters):
        beschafft = person('dsg_bundesorgan_beschafft_daten', period)
        bereits_informiert = person('dsg_betroffene_bereits_informiert', period)
        bei_dritten = person('dsg_daten_bei_dritten_beschafft', period)
        gesetzlich = person('dsg_speicherung_bekanntgabe_gesetzlich', period)
        unverhaeltnismaessig = person('dsg_information_unverhaeltnismaessig', period)

        ausnahme_dritte = bei_dritten * (gesetzlich + unverhaeltnismaessig > 0)
        return beschafft * not_(bereits_informiert) * not_(ausnahme_dritte)
