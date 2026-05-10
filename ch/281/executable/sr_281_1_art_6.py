"""SR 281.1 Art. 6

Generated from: ch/281/de/281.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class jahre_seit_kenntnis_schaedigung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahre seit Kenntnis der Schädigung"
    reference = "SR 281.1 Art. 6 Abs. 1"


class jahre_seit_schaedigendem_verhalten(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahre seit dem schädigenden Verhalten"
    reference = "SR 281.1 Art. 6 Abs. 1"


class schaediger_beging_strafbare_handlung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schädiger hat durch sein Verhalten eine strafbare Handlung begangen"
    reference = "SR 281.1 Art. 6 Abs. 2"


class strafrechtliche_verfolgungsverjaehrung_eingetreten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Strafrechtliche Verfolgungsverjährung ist eingetreten"
    reference = "SR 281.1 Art. 6 Abs. 2"


class schadenersatzanspruch_verjaehrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf Schadenersatz ist verjährt"
    reference = "SR 281.1 Art. 6"

    def formula(person, period, parameters):
        seit_kenntnis = person('jahre_seit_kenntnis_schaedigung', period)
        seit_verhalten = person('jahre_seit_schaedigendem_verhalten', period)
        strafbar = person('schaediger_beging_strafbare_handlung', period)
        straf_verjaehrt = person('strafrechtliche_verfolgungsverjaehrung_eingetreten', period)

        # Ordentliche Verjährung: 3 Jahre seit Kenntnis ODER 10 Jahre seit Verhalten
        ordentlich_verjaehrt = (seit_kenntnis > 3) + (seit_verhalten > 10)

        # Bei Straftat: verjährt frühestens mit strafrechtlicher Verfolgungsverjährung
        # bzw. 3 Jahre nach erstinstanzlichem Urteil
        bei_straftat_verjaehrt = strafbar * straf_verjaehrt * ordentlich_verjaehrt

        # Ohne Straftat: ordentliche Verjährung
        ohne_straftat_verjaehrt = not_(strafbar) * ordentlich_verjaehrt

        return bei_straftat_verjaehrt + ohne_straftat_verjaehrt
