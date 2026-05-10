"""SR 830.11 Art. 5

Generated from: ch/830/de/830.11.md

Art. 5: Grosse Haerte - Great hardship exists when EL-recognized expenses
plus additional expenses exceed EL-recognized income.

Additional expenses (Abs. 4):
a. single persons: CHF 8,000
b. married couples: CHF 12,000
c. pension-eligible orphans and children with AHV/IV child pension: CHF 4,000 per child

Property consumption for persons in homes/hospitals: 1/15 of property
(1/10 for elderly pensioners).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class atsv_el_anerkannte_ausgaben(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "EL-anerkannte Ausgaben (inkl. Miete, KVG-Praemie)"
    reference = "SR 830.11 Art. 5 Abs. 1-2"


class atsv_el_anrechenbare_einnahmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "EL-anrechenbare Einnahmen"
    reference = "SR 830.11 Art. 5 Abs. 1"


class atsv_ist_alleinstehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist alleinstehend"
    reference = "SR 830.11 Art. 5 Abs. 4 Bst. a"


class atsv_ist_verheiratet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist verheiratet (Ehepaar)"
    reference = "SR 830.11 Art. 5 Abs. 4 Bst. b"


class atsv_anzahl_rentenberechtigte_kinder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl rentenberechtigter Waisen oder Kinder mit AHV/IV-Kinderrente"
    reference = "SR 830.11 Art. 5 Abs. 4 Bst. c"


class atsv_zusaetzliche_ausgaben(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zusaetzliche Ausgaben fuer Haerteberechnung nach Art. 5 Abs. 4 ATSV"
    reference = "SR 830.11 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        alleinstehend = person('atsv_ist_alleinstehend', period)
        verheiratet = person('atsv_ist_verheiratet', period)
        kinder = person('atsv_anzahl_rentenberechtigte_kinder', period)

        zuschlag_person = where(verheiratet, 12000, where(alleinstehend, 8000, 0))
        zuschlag_kinder = kinder * 4000

        return zuschlag_person + zuschlag_kinder


class atsv_grosse_haerte_berechnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Grosse Haerte liegt vor (Ausgaben uebersteigen Einnahmen)"
    reference = "SR 830.11 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        ausgaben = person('atsv_el_anerkannte_ausgaben', period)
        zusatz = person('atsv_zusaetzliche_ausgaben', period)
        einnahmen = person('atsv_el_anrechenbare_einnahmen', period)

        return (ausgaben + zusatz) > einnahmen
