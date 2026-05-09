"""SR 143.1 Art. 6 - Entscheid (Decision on Application)

Generated from: ch/143/de/143.1.md

The issuing authority decides on the application. Issuance is refused if:
- it would contradict an order by a Swiss authority
- applicant has deposited documents with prosecution/enforcement authority
- applicant is wanted for arrest (RIPOL) for a felony or misdemeanor
- applicant abroad is being prosecuted or convicted for a crime
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class widerspricht_behoerdlicher_verfuegung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Ausweisausstellung einer behoerdlichen Verfuegung widersprechen wuerde"
    reference = "SR 143.1 Art. 6 Abs. 3 lit. a"


class ausweis_bei_strafbehoerde_hinterlegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Ausweise bei einer Strafverfolgungs- oder Strafvollzugsbehoerde hinterlegt sind"
    reference = "SR 143.1 Art. 6 Abs. 3 lit. b"


class in_ripol_zur_verhaftung_ausgeschrieben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person im RIPOL wegen Verbrechen oder Vergehen zur Verhaftung ausgeschrieben ist"
    reference = "SR 143.1 Art. 6 Abs. 4"


class befindet_sich_im_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob sich die Person im Ausland befindet"
    reference = "SR 143.1 Art. 6 Abs. 5"


class im_ausland_strafrechtlich_verfolgt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person im Ausland wegen eines Verbrechens oder Vergehens verfolgt oder verurteilt wird"
    reference = "SR 143.1 Art. 6 Abs. 5"


class ausweisausstellung_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Ausstellung des Ausweises verweigert wird"
    reference = "SR 143.1 Art. 6 Abs. 3-5"

    def formula(person, period, parameters):
        verfuegung = person('widerspricht_behoerdlicher_verfuegung', period)
        hinterlegt = person('ausweis_bei_strafbehoerde_hinterlegt', period)
        ripol = person('in_ripol_zur_verhaftung_ausgeschrieben', period)
        im_ausland = person('befindet_sich_im_ausland', period)
        ausland_straf = person('im_ausland_strafrechtlich_verfolgt', period)
        # Verweigerung wenn: Verfuegung widerspricht, Ausweis hinterlegt, RIPOL,
        # oder im Ausland befindlich und dort strafrechtlich verfolgt
        return (verfuegung + hinterlegt + ripol + (im_ausland * ausland_straf)) > 0
