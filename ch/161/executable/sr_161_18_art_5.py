"""SR 161.18 Art. 5

Generated from: ch/161/de/161.18.md

Offenlegung der budgetierten Einnahmen und Zuwendungen:
Schwelle von CHF 50'000 fuer Kampagnen, CHF 15'000 fuer Zuwendungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufwendungen_kampagne(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Voraussichtliche Aufwendungen fuer eine Kampagne in CHF"
    reference = "SR 161.18 Art. 5 Abs. 1"


class kampagne_offenlegungspflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kampagne offenlegungspflichtig ist (Aufwendungen ueber CHF 50'000)"
    reference = "SR 161.18 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        aufwendungen = person('aufwendungen_kampagne', period)
        return aufwendungen > 50000


class zuwendung_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag einer einzelnen Zuwendung in CHF"
    reference = "SR 161.18 Art. 5 Abs. 1"


class zuwendung_meldepflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Zuwendung meldepflichtig ist (ueber CHF 15'000)"
    reference = "SR 161.18 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        betrag = person('zuwendung_betrag', period)
        return betrag > 15000
