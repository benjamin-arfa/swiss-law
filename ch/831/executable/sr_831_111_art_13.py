"""SR 831.111 Art. 13

Generated from: ch/831/de/831.111.md

Art. 13: Ausschluss - Exclusion from voluntary insurance.

Abs. 1: Insured persons are excluded if:
a. contributions for the contribution year are not fully paid by
   31 December of the following calendar year
b. default interest is not paid by 31 December of the year following
   the year in which it was legally established
c. required documents are not submitted by 31 December of the year
   following the contribution year

Abs. 3: Exclusion is retroactive to the first day of the contribution year.

Abs. 4: Exclusion does not apply if payment was impossible due to
force majeure or transfer to Switzerland was impossible.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vfv_beitraege_vollstaendig_bezahlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beitraege fuer das Beitragsjahr vollstaendig bezahlt (Art. 13 Abs. 1 Bst. a VFV)"
    reference = "SR 831.111 Art. 13 Abs. 1 Bst. a"


class vfv_verzugszinsen_bezahlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verzugszinsen vollstaendig bezahlt (Art. 13 Abs. 1 Bst. b VFV)"
    reference = "SR 831.111 Art. 13 Abs. 1 Bst. b"


class vfv_belege_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verlangte Belege fristgerecht eingereicht (Art. 13 Abs. 1 Bst. c VFV)"
    reference = "SR 831.111 Art. 13 Abs. 1 Bst. c"


class vfv_hoehere_gewalt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Beitraege konnten infolge hoeherer Gewalt nicht rechtzeitig entrichtet werden"
    reference = "SR 831.111 Art. 13 Abs. 4"


class vfv_ausschluss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausschluss aus der freiwilligen Versicherung (Art. 13 VFV)"
    reference = "SR 831.111 Art. 13"

    def formula(person, period, parameters):
        beitraege_ok = person('vfv_beitraege_vollstaendig_bezahlt', period)
        zinsen_ok = person('vfv_verzugszinsen_bezahlt', period)
        belege_ok = person('vfv_belege_eingereicht', period)
        hoehere_gewalt = person('vfv_hoehere_gewalt', period)

        # Exclusion if any obligation not met AND no force majeure
        grund_fuer_ausschluss = not_(beitraege_ok) + not_(zinsen_ok) + not_(belege_ok)
        return (grund_fuer_ausschluss > 0) * not_(hoehere_gewalt)
