"""SR 642.116 Art. 2

Generated from: ch/642/de/642.116.md

Art. 2: Demolition costs for replacement construction
(Rueckbaukosten im Hinblick auf den Ersatzneubau)

Deductible demolition costs include: dismantling of installations,
demolition of the pre-existing building, transport and disposal of
construction waste.

Not deductible: contaminated site remediation, terrain modifications,
clearing, leveling, excavation for the replacement building.

Costs must be itemized separately. Only deductible if the replacement
construction is undertaken by the same taxpayer.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class liegenschaft_rueckbaukosten_demontage(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Demontagekosten (CHF)"
    reference = "SR 642.116 Art. 2 Abs. 1, 3"


class liegenschaft_rueckbaukosten_abbruch(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abbruchkosten (CHF)"
    reference = "SR 642.116 Art. 2 Abs. 1, 3"


class liegenschaft_rueckbaukosten_abtransport(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abtransportkosten (CHF)"
    reference = "SR 642.116 Art. 2 Abs. 1, 3"


class liegenschaft_rueckbaukosten_entsorgung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Entsorgungskosten (CHF)"
    reference = "SR 642.116 Art. 2 Abs. 1, 3"


class liegenschaft_ersatzneubau_gleicher_eigentuemer(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ersatzneubau wird durch dieselbe steuerpflichtige Person vorgenommen"
    reference = "SR 642.116 Art. 2 Abs. 4"
    default_value = True


class liegenschaft_rueckbaukosten_abzug(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abziehbare Rueckbaukosten im Hinblick auf den Ersatzneubau (CHF)"
    reference = "SR 642.116 Art. 2"

    def formula(person, period, parameters):
        demontage = person('liegenschaft_rueckbaukosten_demontage', period)
        abbruch = person('liegenschaft_rueckbaukosten_abbruch', period)
        abtransport = person('liegenschaft_rueckbaukosten_abtransport', period)
        entsorgung = person('liegenschaft_rueckbaukosten_entsorgung', period)
        gleicher_eigentuemer = person('liegenschaft_ersatzneubau_gleicher_eigentuemer', period)

        # Art. 2 Abs. 4: only deductible if replacement by same taxpayer
        total = demontage + abbruch + abtransport + entsorgung
        return total * gleicher_eigentuemer
