"""SR 446.2 Art. 12

Generated from: ch/446/de/446.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_altersstufen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl verschiedene Altersstufen im Altersklassifizierungssystem"
    reference = "SR 446.2 Art. 12 Abs. 2 Bst. b"


class hoechste_altersstufe_nur_volljaehrige(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hoechste Altersstufe ist volljaehrigen Personen vorbehalten"
    reference = "SR 446.2 Art. 12 Abs. 2 Bst. b"


class einheitliche_klassifizierungskriterien(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einheitliche Kriterien fuer die Klassifizierung aller Filme bzw. Videospiele"
    reference = "SR 446.2 Art. 12 Abs. 2 Bst. a"


class altersklassifizierungssystem_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Altersklassifizierungssystem erfuellt die Anforderungen nach Art. 12"
    reference = "SR 446.2 Art. 12"

    def formula(person, period, parameters):
        stufen = person('anzahl_altersstufen', period)
        volljaehrige = person('hoechste_altersstufe_nur_volljaehrige', period)
        einheitlich = person('einheitliche_klassifizierungskriterien', period)
        return (stufen >= 5) * volljaehrige * einheitlich
