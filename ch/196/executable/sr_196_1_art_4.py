"""SR 196.1 Art. 4

Generated from: ch/196/de/196.1.md

Sperrung im Hinblick auf eine Einziehung bei Scheitern der Rechtshilfe:
Voraussetzungen fuer die Sperrung bei Versagen staatlicher Strukturen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermoegenswerte_vorlaeufig_sichergestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Vermoegenswerte im Rahmen eines Rechtshilfeverfahrens vorlaeufig sichergestellt wurden"
    reference = "SR 196.1 Art. 4 Abs. 2 lit. a"


class versagen_staatlicher_strukturen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Herkunftsstaat die Anforderungen wegen voelligen oder weitgehenden Zusammenbruchs seines Justizsystems nicht erfuellen kann"
    reference = "SR 196.1 Art. 4 Abs. 2 lit. b"


class rechtshilfe_ausgeschlossen_verfahrensgrundsaetze(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zusammenarbeit ausgeschlossen ist weil das Verfahren im Herkunftsstaat den Verfahrensgrundsaetzen nicht entspricht"
    reference = "SR 196.1 Art. 4 Abs. 3"


class sperrung_einziehung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sperrung im Hinblick auf ein Einziehungsverfahren zulaessig ist"
    reference = "SR 196.1 Art. 4 Abs. 2-3"

    def formula(person, period, parameters):
        pep_oder_nahestehend = person('ist_auslaendische_politisch_exponierte_person', period) + person('ist_nahestehende_person', period) > 0
        verfuegungsmacht_oder_berechtigt = person('hat_verfuegungsmacht_ueber_vermoegenswerte', period) + person('ist_wirtschaftlich_berechtigt', period) > 0
        interessen = person('wahrung_schweizer_interessen_erfordert_sperrung', period)
        sichergestellt = person('vermoegenswerte_vorlaeufig_sichergestellt', period)

        # Abs. 2: Versagen staatlicher Strukturen
        abs2 = sichergestellt * person('versagen_staatlicher_strukturen', period) * interessen

        # Abs. 3: Verfahrensgrundsaetze nicht eingehalten
        abs3 = person('rechtshilfe_ausgeschlossen_verfahrensgrundsaetze', period) * interessen

        return pep_oder_nahestehend * verfuegungsmacht_oder_berechtigt * (abs2 + abs3 > 0)
