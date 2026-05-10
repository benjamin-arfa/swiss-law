"""SR 744.103 Art. 9

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unternehmen_hat_zulassungsbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen ist Inhaberin einer Zulassungsbewilligung als Strassentransportunternehmen oder verfügt über eine andere Bewilligung für den grenzüberschreitenden Güterverkehr"
    reference = "SR 744.103 Art. 9 Abs. 1 lit. a"

    def formula(person, period, parameters):
        return person('hat_zulassung_strassentransport', period) | person('hat_bewilligung_grenzueberschreitend', period)


class hat_zulassung_strassentransport(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen ist Inhaberin einer Zulassungsbewilligung als Strassentransportunternehmen"
    reference = "SR 744.103 Art. 9 Abs. 1 lit. a"


class hat_bewilligung_grenzueberschreitend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen verfügt über eine andere Bewilligung für den grenzüberschreitenden Güterverkehr"
    reference = "SR 744.103 Art. 9 Abs. 1 lit. a"


class fahrer_regelkonform_beschaeftigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fahrer oder Fahrerin wird gemäss fremdenpolizei-, sozialversicherungs- und arbeitsrechtlichen Bestimmungen beschäftigt oder eingesetzt"
    reference = "SR 744.103 Art. 9 Abs. 1 lit. b"


class fahrerbescheinigung_erteilbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAV kann dem schweizerischen Strassentransportunternehmen eine Fahrerbescheinigung erteilen"
    reference = "SR 744.103 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        hat_bewilligung = person('unternehmen_hat_zulassungsbewilligung', period)
        regelkonform = person('fahrer_regelkonform_beschaeftigt', period)
        return hat_bewilligung & regelkonform


class fahrerbescheinigung_max_gueltigkeit_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Gültigkeitsdauer der Fahrerbescheinigung in Jahren"
    reference = "SR 744.103 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        return 5
