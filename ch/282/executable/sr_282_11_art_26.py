"""SR 282.11 Art. 26 - Nicht betroffene Verpflichtungen

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verpflichtung_ist_oeffentlichrechtlich_gesetzlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verpflichtung ist eine gesetzlich begruendete oeffentlichrechtliche Verpflichtung"
    reference = "SR 282.11 Art. 26"


class verpflichtung_ist_versicherungsbeitrag(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verpflichtung ist ein Versicherungsbeitrag"
    reference = "SR 282.11 Art. 26"


class verpflichtung_ist_besoldung_oder_pension(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verpflichtung ist eine Besoldung, Dienstentschaedigung oder Pension"
    reference = "SR 282.11 Art. 26"


class verpflichtung_ist_unpfaendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verpflichtung stellt eine unpfaendbare Forderung dar"
    reference = "SR 282.11 Art. 26"


class verpflichtung_nicht_betroffen_von_massnahmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Verpflichtung ist von den Massnahmen nicht betroffen"
    reference = "SR 282.11 Art. 26"

    def formula(self, period, parameters):
        oeffentlich = self('verpflichtung_ist_oeffentlichrechtlich_gesetzlich', period)
        versicherung = self('verpflichtung_ist_versicherungsbeitrag', period)
        besoldung = self('verpflichtung_ist_besoldung_oder_pension', period)
        unpfaendbar = self('verpflichtung_ist_unpfaendbar', period)
        return oeffentlich + versicherung + besoldung + unpfaendbar > 0
