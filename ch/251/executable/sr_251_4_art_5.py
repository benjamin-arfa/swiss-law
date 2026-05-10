"""SR 251.4 Art. 5

Generated from: ch/251/de/251.4.md

Umsatz eines beteiligten Unternehmens: Setzt sich zusammen aus
eigener Geschaeftstaetigkeit und den Umsaetzen von Tochter-, Mutter-,
Schwester- und Gemeinschaftsunternehmen. Konzerninterne Umsaetze
werden nicht beruecksichtigt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class umsatz_eigene_geschaeftstaetigkeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Umsatz aus eigener Geschaeftstaetigkeit"
    reference = "SR 251.4 Art. 5 Abs. 1"


class umsatz_tochterunternehmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Umsaetze der Tochterunternehmen"
    reference = "SR 251.4 Art. 5 Abs. 1 Bst. a"


class umsatz_mutterunternehmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Umsaetze der Mutterunternehmen"
    reference = "SR 251.4 Art. 5 Abs. 1 Bst. b"


class umsatz_schwesterunternehmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Umsaetze der Schwesterunternehmen"
    reference = "SR 251.4 Art. 5 Abs. 1 Bst. c"


class umsatz_gemeinschaftsunternehmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteilige Umsaetze der Gemeinschaftsunternehmen (zu gleichen Teilen)"
    reference = "SR 251.4 Art. 5 Abs. 1 Bst. d / Abs. 3"


class konzerninterne_umsaetze(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Umsaetze aus Geschaeften zwischen den verbundenen Unternehmen (abzuziehen)"
    reference = "SR 251.4 Art. 5 Abs. 2"


class gesamtumsatz_beteiligtes_unternehmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtumsatz des beteiligten Unternehmens fuer die Zusammenschlusskontrolle"
    reference = "SR 251.4 Art. 5"

    def formula(person, period, parameters):
        return (
            person('umsatz_eigene_geschaeftstaetigkeit', period)
            + person('umsatz_tochterunternehmen', period)
            + person('umsatz_mutterunternehmen', period)
            + person('umsatz_schwesterunternehmen', period)
            + person('umsatz_gemeinschaftsunternehmen', period)
            - person('konzerninterne_umsaetze', period)
        )
