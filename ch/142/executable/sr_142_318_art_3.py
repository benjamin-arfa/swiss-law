"""SR 142.318 Art. 3

Generated from: ch/142/de/142.318.md

Genehmigungsfreie Nutzung von zivilen Bauten und Anlagen: Das SEM
kann genehmigungsfrei bauliche Aenderungen, Umnutzungen und
Fahrnisbauten umsetzen. Zweifelsfaelle muessen dem EJPD mindestens
2 Tage vor Arbeitsbeginn vorgelegt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_zivile_baute_bund(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Baute eine zivile Baute im Eigentum des Bundes oder vom Bund gemietet ist"
    reference = "SR 142.318 Art. 3 Abs. 1 Bst. a"


class ist_fahrnisbau_bei_zentrum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um eine Fahrnisbaute am Standort eines Bundeszentrums handelt"
    reference = "SR 142.318 Art. 3 Abs. 1 Bst. b"


class unterbringung_asylsuchende_notwendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Nutzung zur Unterbringung Asylsuchender oder Durchfuehrung von Asylverfahren notwendig ist"
    reference = "SR 142.318 Art. 3 Abs. 1"


class keine_schwerwiegende_einschraenkung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob schutzwuerdige Interessen der Raumordnung, Umwelt oder Dritter nicht schwerwiegend eingeschraenkt werden"
    reference = "SR 142.318 Art. 3 Abs. 1"


class genehmigungsfreie_nutzung_zivile_bauten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die genehmigungsfreie Nutzung von zivilen Bauten zulaessig ist"
    reference = "SR 142.318 Art. 3 Abs. 1"

    def formula_2020_04(person, period, parameters):
        notwendig = person('unterbringung_asylsuchende_notwendig', period)
        keine_einschraenkung = person('keine_schwerwiegende_einschraenkung', period)
        zivil = person('ist_zivile_baute_bund', period)
        fahrnisbau = person('ist_fahrnisbau_bei_zentrum', period)
        return notwendig * keine_einschraenkung * ((zivil + fahrnisbau) > 0)


class vorlage_ejpd_frist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist in Tagen vor Arbeitsbeginn fuer Vorlage von Zweifelsfaellen beim EJPD"
    reference = "SR 142.318 Art. 3 Abs. 2"

    def formula_2020_04(person, period, parameters):
        return parameters(period).vorlage_ejpd_frist_tage
