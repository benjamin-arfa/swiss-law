"""SR 416.211 Art. 2

Generated from: ch/416/de/416.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_stipendiat_in(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Stipendiat/in des Bundes (auslaendische Studierende/Kunstschaffende)"
    reference = "SR 416.211 Art. 2"


class ist_buerger_in_ausserhalb_eu_efta(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Buerger/in eines Landes ausserhalb der EU und der EFTA"
    reference = "SR 416.211 Art. 2 Abs. 1"


class ist_begleitendes_familienmitglied(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist begleitendes Familienmitglied eines Stipendiaten"
    reference = "SR 416.211 Art. 2 Abs. 4"


class anspruch_praemienuebernahme_krankenunfallversicherung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf Uebernahme der Praemien der Grundversicherung der Kranken- und Unfallversicherung durch SBFI"
    reference = "SR 416.211 Art. 2"

    def formula(person, period, parameters):
        ist_stipendiat = person('ist_stipendiat_in', period)
        ausserhalb_eu_efta = person('ist_buerger_in_ausserhalb_eu_efta', period)
        ist_familienmitglied = person('ist_begleitendes_familienmitglied', period)
        return ist_stipendiat * ausserhalb_eu_efta * not_(ist_familienmitglied)
