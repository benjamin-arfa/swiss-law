"""SR 819.14 Art. 1

Generated from: ch/819/de/819.14.md

Art. 1 Gegenstand, Geltungsbereich, Begriffe und anwendbares Recht:
1. Regulates placing on the market and market surveillance of machinery
   per EU Machinery Directive 2006/42/EC.
2. Scope follows Art. 1 of the EU Machinery Directive; Art. 3 applies mutatis mutandis.
3. Where this ordinance references EU law that in turn references other EU law,
   Swiss law per Annex 1 Section 2 applies instead.
4. Where no special provisions exist, the Product Safety Ordinance (PrSV, SR 930.111) applies.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class maschv_maschine_im_geltungsbereich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Maschine in den Geltungsbereich der Maschinenverordnung faellt"
    reference = "SR 819.14 Art. 1 Abs. 2"


class maschv_prsv_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Produktesicherheitsverordnung (PrSV) subsidiär anwendbar ist"
    reference = "SR 819.14 Art. 1 Abs. 4"

    def formula(person, period, parameters):
        return person('maschv_maschine_im_geltungsbereich', period)
