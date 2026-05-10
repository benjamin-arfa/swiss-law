"""SR 981 Art. 2

Generated from: ch/de/981.md

Determination of compensation claims: EDA may publicly call interested
persons to register claims with a forfeiture deadline; EDA determines
whether requirements are met; Federal Council may exclude trivial cases.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class eda_oeffentlicher_aufruf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das EDA interessierte Personen durch oeffentlichen Aufruf zur Anmeldung ihrer Begehren auffordert"
    reference = "SR 981 Art. 2 Abs. 1"


class verwirkungsfrist_gesetzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Verwirkungsfrist fuer die Anmeldung der Begehren gesetzt wurde"
    reference = "SR 981 Art. 2 Abs. 1"


class persoenliche_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die persoenlichen Voraussetzungen fuer die Geltendmachung eines Entschaedigungsanspruchs erfuellt sind"
    reference = "SR 981 Art. 2 Abs. 2"


class sachliche_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die sachlichen Voraussetzungen fuer die Geltendmachung eines Entschaedigungsanspruchs erfuellt sind"
    reference = "SR 981 Art. 2 Abs. 2"


class eda_verfuegung_nicht_bindend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verfuegung des EDA nicht bindend fuer den Entscheid ueber die Entschaedigung ist"
    reference = "SR 981 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return True


class bagatellfall_ausgeschlossen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Bagatellfall von der Geltendmachung ausgeschlossen ist"
    reference = "SR 981 Art. 2 Abs. 3"
