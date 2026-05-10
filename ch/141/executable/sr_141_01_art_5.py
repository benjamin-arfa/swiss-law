"""SR 141.01 Art. 5

Generated from: ch/141/de/141.01.md

Respektierung der Werte der Bundesverfassung: Rechtsstaatliche Prinzipien,
Grundrechte (Gleichberechtigung, Lebensrecht, Freiheiten), Pflichten
(Militaer-/Ersatzdienst, Schulbesuch).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class respektiert_rechtsstaatliche_prinzipien(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die rechtsstaatlichen Prinzipien und die freiheitlich demokratische Grundordnung respektiert werden"
    reference = "SR 141.01 Art. 5 Bst. a"


class respektiert_grundrechte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Grundrechte (Gleichberechtigung, Lebensrecht, persoenliche Freiheit, Gewissensfreiheit, Meinungsfreiheit) respektiert werden"
    reference = "SR 141.01 Art. 5 Bst. b"


class respektiert_pflichten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Pflicht zum Militaer-/Ersatzdienst und Schulbesuch respektiert wird"
    reference = "SR 141.01 Art. 5 Bst. c"


class respektiert_werte_bundesverfassung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Werte der Bundesverfassung respektiert werden"
    reference = "SR 141.01 Art. 5"

    def formula(person, period, parameters):
        prinzipien = person('respektiert_rechtsstaatliche_prinzipien', period)
        grundrechte = person('respektiert_grundrechte', period)
        pflichten = person('respektiert_pflichten', period)
        return prinzipien * grundrechte * pflichten
