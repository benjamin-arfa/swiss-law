"""SR 814.01 Art. 32

Generated from: ch/814/de/814.01.md

Abfallentsorgung Grundsatz: Inhaber traegt die Kosten der Entsorgung.
Kanton traegt Kosten wenn Inhaber nicht ermittelbar oder zahlungsunfaehig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_abfall_inhaber(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Inhaber von Abfaellen ist"
    reference = "SR 814.01 Art. 32 Abs. 1"


class abfall_inhaber_ermittelbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Inhaber der Abfaelle ermittelt werden kann"
    reference = "SR 814.01 Art. 32 Abs. 2"


class abfall_inhaber_zahlungsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Inhaber der Abfaelle zahlungsfaehig ist"
    reference = "SR 814.01 Art. 32 Abs. 2"


class entsorgungskosten_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Betrag der Entsorgungskosten in CHF"
    reference = "SR 814.01 Art. 32"


class traegt_entsorgungskosten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person die Entsorgungskosten traegt"
    reference = "SR 814.01 Art. 32"

    def formula(person, period, parameters):
        ist_inhaber = person('ist_abfall_inhaber', period)
        ermittelbar = person('abfall_inhaber_ermittelbar', period)
        zahlungsfaehig = person('abfall_inhaber_zahlungsfaehig', period)
        # Inhaber traegt Kosten wenn ermittelbar und zahlungsfaehig
        return ist_inhaber * ermittelbar * zahlungsfaehig


class kanton_traegt_entsorgungskosten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Kanton die Entsorgungskosten traegt (Inhaber nicht ermittelbar oder zahlungsunfaehig)"
    reference = "SR 814.01 Art. 32 Abs. 2"

    def formula(person, period, parameters):
        ermittelbar = person('abfall_inhaber_ermittelbar', period)
        zahlungsfaehig = person('abfall_inhaber_zahlungsfaehig', period)
        # Kanton zahlt wenn Inhaber nicht ermittelbar ODER zahlungsunfaehig
        return (1 - ermittelbar) + ermittelbar * (1 - zahlungsfaehig) > 0
