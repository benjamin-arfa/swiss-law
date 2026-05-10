"""SR 142.206 Art. 12

Generated from: ch/142/de/142.206.md

Voraussetzungen fuer den Erhalt der Daten: Erforderlichkeit fuer
Feststellung von Reisen/Aufenthalten oder Identifikation bei
terroristischen oder sonstigen schweren Straftaten.
Verhaeltnismaessigkeit und hinreichende Gruende erforderlich.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ees_daten_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die beantragten EES-Daten erforderlich sind (Art. 12 Abs. 1 Bst. a)"
    reference = "SR 142.206 Art. 12 Abs. 1 Bst. a"


class ees_daten_verhaeltnismaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Datenbekanntgabe verhaeltnismaessig ist"
    reference = "SR 142.206 Art. 12 Abs. 1 Bst. b"


class ees_hinreichende_gruende(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Beweise oder hinreichende Gruende vorliegen, dass die Datenbekanntgabe zweckdienlich ist"
    reference = "SR 142.206 Art. 12 Abs. 1 Bst. c"


class ees_afis_abgefragt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob AFIS vorgaengig abgefragt wurde (bei Identifikation unbekannter Personen)"
    reference = "SR 142.206 Art. 12 Abs. 3"


class ees_unmittelbare_lebensgefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine unmittelbar drohende Lebensgefahr im Zusammenhang mit einer terroristischen oder schweren Straftat besteht"
    reference = "SR 142.206 Art. 12 Abs. 4 Bst. b"


class ees_datenerhalt_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob alle Voraussetzungen fuer den Erhalt von EES-Daten erfuellt sind"
    reference = "SR 142.206 Art. 12"

    def formula_2022_05(person, period, parameters):
        erforderlich = person('ees_daten_erforderlich', period)
        verhaeltnismaessig = person('ees_daten_verhaeltnismaessig', period)
        gruende = person('ees_hinreichende_gruende', period)
        return erforderlich * verhaeltnismaessig * gruende
