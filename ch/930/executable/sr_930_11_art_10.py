"""SR 930.11 Art. 10

Generated from: ch/930/de/930.11.md

Art. 10: Kontrolle und Verwaltungsmassnahmen - Controls and administrative measures:
1. Authorities may inspect and sample products on the market
2. If product doesn't meet requirements: order appropriate measures
3. Possible measures:
   a. Ban further placing on market
   b. Order warning/recall/return and execute if necessary
   c. Ban export of banned products
   d. Seize and destroy products posing immediate serious danger
4. Authorities warn public about dangerous products
5. Measures may be issued as general orders
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class prsg_kontrolle_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produktkontrolle durch Vollzugsorgan wurde durchgeführt"
    reference = "SR 930.11 Art. 10 Abs. 1"


class prsg_produkt_nicht_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produkt entspricht nicht den Anforderungen (festgestellt bei Kontrolle)"
    reference = "SR 930.11 Art. 10 Abs. 2"


class prsg_unmittelbare_gefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Von Produkt geht eine unmittelbare und ernste Gefahr aus"
    reference = "SR 930.11 Art. 10 Abs. 3 Bst. d"


class prsg_massnahme_inverkehrbringen_verbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verbot des weiteren Inverkehrbringens angeordnet"
    reference = "SR 930.11 Art. 10 Abs. 3 Bst. a"


class prsg_massnahme_rueckruf(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Warnung, Rücknahme oder Rückruf des Produkts angeordnet"
    reference = "SR 930.11 Art. 10 Abs. 3 Bst. b"


class prsg_massnahme_ausfuhrverbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausfuhrverbot für verbotenes Produkt angeordnet"
    reference = "SR 930.11 Art. 10 Abs. 3 Bst. c"


class prsg_massnahme_einziehung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Einziehung und Vernichtung des Produkts (bei unmittelbarer Gefahr)"
    reference = "SR 930.11 Art. 10 Abs. 3 Bst. d"

    def formula(person, period, parameters):
        nicht_konform = person('prsg_produkt_nicht_konform', period)
        unmittelbar = person('prsg_unmittelbare_gefahr', period)
        return nicht_konform * unmittelbar
