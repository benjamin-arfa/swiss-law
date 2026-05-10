"""SR 120.52 Art. 7

Generated from: ch/120/de/120.52.md

Ausreisebeschraenkung: Travel restriction for violent sports fans.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beteiligung_gewalttaetigkeiten_inland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person sich an Gewalttaetigkeiten im Inland beteiligt hat"
    reference = "SR 120.52 Art. 7 Abs. 4 lit. a"


class bekannt_gewalttaetigkeiten_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person aufgrund auslaendischer Polizeiinformationen wegen Gewalttaetigkeiten bekannt ist"
    reference = "SR 120.52 Art. 7 Abs. 4 lit. b"


class mitglied_gewalttaetige_gruppierung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Mitglied einer Gruppierung ist, die an Gewalttaetigkeiten beteiligt war"
    reference = "SR 120.52 Art. 7 Abs. 4 lit. c"


class absicht_reise_sportanlass_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Hinweise vorliegen, dass die Person zum Sportanlass ins Ausland reisen will"
    reference = "SR 120.52 Art. 7 Abs. 5"


class ausreisebeschraenkung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Ausreisebeschraenkung verfuegt werden kann"
    reference = "SR 120.52 Art. 7 Abs. 4-5"

    def formula(person, period, parameters):
        # Abs. 4: Annahme Beteiligung an Gewalttaetigkeiten
        beteiligung = (
            person('beteiligung_gewalttaetigkeiten_inland', period) +
            person('bekannt_gewalttaetigkeiten_ausland', period) +
            person('mitglied_gewalttaetige_gruppierung', period)
        ) > 0

        # Abs. 5: Absicht zur Reise
        reise = person('absicht_reise_sportanlass_ausland', period)

        return beteiligung * reise
