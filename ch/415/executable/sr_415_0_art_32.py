"""SR 415.0 Art. 32

Generated from: ch/415/de/415.0.md

Verweigerung oder Rueckforderung von Finanzhilfen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# --- Input variables ---

class finanzhilfe_durch_unwahre_angaben_erwirkt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Finanzhilfe durch unwahre oder irrefuehrende Angaben erwirkt"
    reference = "SR 415.0 Art. 32 Abs. 1 Bst. a"


class bedingungen_nicht_erfuellt_oder_auflagen_nicht_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bedingungen nicht erfuellt oder Auflagen nicht eingehalten"
    reference = "SR 415.0 Art. 32 Abs. 1 Bst. b"


class js_mittel_zweckentfremdet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "J+S-Mittel nicht fuer J+S-Taetigkeiten verwendet"
    reference = "SR 415.0 Art. 32 Abs. 1 Bst. c"


class verpflichtungen_fairer_sport_nicht_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verpflichtungen im Bereich fairer/sicherer Sport nicht eingehalten"
    reference = "SR 415.0 Art. 32 Abs. 1 Bst. d"


# --- Computed variables ---

class finanzhilfe_verweigerung_oder_rueckforderung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bund kann Finanzhilfe verweigern oder zurueckfordern"
    reference = "SR 415.0 Art. 32 Abs. 1"

    def formula(person, period, parameters):
        unwahr = person('finanzhilfe_durch_unwahre_angaben_erwirkt', period)
        bedingungen = person('bedingungen_nicht_erfuellt_oder_auflagen_nicht_eingehalten', period)
        zweckentfremdet = person('js_mittel_zweckentfremdet', period)
        fair_sport = person('verpflichtungen_fairer_sport_nicht_eingehalten', period)
        return unwahr + bedingungen + zweckentfremdet + fair_sport
