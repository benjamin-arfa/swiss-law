"""SR 784.104 Art. 11

Generated from: ch/784/de/784.104.md

Widerruf von Adressierungselementen:
- BAKOM kann Zuteilung widerrufen bei: Änderung der Nummerierungspläne,
  Rechtsmissachtung, Nichtverwendung, Nichtbezahlung, Konkurs, etc.
- Vorläufige Massnahme: Ausserbetriebsetzung
- Element gilt als widerrufen bei Tod oder Löschung aus dem Handelsregister
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aenderung_nummerierungsplan(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Änderung der Nummerierungspläne den Widerruf erfordert"
    reference = "SR 784.104 Art. 11 Abs. 1 Bst. a"


class missachtung_anwendbares_recht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Inhaberin das anwendbare Recht missachtet"
    reference = "SR 784.104 Art. 11 Abs. 1 Bst. b"


class verdacht_rechtsverletzung_inhaberin(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Verdacht besteht, dass Inhaberin Bundesrecht verletzt"
    reference = "SR 784.104 Art. 11 Abs. 1 Bst. bter"


class element_nicht_mehr_verwendet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Element nicht mehr oder nicht in der Schweiz verwendet wird"
    reference = "SR 784.104 Art. 11 Abs. 1 Bst. c"


class gebuehren_nicht_bezahlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die fälligen Verwaltungsgebühren nicht bezahlt wurden"
    reference = "SR 784.104 Art. 11 Abs. 1 Bst. d"


class inhaberin_verstorben_oder_geloescht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Inhaberin verstorben ist oder aus dem HR gelöscht wurde"
    reference = "SR 784.104 Art. 11 Abs. 3"


class widerruf_adressierungselement_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zuteilung des Adressierungselements widerrufen werden kann"
    reference = "SR 784.104 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('aenderung_nummerierungsplan', period) +
            person('missachtung_anwendbares_recht', period) +
            person('verdacht_rechtsverletzung_inhaberin', period) +
            person('element_nicht_mehr_verwendet', period) +
            person('gebuehren_nicht_bezahlt', period) +
            person('in_konkurs_oder_liquidation_aefv', period) +
            person('inhaberin_verstorben_oder_geloescht', period)
        )
