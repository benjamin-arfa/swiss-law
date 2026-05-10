"""SR 142.318 Art. 8

Generated from: ch/142/de/142.318.md

Erstinstanzliche Verfahrensfristen: Die Fristen nach Art. 37 AsylG
koennen angemessen ueberschritten werden, wenn die Umstaende im
Zusammenhang mit dem Coronavirus dies erfordern.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class coronavirus_umstaende_verfahrensfrist(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Umstaende im Zusammenhang mit dem Coronavirus eine Fristverlaengerung erfordern"
    reference = "SR 142.318 Art. 8"


class verfahrensfristen_ueberschreitung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die erstinstanzlichen Verfahrensfristen nach Art. 37 AsylG angemessen ueberschritten werden duerfen"
    reference = "SR 142.318 Art. 8"

    def formula_2020_04(person, period, parameters):
        return person('coronavirus_umstaende_verfahrensfrist', period)
