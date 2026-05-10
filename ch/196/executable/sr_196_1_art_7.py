"""SR 196.1 Art. 7

Generated from: ch/196/de/196.1.md

Melde- und Auskunftspflicht: Personen und Institutionen die Vermoegenswerte
halten oder verwalten muessen diese der Meldestelle melden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class haelt_oder_verwaltet_gesperrte_vermoegenswerte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person/Institution in der Schweiz Vermoegenswerte von gesperrten Personen haelt oder verwaltet"
    reference = "SR 196.1 Art. 7 Abs. 1"


class weiss_von_gesperrten_vermoegenswerten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person aufgrund ihrer Aufgaben von gesperrten Vermoegenswerten weiss"
    reference = "SR 196.1 Art. 7 Abs. 2"


class ist_anwalt_oder_notar_mit_berufsgeheimnis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Anwaeltin/Anwalt oder Notarin/Notar ist und dem Berufsgeheimnis untersteht"
    reference = "SR 196.1 Art. 7 Abs. 5"


class meldepflicht_art_7(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person der Meldepflicht nach Art. 7 SRVG unterliegt"
    reference = "SR 196.1 Art. 7"

    def formula(person, period, parameters):
        haelt = person('haelt_oder_verwaltet_gesperrte_vermoegenswerte', period)
        weiss = person('weiss_von_gesperrten_vermoegenswerten', period)
        ausnahme = person('ist_anwalt_oder_notar_mit_berufsgeheimnis', period)
        return (haelt + weiss > 0) * (1 - ausnahme)
