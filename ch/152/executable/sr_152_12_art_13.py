"""SR 152.12 Art. 13 - Einsichtnahme waehrend der Schutzfrist (Access During Protection Period)

Generated from: ch/152/de/152.12.md

Access during the protection period may be granted if the applicant
demonstrates a legitimate interest, particularly when:
a) consent of affected persons exists
b) affected persons have been deceased for at least 3 years
c) documents were already publicly accessible
d) justified for scientific purposes while preserving the protective purpose
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einverstaendnis_betroffener_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Einverstaendnis der betroffenen Personen vorliegt"
    reference = "SR 152.12 Art. 13 Abs. 1 lit. a"


class betroffene_seit_3_jahren_verstorben_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die betroffenen Personen seit mindestens 3 Jahren verstorben sind"
    reference = "SR 152.12 Art. 13 Abs. 1 lit. b"


class unterlagen_bereits_oeffentlich_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unterlagen bereits der Oeffentlichkeit zugaenglich waren"
    reference = "SR 152.12 Art. 13 Abs. 1 lit. c"


class wissenschaftliche_taetigkeit_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einsichtnahme fuer eine wissenschaftliche Taetigkeit gerechtfertigt ist"
    reference = "SR 152.12 Art. 13 Abs. 1 lit. d"


class hat_schutzwuerdiges_interesse_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Gesuchsteller ein schutzwuerdiges Interesse nachweist"
    reference = "SR 152.12 Art. 13 Abs. 1"


class einsichtnahme_waehrend_schutzfrist_bstger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Einsichtnahme waehrend der Schutzfrist gewaehrt werden kann"
    reference = "SR 152.12 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        interesse = person('hat_schutzwuerdiges_interesse_bstger', period)
        einverstaendnis = person('einverstaendnis_betroffener_bstger', period)
        verstorben = person('betroffene_seit_3_jahren_verstorben_bstger', period)
        oeffentlich = person('unterlagen_bereits_oeffentlich_bstger', period)
        wissenschaft = person('wissenschaftliche_taetigkeit_bstger', period)

        grund_vorhanden = (einverstaendnis + verstorben + oeffentlich + wissenschaft) > 0
        return interesse * grund_vorhanden
