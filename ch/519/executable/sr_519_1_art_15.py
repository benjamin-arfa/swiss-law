"""SR 519.1 Art. 15

Generated from: ch/519/de/519.1.md

Art. 15 Ferien (Vacation):
1. Personnel have an entitlement to 6 weeks vacation per year during deployment.
   Exceptionally, the VBS may grant one additional vacation week from age 50.
2. This entitlement covers public holidays at the deployment location.
   Official Swiss public holidays falling on a workday may be compensated with
   paid leave if operational needs permit.
3. Vacation must be taken during the deployment. If not possible:
   a. for federal employees: credited to existing vacation balance
   b. for other personnel: paid out at end of deployment
4. Federal employees' vacation entitlement from their original employment is
   reduced proportionally to the deployment duration.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pvspa_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Age of the deployed person"
    reference = "SR 519.1 Art. 15 Abs. 1"


class pvspa_ferienanspruch_wochen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Annual vacation entitlement in weeks during deployment"
    reference = "SR 519.1 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        alter = person('pvspa_alter', period)
        basis_wochen = 6
        zusatz = where(alter >= 50, 1, 0)
        return basis_wochen + zusatz


class pvspa_ferienanspruch_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Annual vacation entitlement in days during deployment (weeks * 5 workdays)"
    reference = "SR 519.1 Art. 15 Abs. 1"

    def formula(person, period, parameters):
        wochen = person('pvspa_ferienanspruch_wochen', period)
        return wochen * 5


class pvspa_ferien_ausbezahlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether unused vacation is paid out at end of deployment (non-federal employees)"
    reference = "SR 519.1 Art. 15 Abs. 3 Bst. b"

    def formula(person, period, parameters):
        ist_bundesangestellter = person('pvspa_ist_bundesangestellter', period.first_month)
        return not_(ist_bundesangestellter)
