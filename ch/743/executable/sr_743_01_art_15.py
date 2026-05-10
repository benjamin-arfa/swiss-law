"""SR 743.01 Art. 15

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Vereinfachtes Verfahren.
Vereinfachtes Verfahren bei: nicht wesentlicher Aenderung des aeusseren
Erscheinungsbilds, Seilbahnen die spaetestens nach 3 Jahren entfernt werden.
Einsprachefrist: 30 Tage.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class seilbahn_aenderung_nicht_wesentlich(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Aenderung das aeussere Erscheinungsbild nicht wesentlich veraendert"
    reference = "SR 743.01 Art. 15 Abs. 1 Bst. a"


class seilbahn_keine_schutzwuerdigen_interessen_dritter(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob keine schutzwuerdigen Interessen Dritter beruehrt werden"
    reference = "SR 743.01 Art. 15 Abs. 1 Bst. a"


class seilbahn_unerhebliche_auswirkungen_raum_umwelt(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob sich die Anlage nur unerheblich auf Raum und Umwelt auswirkt"
    reference = "SR 743.01 Art. 15 Abs. 1 Bst. a"


class seilbahn_temporaer_max_3_jahre(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob die Seilbahn spaetestens nach 3 Jahren entfernt wird"
    reference = "SR 743.01 Art. 15 Abs. 1 Bst. b"


class seilbahn_vereinfachtes_verfahren(Variable):
    value_type = bool
    entity_key = 'organisation'
    definition_period = YEAR
    label = "Ob das vereinfachte Plangenehmigungsverfahren anwendbar ist"
    reference = "SR 743.01 Art. 15 Abs. 1"

    def formula(organisation, period, parameters):
        nicht_wesentlich = organisation('seilbahn_aenderung_nicht_wesentlich', period)
        keine_interessen = organisation('seilbahn_keine_schutzwuerdigen_interessen_dritter', period)
        unerheblich = organisation('seilbahn_unerhebliche_auswirkungen_raum_umwelt', period)
        temporaer = organisation('seilbahn_temporaer_max_3_jahre', period)
        aenderungsfall = nicht_wesentlich * keine_interessen * unerheblich
        return (aenderungsfall + temporaer) > 0
