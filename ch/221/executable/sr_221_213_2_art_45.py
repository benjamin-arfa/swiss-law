"""SR 221.213.2 Art. 45

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pachtzins_uebersteigt_zulaessiges_mass(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vereinbarter Pachtzins übersteigt das behördlich festgesetzte Mass"
    reference = "SR 221.213.2 Art. 45 Abs. 1"


class pachtzinsvereinbarung_nichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pachtzinsvereinbarung ist nichtig soweit sie das zulässige Mass übersteigt"
    reference = "SR 221.213.2 Art. 45 Abs. 1"

    def formula(person, period, parameters):
        return person('pachtzins_uebersteigt_zulaessiges_mass', period)


class jahre_seit_bezahlung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahre seit Bezahlung des überhöhten Pachtzinses"
    reference = "SR 221.213.2 Art. 45 Abs. 2"


class jahre_seit_rechtskraeftigem_entscheid(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahre seit dem rechtskräftigen Entscheid über den Pachtzins"
    reference = "SR 221.213.2 Art. 45 Abs. 2"


class rueckforderung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rückforderung des zu viel bezahlten Pachtzinses ist möglich"
    reference = "SR 221.213.2 Art. 45 Abs. 2"

    def formula(person, period, parameters):
        nichtig = person('pachtzinsvereinbarung_nichtig', period)
        seit_entscheid = person('jahre_seit_rechtskraeftigem_entscheid', period)
        seit_bezahlung = person('jahre_seit_bezahlung', period)
        # Innerhalb 1 Jahr seit Entscheid UND spätestens 5 Jahre seit Bezahlung
        frist_eingehalten = (seit_entscheid <= 1) * (seit_bezahlung <= 5)
        return nichtig * frist_eingehalten
