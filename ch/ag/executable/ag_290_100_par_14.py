"""AG 290.100 § 14

Generated from: ch/ag/de/290.100.md

§ 14 Kostentragung: Costs are borne by the complainant (if malicious),
by the lawyer (if punished or at fault), or by the state (otherwise).
Party cost compensation may be imposed where justified.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ag_disziplinar_anzeige_mutwillig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Disziplinaranzeige mutwillig oder troelerisch erstattet (AG 290.100 § 14 Abs. 1)"
    reference = "AG 290.100 § 14 Abs. 1"


class ag_disziplinar_anwalt_bestraft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anwalt im Disziplinarverfahren bestraft oder schuldhaft veranlasst (AG 290.100 § 14 Abs. 1)"
    reference = "AG 290.100 § 14 Abs. 1"


class ag_disziplinar_kosten_traeger(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Kostenpflichtige Person im Disziplinarverfahren (AG 290.100 § 14)"
    reference = "AG 290.100 § 14 Abs. 1"

    def formula(person, period, parameters):
        mutwillig = person('ag_disziplinar_anzeige_mutwillig', period)
        bestraft = person('ag_disziplinar_anwalt_bestraft', period)
        # Priority: complainant if malicious, lawyer if punished, else state
        return where(mutwillig, 'anzeigende_person',
                     where(bestraft, 'anwalt', 'staat'))
