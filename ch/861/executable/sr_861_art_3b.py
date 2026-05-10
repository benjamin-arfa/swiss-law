"""SR 861 Art. 3b

Generated from: ch/de/861.md

Financial aid for projects to better align family-supplementary
childcare with parents' needs: comprehensive after-school care,
care for irregular work schedules, care outside normal hours.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class projekt_abstimmung_beduerfnisse_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Kantone, Gemeinden, juristische oder natuerliche Personen fuer Abstimmungsprojekte berechtigt sind"
    reference = "SR 861 Art. 3b Abs. 1"


class projekt_umfassende_schulkinder_betreuung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Projekt umfassende und mit der Schule organisierte Betreuungsangebote fuer Schulkinder bereitstellt"
    reference = "SR 861 Art. 3b Abs. 2 Bst. a"


class projekt_unregelmaessige_arbeitszeiten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Projekt Betreuungsangebote fuer Eltern mit unregelmaessigen Arbeitszeiten bereitstellt"
    reference = "SR 861 Art. 3b Abs. 2 Bst. b"


class projekt_betreuung_ausserhalb_oeffnungszeiten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Projekt Betreuungsangebote ausserhalb der ueblichen Oeffnungszeiten (Randzeiten, Schulferien) bereitstellt"
    reference = "SR 861 Art. 3b Abs. 2 Bst. c"


class projekt_kantonale_qualitaetsanforderungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Projekt den kantonalen Qualitaetsanforderungen genuegt"
    reference = "SR 861 Art. 3b Abs. 3"
