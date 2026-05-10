"""SR 721.80 Art. 14

Generated from: ch/721/de/721.80.md

Art. 14 - Tax compensation for federal use of water power:
1. The Confederation pays cantons CHF 11/year per kW of installed gross capacity
   as compensation for lost cantonal, communal, and other taxes.
1bis. Also applies when the Confederation uses water power based on a concession
   or other legal title.
2. If the water stretches are in multiple cantons, each canton's share is
   proportional to its contribution to the power generation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wrg_bruttoleistung_kw(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Installed gross capacity of the water power plant (kW)"
    reference = "SR 721.80 Art. 14 Abs. 1"


class wrg_bundesnutzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the water power is used by the Confederation"
    reference = "SR 721.80 Art. 14 Abs. 1"


class wrg_kanton_anteil_leistung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Canton's proportional share of the power generation (0-1)"
    reference = "SR 721.80 Art. 14 Abs. 2"
    default_value = 1.0


class wrg_steuerausfall_entschaedigung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tax compensation paid by Confederation to canton (CHF/year)"
    reference = "SR 721.80 Art. 14"

    def formula(person, period, parameters):
        bruttoleistung = person('wrg_bruttoleistung_kw', period)
        bundesnutzung = person('wrg_bundesnutzung', period)
        kanton_anteil = person('wrg_kanton_anteil_leistung', period)
        satz = parameters(period).sr_721_80.steuerausfall_entschaedigung_pro_kw

        return where(bundesnutzung, bruttoleistung * satz * kanton_anteil, 0)
