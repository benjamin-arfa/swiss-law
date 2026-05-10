"""SR 151.14 Art. 7

Generated from: ch/151/de/151.14.md

Formal verification of pay equality analysis for employers under OR:
- Lead auditors perform formal review
- Check: analysis done within legally prescribed timeframe
- Check: scientific and legally compliant method used
- Check: all employees fully recorded
- Check: all salary components fully recorded
- Check: required data (personal and workplace characteristics) fully recorded
- Report due within one year of analysis completion
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class glg_lohngleichheitsanalyse_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Lohngleichheitsanalyse im gesetzlich vorgeschriebenen Zeitraum durchgefuehrt wurde"
    reference = "SR 151.14 Art. 7 Abs. 2 Bst. a"


class glg_methode_wissenschaftlich_rechtskonform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Analysemethode wissenschaftlich und rechtskonform ist"
    reference = "SR 151.14 Art. 7 Abs. 2 Bst. b"


class glg_arbeitnehmer_vollstaendig_erfasst(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Arbeitnehmerinnen und Arbeitnehmer vollstaendig erfasst wurden"
    reference = "SR 151.14 Art. 7 Abs. 2 Bst. c"


class glg_lohnbestandteile_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle Lohnbestandteile vollstaendig erfasst wurden"
    reference = "SR 151.14 Art. 7 Abs. 2 Bst. d"


class glg_daten_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob alle erforderlichen Daten einschliesslich persoenlicher und arbeitsplatzbezogener Merkmale vollstaendig erfasst wurden"
    reference = "SR 151.14 Art. 7 Abs. 2 Bst. e"


class glg_analyse_formell_korrekt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Lohngleichheitsanalyse formell korrekt durchgefuehrt wurde"
    reference = "SR 151.14 Art. 7 Abs. 2"

    def formula(person, period, parameters):
        durchgefuehrt = person('glg_lohngleichheitsanalyse_durchgefuehrt', period)
        methode = person('glg_methode_wissenschaftlich_rechtskonform', period)
        arbeitnehmer = person('glg_arbeitnehmer_vollstaendig_erfasst', period)
        lohn = person('glg_lohnbestandteile_vollstaendig', period)
        daten = person('glg_daten_vollstaendig', period)

        return durchgefuehrt * methode * arbeitnehmer * lohn * daten
