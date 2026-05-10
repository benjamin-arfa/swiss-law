"""SR 446.21 Art. 4

Generated from: ch/446/de/446.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class taetig_bei_kinderschutzorganisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetig bei einer anerkannten Kinder- oder Jugendschutzorganisation"
    reference = "SR 446.21 Art. 4 Abs. 1 Bst. a"


class taetig_an_hochschule_kinderschutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetig an einer Hochschule im Themenfeld Kinder- oder Jugendschutz"
    reference = "SR 446.21 Art. 4 Abs. 1 Bst. b"


class langjaehrige_erfahrung_kinderschutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verfuegt ueber langjaehrige praktische Erfahrung im Kinder- oder Jugendschutz"
    reference = "SR 446.21 Art. 4 Abs. 1 Bst. c"


class unabhaengig_von_akteurinnen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist von den Akteurinnen im Bereich Film bzw. Videospiele unabhaengig"
    reference = "SR 446.21 Art. 4 Abs. 2"


class erfuellt_anforderungen_experte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erfuellt die Anforderungen als beigezogene Expertin/Experte"
    reference = "SR 446.21 Art. 4"

    def formula(person, period, parameters):
        org = person('taetig_bei_kinderschutzorganisation', period)
        hochschule = person('taetig_an_hochschule_kinderschutz', period)
        erfahrung = person('langjaehrige_erfahrung_kinderschutz', period)
        unabhaengig = person('unabhaengig_von_akteurinnen', period)
        fachlich = (org + hochschule + erfahrung) >= 1
        return fachlich * unabhaengig
