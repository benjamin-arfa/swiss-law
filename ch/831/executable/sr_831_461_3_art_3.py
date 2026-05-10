"""SR 831.461.3 Art. 3

Generated from: ch/831/de/831.461.3.md

Timing of pillar 3a benefit payments:
- Earliest: 5 years before reaching reference age
- Due at reference age
- Can be deferred up to 5 years past reference age if still employed
- Early withdrawal permitted for: full IV disability, change of
  self-employment, mandatory cash payout per FZG Art. 5,
  home ownership acquisition, mortgage repayment
- Spousal/partner consent required for early withdrawal in cases c, d, and 3
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bvv3_referenzalter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    default_value = 65
    label = "Referenzalter nach Art. 13 Abs. 1 BVG"
    reference = "SR 831.461.3 Art. 3 Abs. 1"


class bvv3_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der versicherten Person"
    reference = "SR 831.461.3 Art. 3"


class bvv3_weiterhin_erwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nach Erreichen des Referenzalters weiterhin erwerbstaetig ist"
    reference = "SR 831.461.3 Art. 3 Abs. 1"


class bvv3_bezieht_ganze_iv_rente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine ganze Invalidenrente der IV bezieht"
    reference = "SR 831.461.3 Art. 3 Abs. 2 Bst. a"


class bvv3_aufgabe_selbstaendige_taetigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ihre selbstaendige Erwerbstaetigkeit aufgibt und eine andersartige aufnimmt"
    reference = "SR 831.461.3 Art. 3 Abs. 2 Bst. c"


class bvv3_barauszahlungspflicht_fzg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Barauszahlungspflicht nach Art. 5 FZG besteht"
    reference = "SR 831.461.3 Art. 3 Abs. 2 Bst. d"


class bvv3_wohneigentum_erwerb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Vorbezug fuer Wohneigentum zum Eigenbedarf beantragt wird"
    reference = "SR 831.461.3 Art. 3 Abs. 3"


class bvv3_anspruch_altersleistung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Anspruch auf Ausrichtung der Altersleistung der Saeule 3a besteht"
    reference = "SR 831.461.3 Art. 3"

    def formula(person, period, parameters):
        alter = person('bvv3_alter', period)
        ref_alter = person('bvv3_referenzalter', period)
        erwerbstaetig = person('bvv3_weiterhin_erwerbstaetig', period)

        # Regular entitlement: from 5 years before reference age
        fruehester_bezug = ref_alter - 5
        regulaer = alter >= fruehester_bezug

        # Deferral: up to 5 years past reference age if still employed
        spaetester_bezug = ref_alter + 5
        aufgeschoben = erwerbstaetig * (alter <= spaetester_bezug)

        # Early withdrawal grounds
        iv_rente = person('bvv3_bezieht_ganze_iv_rente', period)
        selbstaendig = person('bvv3_aufgabe_selbstaendige_taetigkeit', period)
        barauszahlung = person('bvv3_barauszahlungspflicht_fzg', period)
        wohneigentum = person('bvv3_wohneigentum_erwerb', period)

        vorzeitig = iv_rente + selbstaendig + barauszahlung + wohneigentum

        return regulaer + vorzeitig
