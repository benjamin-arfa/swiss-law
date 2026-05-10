"""SR 981 Art. 5

Generated from: ch/de/981.md

Tasks of the Commission: public call for claims registration, exemption
from registration for previously submitted claims, assessment of
eligibility, damage valuation, and distribution of compensation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kommission_oeffentlicher_aufruf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission interessierte Personen durch oeffentlichen Aufruf zur Anmeldung auffordert"
    reference = "SR 981 Art. 5 Abs. 1"


class kommission_verwirkungsfrist(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission eine Verwirkungsfrist fuer die Anmeldung setzt"
    reference = "SR 981 Art. 5 Abs. 1"


class anmeldepflicht_entbunden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Personen deren Begehren bereits angemeldet und in Verhandlungen aufgenommen wurden von der Anmeldepflicht entbunden sind"
    reference = "SR 981 Art. 5 Abs. 2"


class gesuchsteller_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Gesuchsteller die persoenlichen und sachlichen Voraussetzungen fuer die Entschaedigung erfuellt"
    reference = "SR 981 Art. 5 Abs. 3"


class schaden_bewertet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kommission den erlittenen Schaden bewertet hat"
    reference = "SR 981 Art. 5 Abs. 3"


class entschaedigung_verteilt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Entschaedigung auf die Anspruchsberechtigten verteilt wurde"
    reference = "SR 981 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        return (
            person('gesuchsteller_voraussetzungen_erfuellt', period)
            * person('schaden_bewertet', period)
        )


class kommission_weitere_aufgaben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat der Kommission weitere Aufgaben im Bereich Entschaedigungsansprueche uebertragen hat"
    reference = "SR 981 Art. 5 Abs. 4"
