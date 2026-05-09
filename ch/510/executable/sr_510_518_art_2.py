"""SR 510.518 Art. 2 - Meldepflicht der Gemeinden und Kantone

Generated from: ch/510/de/510.518.md

Die Gemeinden und Kantone haben dem VBS zu melden:
a. jede bauliche oder forstwirtschaftliche Massnahme, die militaerische
   Anlagen beeintraechtigen koennte, vor deren Ausfuehrung
b. alle Um- und Neubauten von Flugplaetzen und alle militaerisch wichtigen
   Kunstbauten
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_bauliche_massnahme_nahe_mil_anlage(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine bauliche oder forstwirtschaftliche Massnahme militaerische Anlagen beeintraechtigen koennte"
    reference = "SR 510.518 Art. 2 lit. a"


class ist_flugplatz_umbau_neubau(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen Um- oder Neubau von Flugplaetzen oder militaerisch wichtigen Kunstbauten handelt"
    reference = "SR 510.518 Art. 2 lit. b"


class meldepflicht_an_vbs(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Meldepflicht gegenueber dem VBS besteht"
    reference = "SR 510.518 Art. 2"

    def formula(person, period, parameters):
        return (
            person('ist_bauliche_massnahme_nahe_mil_anlage', period)
            + person('ist_flugplatz_umbau_neubau', period)
        ) > 0
