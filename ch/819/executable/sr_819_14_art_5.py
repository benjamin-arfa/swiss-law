"""SR 819.14 Art. 5

Generated from: ch/819/de/819.14.md

Art. 5 Marktueberwachung:
1. Market surveillance follows Art. 19-29 of PrSV (SR 930.111).
2. When the European Commission takes measures under Art. 8 or 9 of
   the EU Machinery Directive, the competent Swiss control bodies implement
   these measures. Bans, restrictions, or recalls are published in the
   Federal Gazette (Bundesblatt).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class maschv_eu_massnahme_ergriffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die EU-Kommission eine Massnahme nach Art. 8/9 EU-MRL ergriffen hat"
    reference = "SR 819.14 Art. 5 Abs. 2"


class maschv_umsetzung_ch_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Umsetzung der EU-Massnahme fuer die Schweiz erforderlich ist"
    reference = "SR 819.14 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        return person('maschv_eu_massnahme_ergriffen', period)
