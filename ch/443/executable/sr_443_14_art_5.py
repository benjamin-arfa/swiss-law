"""SR 443.14 Art. 5

Generated from: ch/443/de/443.14.md

Ausgenommene Unternehmen: Ausgenommen wenn Umsatz < 2.5 Mio CHF,
max 12 lange Filme/Jahr, oder nur zeitversetztes TV.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class umsatz_fernseh_abrufdienste_ch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Umsatz mit Fernseh-/Abrufdiensten in CH (CHF)"
    reference = "SR 443.14 Art. 5 Abs. 1 Bst. a"


class anzahl_lange_filme_pro_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl langer anrechenbarer Filme pro Jahr"
    reference = "SR 443.14 Art. 5 Abs. 1 Bst. b"


class nur_zeitversetztes_tv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob nur zeitversetztes Fernsehen angeboten wird"
    reference = "SR 443.14 Art. 5 Abs. 1 Bst. c"


class von_filmpflichten_ausgenommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen von den Filmpflichten ausgenommen ist"
    reference = "SR 443.14 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        umsatz = person('umsatz_fernseh_abrufdienste_ch', period)
        filme = person('anzahl_lange_filme_pro_jahr', period)
        zeitversetzt = person('nur_zeitversetztes_tv', period)
        return (umsatz < 2500000) + (filme <= 12) + zeitversetzt
