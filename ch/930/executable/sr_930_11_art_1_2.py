"""SR 930.11 Art. 1 & 2

Generated from: ch/930/de/930.11.md

Art. 1: Zweck und Geltungsbereich - Purpose and scope:
- Ensure safety of products and facilitate free movement of goods
- Applies to commercial/professional placing on market of products
- Does not apply to used products sold as antiques or requiring refurbishment

Art. 2: Begriffe - Definitions:
- Product: ready-to-use movable item (including parts for assembly)
- Placing on market: any transfer, including own use, service use, making available, offering
- Manufacturer: includes own-brand labelers, representatives, refurbishers
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class prsg_ist_produkt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gegenstand ist ein Produkt im Sinne des PrSG (verwendungsbereite bewegliche Sache)"
    reference = "SR 930.11 Art. 2 Abs. 1"


class prsg_gewerbliches_inverkehrbringen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produkt wird gewerblich oder beruflich in Verkehr gebracht"
    reference = "SR 930.11 Art. 1 Abs. 2"


class prsg_ist_antiquitaet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebrauchtes Produkt wird als Antiquität überlassen"
    reference = "SR 930.11 Art. 1 Abs. 4 Bst. a"


class prsg_muss_instandgesetzt_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebrauchtes Produkt muss vor Verwendung instand gesetzt/wiederaufbereitet werden"
    reference = "SR 930.11 Art. 1 Abs. 4 Bst. b"


class prsg_im_geltungsbereich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Produkt fällt in den Geltungsbereich des PrSG"
    reference = "SR 930.11 Art. 1"

    def formula(person, period, parameters):
        ist_produkt = person('prsg_ist_produkt', period)
        gewerblich = person('prsg_gewerbliches_inverkehrbringen', period)
        antiquitaet = person('prsg_ist_antiquitaet', period)
        instandsetzung = person('prsg_muss_instandgesetzt_werden', period)
        # In scope if: is a product, commercially placed, not an antique or needing refurbishment
        return ist_produkt * gewerblich * (1 - antiquitaet) * (1 - instandsetzung)


class prsg_ist_hersteller(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person gilt als Hersteller im Sinne des PrSG"
    reference = "SR 930.11 Art. 2 Abs. 4"


class prsg_ist_importeur(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Importeur des Produkts"
    reference = "SR 930.11 Art. 3 Abs. 6 Bst. b"


class prsg_ist_haendler(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Händler des Produkts"
    reference = "SR 930.11 Art. 3 Abs. 6 Bst. b"
