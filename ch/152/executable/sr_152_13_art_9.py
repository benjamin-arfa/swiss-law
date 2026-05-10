"""SR 152.13 Art. 9 - Einsichtnahme in die Prozessakten waehrend der Schutzfrist

Generated from: ch/152/de/152.13.md

Access to case files during the protection period may be granted if:
a) consent of affected persons exists
b) affected persons have been deceased for at least 3 years

The court respects the rights of parties and affected third persons.
Access can be limited to parts of the files; files may be anonymized.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einverstaendnis_betroffener_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Einverstaendnis der betroffenen Personen vorliegt"
    reference = "SR 152.13 Art. 9 Abs. 1 lit. a"


class betroffene_seit_3_jahren_verstorben_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die betroffenen Personen seit mindestens 3 Jahren verstorben sind"
    reference = "SR 152.13 Art. 9 Abs. 1 lit. b"


class einsichtnahme_prozessakten_waehrend_schutzfrist_bvger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Einsichtnahme in Prozessakten waehrend der Schutzfrist gewaehrt werden kann"
    reference = "SR 152.13 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        einverstaendnis = person('einverstaendnis_betroffener_bvger', period)
        verstorben = person('betroffene_seit_3_jahren_verstorben_bvger', period)
        return (einverstaendnis + verstorben) > 0
