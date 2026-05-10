"""SR 451.31 Art. 6

Generated from: ch/451/de/451.31.md
Auenverordnung - Frist fuer Schutzmassnahmen: 10 Jahre nach Aufnahme.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufnahme_aueninventar_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der Aufnahme des Objekts in das Aueninventar"
    reference = "SR 451.31 Art. 6"


class frist_schutzmassnahmen_auen_abgelaufen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Frist fuer Schutzmassnahmen (10 Jahre) ist abgelaufen"
    reference = "SR 451.31 Art. 6"

    def formula(person, period, parameters):
        aufnahme = person('aufnahme_aueninventar_jahr', period)
        aktuelles_jahr = period.start.year
        return (aktuelles_jahr - aufnahme) > 10
