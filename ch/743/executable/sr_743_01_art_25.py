"""SR 743.01 Art. 25

Generated from: ch/743/de/743.01.md

Seilbahngesetz (SebG) - Vergehen.
Vorsaetzlicher Bau/Betrieb ohne Genehmigung: Freiheitsstrafe bis 3 Jahre
oder Geldstrafe. Fahrlaessig: Geldstrafe bis 180 Tagessaetze.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class seilbahn_bau_ohne_plangenehmigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Seilbahn ohne Plangenehmigung oder kantonale Bewilligung gebaut wurde"
    reference = "SR 743.01 Art. 25 Abs. 1 Bst. a"


class seilbahn_betrieb_ohne_betriebsbewilligung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Seilbahn ohne Betriebsbewilligung betrieben wurde"
    reference = "SR 743.01 Art. 25 Abs. 1 Bst. b"


class seilbahn_vergehen_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein vorsaetzliches Vergehen nach Art. 25 vorliegt"
    reference = "SR 743.01 Art. 25 Abs. 1"


class seilbahn_vergehen_max_freiheitsstrafe_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechststrafe Freiheitsstrafe in Jahren bei vorsaetzlichem Vergehen"
    reference = "SR 743.01 Art. 25 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        vorsaetzlich = person('seilbahn_vergehen_vorsaetzlich', period)
        return np.where(vorsaetzlich, 3, 0)


class seilbahn_vergehen_fahrlaessig_max_tagessaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechststrafe in Tagessaetzen bei fahrlaessigem Vergehen"
    reference = "SR 743.01 Art. 25 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        vorsaetzlich = person('seilbahn_vergehen_vorsaetzlich', period)
        bau = person('seilbahn_bau_ohne_plangenehmigung', period)
        betrieb = person('seilbahn_betrieb_ohne_betriebsbewilligung', period)
        fahrlaessig = np.logical_not(vorsaetzlich) * ((bau + betrieb) > 0)
        return np.where(fahrlaessig, 180, 0)
