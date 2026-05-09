"""SR 810.211 Art. 21

Generated from: ch/810/de/810.211.md

Art. 21: Pflichten bei der Lagerung.

Abs. 1: Die Inhaberin oder der Inhaber einer Bewilligung fuer die
Lagerung von Geweben oder Zellen muss geeignete biologische Proben
der Spenderinnen und Spender in genuegender Menge aufbewahren, damit
sie bis 2 Jahre nach der Transplantation getestet werden koennen.

Abs. 2: Jaehrliche Meldepflicht an das BAG bis Ende April fuer das
vergangene Kalenderjahr:
  a. Art und Anzahl der gelagerten Gewebe
  b. Art der gelagerten Zellen und Anzahl in Applikationseinheiten
  c. Anzahl der Ein- und Ausgaenge
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_bewilligung_lagerung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Inhaber/in einer Bewilligung fuer die Lagerung von Geweben oder Zellen"
    reference = "SR 810.211 Art. 21 Abs. 1"


class monate_seit_transplantation(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit der Transplantation der Gewebe oder Zellen"
    reference = "SR 810.211 Art. 21 Abs. 1"


class probenaufbewahrung_pflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Biologische Proben muessen aufbewahrt werden (bis 2 Jahre nach Transplantation)"
    reference = "SR 810.211 Art. 21 Abs. 1"

    def formula(person, period, parameters):
        bewilligung = person('hat_bewilligung_lagerung', period.this_year)
        monate = person('monate_seit_transplantation', period)
        max_monate = parameters(period).sr_810_211.art_21.probenaufbewahrung_jahre * 12
        return bewilligung * (monate <= max_monate)


class meldung_lagerung_bag_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Meldung an das BAG ueber Lagerung ist faellig (bis Ende April)"
    reference = "SR 810.211 Art. 21 Abs. 2"

    def formula(person, period, parameters):
        return person('hat_bewilligung_lagerung', period)
