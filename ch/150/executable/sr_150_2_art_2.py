"""SR 150.2 Art. 2

Generated from: ch/150/de/150.2.md

Definition: Als verschwunden gilt jede Person, der im Auftrag oder
mit Billigung des Staates die Freiheit entzogen wurde, ueber deren
Schicksal die Auskunft verweigert wird und die dadurch dem Schutz
des Gesetzes entzogen ist.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class freiheitsentzug_im_auftrag_staat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Person im Auftrag oder mit Billigung des Staates die Freiheit entzogen wurde"
    reference = "SR 150.2 Art. 2"


class auskunft_ueber_schicksal_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Auskunft ueber Schicksal oder Verbleib verweigert wird"
    reference = "SR 150.2 Art. 2"


class dem_schutz_des_gesetzes_entzogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person dadurch dem Schutz des Gesetzes entzogen ist"
    reference = "SR 150.2 Art. 2"


class gilt_als_verschwunden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als verschwunden im Sinne des Gesetzes gilt"
    reference = "SR 150.2 Art. 2"

    def formula(person, period, parameters):
        return (
            person('freiheitsentzug_im_auftrag_staat', period)
            * person('auskunft_ueber_schicksal_verweigert', period)
            * person('dem_schutz_des_gesetzes_entzogen', period)
        )
