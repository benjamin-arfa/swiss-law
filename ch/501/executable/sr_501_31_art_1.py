"""SR 501.31 Art. 1 - Koordinierter Sanitaetsdienst

Generated from: ch/501/de/501.31.md

Aufgabe des KSD ist die stufengerechte Koordination des Einsatzes und der
Nutzung der personellen, materiellen und einrichtungsmaessigen Mittel der
zivilen und militaerischen Stellen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_ksd_partner(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle ein KSD-Partner ist (mit Planung, Vorbereitung und Durchfuehrung sanitaetsdienstlicher Massnahmen beauftragt)"
    reference = "SR 501.31 Art. 1 Abs. 1"


class ksd_zustaendigkeit_vorbehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustaendigkeit des einzelnen KSD-Partners vorbehalten bleibt"
    reference = "SR 501.31 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        return person('ist_ksd_partner', period)


class ksd_bestmoegliche_versorgung_gewaehrleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die bestmoegliche sanitaetsdienstliche Versorgung aller Patienten in allen Lagen gewaehrleistet ist"
    reference = "SR 501.31 Art. 1 Abs. 3"
