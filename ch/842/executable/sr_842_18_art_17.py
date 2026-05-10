"""SR 842.18 Art. 17

Generated from: ch/842/de/842.18.md

Revisionspflicht (Audit obligation): WBG audit requirements based on size.
- General audit obligation per OR
- BWO can require limited audit (eingeschraenkte Revision) for WBG that opted out under OR 727a
- Simplified review allowed if WBG has <= 30 federally subsidized apartments
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

SCHWELLE_VEREINFACHTE_PRUEFUNG = 30  # max Wohnungen fuer prüferische Durchsicht


class anzahl_gefoerderte_wohnungen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl mit Bundeshilfe gefoerderte Wohnungen der WBG"
    reference = "SR 842.18 Art. 17 Abs. 3"


class hat_auf_revision_verzichtet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "WBG hat im Rahmen von Art. 727a OR auf Revision verzichtet"
    reference = "SR 842.18 Art. 17 Abs. 2"


class braucht_eingeschraenkte_revision(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BWO verlangt eine eingeschraenkte Revision"
    reference = "SR 842.18 Art. 17 Abs. 2"

    def formula(person, period):
        return person('hat_auf_revision_verzichtet', period)


class darf_prueferische_durchsicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Darf statt eingeschraenkter Revision eine prueferische Durchsicht durchfuehren"
    reference = "SR 842.18 Art. 17 Abs. 3"

    def formula(person, period):
        # Nur wenn: auf Revision verzichtet UND hoechstens 30 gefoerderte Wohnungen
        verzichtet = person('hat_auf_revision_verzichtet', period)
        wohnungen = person('anzahl_gefoerderte_wohnungen', period)
        return verzichtet * (wohnungen <= SCHWELLE_VEREINFACHTE_PRUEFUNG)
