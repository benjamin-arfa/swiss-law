"""SR 251.5 Art. 8

Generated from: ch/251/de/251.5.md

Vollstaendiger Erlass der Sanktion: Voraussetzungen fuer die
Selbstanzeige und den vollstaendigen Sanktionserlass.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_erstes_unternehmen_mit_anzeige(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen als Erstes die Beteiligung anzeigt"
    reference = "SR 251.5 Art. 8 Abs. 1"


class liefert_informationen_fuer_verfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen Informationen liefert, die ein kartellrechtliches Verfahren ermoeglichen"
    reference = "SR 251.5 Art. 8 Abs. 1 Bst. a"


class legt_beweismittel_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen Beweismittel vorlegt, die eine Feststellung des Verstosses ermoeglichen"
    reference = "SR 251.5 Art. 8 Abs. 1 Bst. b"


class kein_zwang_auf_andere(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen kein anderes Unternehmen zur Teilnahme gezwungen hat und keine fuehrende Rolle hatte"
    reference = "SR 251.5 Art. 8 Abs. 2 Bst. a"


class alle_informationen_vorgelegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen unaufgefordert saemtliche Informationen und Beweismittel vorgelegt hat"
    reference = "SR 251.5 Art. 8 Abs. 2 Bst. b"


class ununterbrochene_zusammenarbeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen waehrend des gesamten Verfahrens ununterbrochen zusammenarbeitet"
    reference = "SR 251.5 Art. 8 Abs. 2 Bst. c"


class beteiligung_eingestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Beteiligung am Verstoss spaetestens zum Zeitpunkt der Selbstanzeige eingestellt wurde"
    reference = "SR 251.5 Art. 8 Abs. 2 Bst. d"


class behoerde_hat_genuegend_informationen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Wettbewerbsbehoerde bereits ueber ausreichende Informationen verfuegt"
    reference = "SR 251.5 Art. 8 Abs. 3"


class anderes_unternehmen_hat_erlass(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob bereits ein anderes Unternehmen die Voraussetzungen fuer einen Erlass erfuellt"
    reference = "SR 251.5 Art. 8 Abs. 4 Bst. a"


class vollstaendiger_sanktionserlass(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein vollstaendiger Erlass der Sanktion gewaehrt wird"
    reference = "SR 251.5 Art. 8"

    def formula(person, period, parameters):
        # Grundvoraussetzungen (Abs. 2)
        grundvoraussetzung = (
            person('kein_zwang_auf_andere', period)
            * person('alle_informationen_vorgelegt', period)
            * person('ununterbrochene_zusammenarbeit', period)
            * person('beteiligung_eingestellt', period)
        )

        # Variante a: Informationen fuer Verfahrenseroeffnung
        variante_a = (
            person('ist_erstes_unternehmen_mit_anzeige', period)
            * person('liefert_informationen_fuer_verfahren', period)
            * not_(person('behoerde_hat_genuegend_informationen', period))
        )

        # Variante b: Beweismittel fuer Feststellung
        variante_b = (
            person('ist_erstes_unternehmen_mit_anzeige', period)
            * person('legt_beweismittel_vor', period)
            * not_(person('anderes_unternehmen_hat_erlass', period))
            * not_(person('behoerde_hat_genuegend_informationen', period))
        )

        return grundvoraussetzung * (variante_a + variante_b)
