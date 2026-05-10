"""SR 672.933.21 Art. 8 — Vereinfachte Ausführung

Art. 8: Stimmt die betroffene Person der Aushändigung zu (unwiderruflich),
schliesst die ESTV das Verfahren durch Übermittlung ab.
Bei Teilzustimmung werden restliche Informationen nach Art. 5-7 beschafft.

Generated from: ch/672/de/672.933.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class betroffene_stimmt_aushaendigung_zu(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Betroffene Person stimmt Aushändigung der Informationen an Spanien zu (SR 672.933.21 Art. 8 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_8"
    default_value = False


class zustimmung_unwiderruflich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Zustimmung zur Aushändigung ist unwiderruflich (SR 672.933.21 Art. 8 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_8"

    def formula(person, period, parameters):
        return person('betroffene_stimmt_aushaendigung_zu', period)


class vereinfachte_ausfuehrung_abschluss(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Verfahren wird vereinfacht durch Übermittlung abgeschlossen (SR 672.933.21 Art. 8 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2007/302/de#art_8"

    def formula(person, period, parameters):
        # Art. 8 Abs. 2: ESTV hält Zustimmung fest und schliesst Verfahren ab.
        return person('betroffene_stimmt_aushaendigung_zu', period)
