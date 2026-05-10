"""SR 443.1 Art. 16

Generated from: ch/443/de/443.1.md

Ausschluss von der Filmfoerderung:
- Keine Finanzhilfen: Werbefilme, didaktische Filme, Auftragsproduktionen
- Gaenzlich ausgeschlossen: Menschenwuerde verletzend, erniedrigend,
  Gewalt verherrlichend, pornografisch
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_werbefilm(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Werbefilm handelt"
    reference = "SR 443.1 Art. 16 Abs. 1 Bst. a"


class ist_didaktischer_film(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Film vorwiegend didaktische Zielsetzung hat"
    reference = "SR 443.1 Art. 16 Abs. 1 Bst. b"


class ist_auftragsproduktion(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Auftragsproduktion handelt"
    reference = "SR 443.1 Art. 16 Abs. 1 Bst. c"


class verletzt_menschenwuerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Film die Menschenwuerde verletzt"
    reference = "SR 443.1 Art. 16 Abs. 2 Bst. a"


class ist_pornografisch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Film pornografischen Charakter hat"
    reference = "SR 443.1 Art. 16 Abs. 2 Bst. d"


class film_von_foerderung_ausgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Film von der Filmfoerderung ausgeschlossen ist"
    reference = "SR 443.1 Art. 16"

    def formula(person, period, parameters):
        werbe = person('ist_werbefilm', period)
        didaktisch = person('ist_didaktischer_film', period)
        auftrag = person('ist_auftragsproduktion', period)
        wuerde = person('verletzt_menschenwuerde', period)
        porno = person('ist_pornografisch', period)
        return werbe + didaktisch + auftrag + wuerde + porno
