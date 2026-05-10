"""SR 150.2 Art. 7

Generated from: ch/150/de/150.2.md

Benachrichtigung: Kann der Aufenthaltsort nicht ermittelt werden,
wird die gesuchstellende Person benachrichtigt. Bei Fund im Freiheitsentzug:
Benachrichtigung nur mit ausdruecklicher Einwilligung der gesuchten Person.
Ohne Einwilligung: Mitteilung, dass Person nicht verschwunden ist (keine
weiteren Angaben).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuchte_person_gefunden_in_freiheitsentzug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die gesuchte Person in einem Freiheitsentzug gefunden wurde"
    reference = "SR 150.2 Art. 7 Abs. 2"


class gesuchte_person_willigt_ein(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die gesuchte Person ausdruecklich in die Benachrichtigung einwilligt"
    reference = "SR 150.2 Art. 7 Abs. 2"


class untersuchungszweck_verbietet_benachrichtigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Untersuchungszweck die Benachrichtigung verbietet (Art. 214 Abs. 2 StPO)"
    reference = "SR 150.2 Art. 7 Abs. 3"


class benachrichtigung_mit_aufenthaltsort(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die gesuchstellende Person ueber den Aufenthaltsort benachrichtigt wird"
    reference = "SR 150.2 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        return (
            person('gesuchte_person_gefunden_in_freiheitsentzug', period)
            * person('gesuchte_person_willigt_ein', period)
            * not_(person('untersuchungszweck_verbietet_benachrichtigung', period))
        )
