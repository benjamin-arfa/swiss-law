"""SR 614.0 Art. 17

Generated from: ch/614/de/614.0.md

Art. 17: Verfahren - Regelung des Verfahrens bei Mängeln, die die EFK
bei Kantonen feststellt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class efk_mangel_bei_kanton_festgestellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK stellt bei Prüfung nach Art. 16 Abs. 1 bei Kantonen "
        "Mängel fest (Art. 17 Abs. 1)"
    )
    reference = "SR 614.0 Art. 17 Abs. 1"


class efk_wendet_sich_an_dienststelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Bei Mängeln gemäss Art. 16 Abs. 1 gelangt EFK an die zuständige "
        "Dienststelle des Bundes; diese behandelt die Sache abschliessend "
        "mit den kantonalen Organen (Art. 17 Abs. 1)"
    )
    reference = "SR 614.0 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        mangel = person('efk_mangel_bei_kanton_festgestellt', period)
        return ist_efk * mangel


class efk_informiert_kantonsregierung_bei_mangel(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Bei Mängeln gemäss Art. 16 Abs. 2 informiert EFK gleichzeitig "
        "die Kantonsregierung und die zuständige Dienststelle des "
        "Bundes (Art. 17 Abs. 2)"
    )
    reference = "SR 614.0 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        mangel = person('efk_mangel_bei_kanton_festgestellt', period)
        return ist_efk * mangel
