"""SR 142.318 Art. 4

Generated from: ch/142/de/142.318.md

Grundsatz: Anzahl anwesender Personen an Befragungen ist zu
beschraenken gemaess BAG-Vorgaben. Asylsuchende und Befrager
im gleichen Raum, ausnahmsweise getrennt mit technischen Hilfsmitteln.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class befragung_bag_vorgaben_eingehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die BAG-Vorgaben zur Personenanzahl bei Befragungen eingehalten werden"
    reference = "SR 142.318 Art. 4 Abs. 1"


class gesundheitliche_gruende_coronavirus(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob aus gesundheitlichen Gruenden im Zusammenhang mit dem Coronavirus eine getrennte Befragung notwendig ist"
    reference = "SR 142.318 Art. 4 Abs. 2"


class befragung_getrennte_raeume_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Befragung ausnahmsweise in separaten Raeumen mittels technischer Hilfsmittel durchgefuehrt werden darf"
    reference = "SR 142.318 Art. 4 Abs. 2"

    def formula_2020_04(person, period, parameters):
        return person('gesundheitliche_gruende_coronavirus', period)


class weitere_personen_anderer_raum_zugeschaltet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob weitere beteiligte Personen sich in einem anderen Raum aufhalten und zugeschaltet werden koennen"
    reference = "SR 142.318 Art. 4 Abs. 3"

    def formula_2020_04(person, period, parameters):
        return True
