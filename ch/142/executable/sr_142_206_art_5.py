"""SR 142.206 Art. 5

Generated from: ch/142/de/142.206.md

Abfrage bei Kontrollen an den Schengen-Aussengrenzen oder im
Hoheitsgebiet: Abfrage anhand personenbezogener Daten oder
Reisedokumentdaten. Biometrischer Vergleich bei Treffer.
Zugang zu Kategorien I-VI bei Uebereinstimmung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ees_kontrolle_aussengrenze_oder_inland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Kontrolle an Schengen-Aussengrenzen oder im Hoheitsgebiet der Schweiz stattfindet"
    reference = "SR 142.206 Art. 5 Abs. 1"


class ees_biometrischer_vergleich_uebereinstimmung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der biometrische Vergleich eine Uebereinstimmung ergibt"
    reference = "SR 142.206 Art. 5 Abs. 2-3"


class ees_zugang_kategorien_kontrolle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob bei Grenz-/Inlandskontrolle Zugang zu Kategorien I-VI besteht"
    reference = "SR 142.206 Art. 5 Abs. 3"

    def formula_2022_05(person, period, parameters):
        kontrolle = person('ees_kontrolle_aussengrenze_oder_inland', period)
        treffer = person('ees_treffer_gefunden', period)
        biometrisch = person('ees_biometrischer_vergleich_uebereinstimmung', period)
        return kontrolle * treffer * biometrisch


class ees_identifikation_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Identifikationsabfrage erforderlich ist (kein Treffer oder Identitaetszweifel)"
    reference = "SR 142.206 Art. 5 Abs. 4"

    def formula_2022_05(person, period, parameters):
        kontrolle = person('ees_kontrolle_aussengrenze_oder_inland', period)
        treffer = person('ees_treffer_gefunden', period)
        return kontrolle * not_(treffer)
