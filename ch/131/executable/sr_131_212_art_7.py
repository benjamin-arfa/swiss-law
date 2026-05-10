"""SR 131.212 Art. 7

Generated from: ch/131/de/131.212.md

Kantons- und Gemeindebuergerrecht: Conditions under which naturalisation
is excluded in Canton Bern (criminal conviction, social welfare dependency,
insufficient language skills, insufficient civic knowledge, no settlement permit).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verurteilt_wegen_verbrechen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person wegen eines Verbrechens rechtskraeftig verurteilt wurde"
    reference = "SR 131.212 Art. 7 Abs. 3 Bst. a"


class verurteilt_freiheitsstrafe_2_jahre(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person zu einer Freiheitsstrafe von mindestens 2 Jahren verurteilt wurde"
    reference = "SR 131.212 Art. 7 Abs. 3 Bst. a"


class bezieht_sozialhilfe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Sozialhilfe bezieht oder bezogene Leistungen nicht zurueckbezahlt hat"
    reference = "SR 131.212 Art. 7 Abs. 3 Bst. b"


class gute_amtssprachkenntnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nachweislich ueber gute Kenntnisse einer Amtssprache verfuegt"
    reference = "SR 131.212 Art. 7 Abs. 3 Bst. c"


class ausreichende_staatskenntnisse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ausreichende Kenntnisse des schweizerischen und kantonalen Staatsaufbaus hat"
    reference = "SR 131.212 Art. 7 Abs. 3 Bst. d"


class hat_niederlassungsverfuegung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ueber eine Niederlassungsverfuegung verfuegt"
    reference = "SR 131.212 Art. 7 Abs. 3 Bst. e"


class einbuergerung_ausgeschlossen_bern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einbuergerung im Kanton Bern ausgeschlossen ist"
    reference = "SR 131.212 Art. 7 Abs. 3"

    def formula(person, period, parameters):
        import numpy as np
        verbrechen = person('verurteilt_wegen_verbrechen', period)
        freiheitsstrafe = person('verurteilt_freiheitsstrafe_2_jahre', period)
        sozialhilfe = person('bezieht_sozialhilfe', period)
        sprache = np.logical_not(person('gute_amtssprachkenntnisse', period))
        staat = np.logical_not(person('ausreichende_staatskenntnisse', period))
        niederlassung = np.logical_not(person('hat_niederlassungsverfuegung', period))
        return (verbrechen + freiheitsstrafe + sozialhilfe + sprache + staat + niederlassung) > 0
