"""SR 832.105 Art. 1

Generated from: ch/fr/832/832.105.md

Art. 1: Principe - Carte d'assure (Versichertenkarte)
- Abs. 1: Insurers must issue an insurance card to all persons required to be insured
  under KVV/OAMal.
- Abs. 2: Persons insured under Art. 1(2)(d-ebis) OAMal who cannot receive benefits
  in Switzerland (except via international mutual assistance) do not receive a card.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kvg_versicherungspflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person obligatorisch krankenversichert ist"
    reference = "SR 832.105 Art. 1 Abs. 1"


class kvg_leistungsbezug_schweiz_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    default_value = True
    label = "Ob die Person Leistungen in der Schweiz beziehen kann"
    reference = "SR 832.105 Art. 1 Abs. 2"


class kvg_versichertenkarte_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Anspruch auf eine Versichertenkarte hat"
    reference = "SR 832.105 Art. 1"

    def formula(person, period, parameters):
        versichert = person('kvg_versicherungspflichtig', period)
        leistung_ch = person('kvg_leistungsbezug_schweiz_moeglich', period)
        return versichert * leistung_ch
