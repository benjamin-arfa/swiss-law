"""SR 832.12 Art. 16

Generated from: ch/832/de/832.12.md

Art. 16: Genehmigung der Praemientarife
- Abs. 1: Praemientarife fuer OKP und freiwillige Taggeldversicherung
  beduerfn der Genehmigung.
- Abs. 4: Verweigerung wenn Praemien:
  a. gesetzlichen Vorgaben nicht entsprechen
  b. Kosten nicht decken
  c. unangemessen hoch ueber den Kosten liegen
  d. zu uebermaessigen Reserven fuehren
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR


class kvag_praemientarif_entspricht_gesetz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Praemientarif entspricht gesetzlichen Vorgaben"
    reference = "SR 832.12 Art. 16 Abs. 4 Bst. a"


class kvag_praemientarif_deckt_kosten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Praemientarif deckt die kantonalen Kosten"
    reference = "SR 832.12 Art. 16 Abs. 4 Bst. b"


class kvag_praemientarif_angemessen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Praemientarif liegt nicht unangemessen hoch ueber den Kosten"
    reference = "SR 832.12 Art. 16 Abs. 4 Bst. c"


class kvag_praemientarif_keine_uebermaessigen_reserven(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Praemientarif fuehrt nicht zu uebermaessigen Reserven"
    reference = "SR 832.12 Art. 16 Abs. 4 Bst. d"


class kvag_praemientarif_genehmigungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Praemientarif ist genehmigungsfaehig nach Art. 16 KVAG"
    reference = "SR 832.12 Art. 16 Abs. 4"

    def formula(person, period, parameters):
        gesetz = person('kvag_praemientarif_entspricht_gesetz', period)
        kosten = person('kvag_praemientarif_deckt_kosten', period)
        angemessen = person('kvag_praemientarif_angemessen', period)
        reserven = person('kvag_praemientarif_keine_uebermaessigen_reserven', period)
        # Alle vier Bedingungen muessen erfuellt sein (Art. 16 Abs. 4 a-d)
        return gesetz * kosten * angemessen * reserven
