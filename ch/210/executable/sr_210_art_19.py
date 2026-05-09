"""SR 210 Art. 19

Generated from: ch/de/210.md

Urteilsfaehige handlungsunfaehige Personen: Koennen nur mit Zustimmung
ihres gesetzlichen Vertreters Verpflichtungen eingehen oder Rechte aufgeben.
Ohne Zustimmung koennen sie unentgeltliche Vorteile erlangen und
geringfuegige Alltagsgeschaefte besorgen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kann_verpflichtungen_eingehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person selbstaendig Verpflichtungen eingehen kann"
    reference = "SR 210 Art. 19"

    def formula(person, period, parameters):
        ist_handlungsfaehig = person('ist_handlungsfaehig', period)
        # Abs. 1: Urteilsfaehige Handlungsunfaehige brauchen Zustimmung
        # des gesetzlichen Vertreters
        hat_zustimmung_vertreter = person('hat_zustimmung_gesetzlicher_vertreter', period)
        ist_urteilsfaehig = person('ist_urteilsfaehig', period)
        ist_handlungsunfaehig = person('ist_handlungsunfaehig', period)

        # Voll handlungsfaehig: ja
        # Urteilsfaehig aber handlungsunfaehig: nur mit Zustimmung
        return ist_handlungsfaehig + (ist_urteilsfaehig * ist_handlungsunfaehig * hat_zustimmung_vertreter) > 0


class kann_unentgeltliche_vorteile_erlangen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person ohne Zustimmung unentgeltliche Vorteile erlangen kann"
    reference = "SR 210 Art. 19 Abs. 2"

    def formula(person, period, parameters):
        # Abs. 2: Urteilsfaehige Handlungsunfaehige koennen ohne Zustimmung
        # unentgeltliche Vorteile erlangen und geringfuegige Alltagsgeschaefte
        # besorgen
        ist_urteilsfaehig = person('ist_urteilsfaehig', period)
        return ist_urteilsfaehig


class hat_zustimmung_gesetzlicher_vertreter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Zustimmung des gesetzlichen Vertreters vorliegt"
    reference = "SR 210 Art. 19 Abs. 1"
