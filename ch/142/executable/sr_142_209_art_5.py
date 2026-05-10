"""SR 142.209 Art. 5

Generated from: ch/142/de/142.209.md

Gebuehrenzuschlag: Bis zu 50 Prozent fuer dringliche Verfuegungen,
ausserhalb der normalen Arbeitszeit, aussergewoehnlicher Umfang
oder besonderer Schwierigkeit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_dringliche_verfuegung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verfuegung dringlich oder ausserhalb der normalen Arbeitszeit erlassen wird"
    reference = "SR 142.209 Art. 5"


class ist_aussergewoehnlicher_umfang(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verfahren aussergewoehnlichen Umfangs oder besonderer Schwierigkeit ist"
    reference = "SR 142.209 Art. 5"


class gebuehrenzuschlag_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gebuehrenzuschlag in Prozent (max. 50%)"
    reference = "SR 142.209 Art. 5"

    def formula(person, period, parameters):
        dringlich = person('ist_dringliche_verfuegung', period)
        aussergewoehnlich = person('ist_aussergewoehnlicher_umfang', period)
        # Zuschlag nur wenn einer der Gruende vorliegt, max. 50%
        return where(dringlich + aussergewoehnlich > 0, 50.0, 0.0)
