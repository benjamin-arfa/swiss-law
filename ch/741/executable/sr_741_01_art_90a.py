"""SR 741.01 Art. 90a - Einziehung und Verwertung von Motorfahrzeugen

Generated from: ch/de/741/741.01.md

Vehicle confiscation:
- Court may order confiscation if:
  a) gross traffic violation committed recklessly, AND
  b) confiscation can deter further gross violations
- Court may order sale and determine use of proceeds
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class grobe_verkehrsregelverletzung_skrupellos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine grobe Verkehrsregelverletzung in skrupelloser Weise begangen wurde"
    reference = "SR 741.01 Art. 90a Abs. 1 Bst. a"


class einziehung_praeventiv_wirksam(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Einziehung von weiteren groben Verletzungen abhalten kann"
    reference = "SR 741.01 Art. 90a Abs. 1 Bst. b"


class fahrzeug_einziehung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Einziehung des Motorfahrzeugs zulaessig ist"
    reference = "SR 741.01 Art. 90a Abs. 1"

    def formula(person, period, parameters):
        skrupellos = person('grobe_verkehrsregelverletzung_skrupellos', period)
        praeventiv = person('einziehung_praeventiv_wirksam', period)
        return skrupellos * praeventiv
