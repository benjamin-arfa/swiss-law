"""SR 161.116 Art. 4

Generated from: ch/161/de/161.116.md

Anforderungen an die Zulassung von mehr als 30% des kantonalen Elektorats
fuer elektronische Stimmabgabe: individuelle Verifizierbarkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anteil_kantonales_elektorat_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil des kantonalen Elektorats in Prozent, der zur elektronischen Stimmabgabe zugelassen werden soll"
    reference = "SR 161.116 Art. 4"


class individuelle_verifizierbarkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das System individuelle Verifizierbarkeit bietet"
    reference = "SR 161.116 Art. 4 Abs. 1"


class vollstaendige_verifizierbarkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das System vollstaendige Verifizierbarkeit bietet"
    reference = "SR 161.116 Art. 5"


class elektronische_stimmabgabe_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die elektronische Stimmabgabe zulaessig ist"
    reference = "SR 161.116 Art. 4-5"

    def formula(person, period, parameters):
        anteil = person('anteil_kantonales_elektorat_prozent', period)
        indiv = person('individuelle_verifizierbarkeit', period)
        vollst = person('vollstaendige_verifizierbarkeit', period)
        # Bis 30%: keine besondere Verifizierbarkeit noetig
        # Ueber 30%: individuelle Verifizierbarkeit
        # Ueber 50%: vollstaendige Verifizierbarkeit
        bis_30 = anteil <= 30
        ueber_30 = (anteil > 30) * (anteil <= 50) * indiv
        ueber_50 = (anteil > 50) * vollst
        return bis_30 + ueber_30 + ueber_50 > 0
