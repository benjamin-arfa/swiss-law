"""SR 152.31 Art. 1

Generated from: ch/152/de/152.31.md

Definitions: commercially used document, finalised document,
document for personal use.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_kommerziell_genutztes_dokument(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Dokument als kommerziell genutztes Dokument gilt (gegen Entgelt angeboten)"
    reference = "SR 152.31 Art. 1 Abs. 1"


class ist_dokument_fertiggestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Dokument als fertiggestellt gilt (unterzeichnet oder definitiv uebergeben)"
    reference = "SR 152.31 Art. 1 Abs. 2"


class ist_dokument_unterzeichnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Dokument von der erstellenden Behoerde unterzeichnet ist"
    reference = "SR 152.31 Art. 1 Abs. 2 Bst. a"


class ist_dokument_definitiv_uebergeben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Dokument definitiv an die Adressatin uebergeben wurde"
    reference = "SR 152.31 Art. 1 Abs. 2 Bst. b"


class ist_dokument_zum_persoenlichen_gebrauch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Dokument zum persoenlichen Gebrauch bestimmt ist (Notizen, Arbeitskopien)"
    reference = "SR 152.31 Art. 1 Abs. 3"
