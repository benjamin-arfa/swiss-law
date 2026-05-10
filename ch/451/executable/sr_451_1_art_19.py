"""SR 451.1 Art. 19

Generated from: ch/451/de/451.1.md
Verhaeltnis zu oekologischen Leistungen in der Landwirtschaft - Kuerzungsregel.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class abgeltung_biotopschutz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Abgeltung nach Art. 18 NHV fuer Biotopschutz in CHF"
    reference = "SR 451.1 Art. 18"


class direktzahlungsbeitraege_gleiche_leistung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Beitraege nach Direktzahlungsverordnung fuer gleiche oekologische Leistung in CHF"
    reference = "SR 451.1 Art. 19"


class abgeltung_biotopschutz_gekuerzt(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gekuerzte Abgeltung fuer Biotopschutz (abzueglich Direktzahlungen) in CHF"
    reference = "SR 451.1 Art. 19"

    def formula(person, period, parameters):
        abgeltung = person('abgeltung_biotopschutz', period)
        direktzahlung = person('direktzahlungsbeitraege_gleiche_leistung', period)
        return max_(abgeltung - direktzahlung, 0)
