"""SR 614.0 Art. 3

Generated from: ch/614/de/614.0.md

Art. 3: Beizug von Sachverständigen - Die EFK kann Sachverständige beiziehen,
soweit die Durchführung ihrer Aufgabe besondere Fachkenntnisse erfordert oder
mit ihrem ordentlichen Personalbestand nicht gewährleistet werden kann.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class efk_kann_sachverstaendige_beiziehen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "EFK kann Sachverständige beiziehen, soweit besondere Fachkenntnisse "
        "erforderlich oder ordentlicher Personalbestand nicht ausreicht (Art. 3)"
    )
    reference = "SR 614.0 Art. 3"

    def formula(person, period, parameters):
        ist_efk = person('ist_eidgenoessische_finanzkontrolle', period)
        besondere_fachkenntnisse = person('aufgabe_erfordert_besondere_fachkenntnisse', period)
        personal_nicht_ausreichend = person('personalbestand_nicht_ausreichend', period)
        return ist_efk * (besondere_fachkenntnisse + personal_nicht_ausreichend)


class aufgabe_erfordert_besondere_fachkenntnisse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Durchführung der Aufgabe erfordert besondere Fachkenntnisse"
    reference = "SR 614.0 Art. 3"


class personalbestand_nicht_ausreichend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ordentlicher Personalbestand der EFK reicht für die Aufgabe nicht aus"
    reference = "SR 614.0 Art. 3"
