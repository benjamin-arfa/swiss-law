"""SR 321.0 Art. 3

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_dienstpflichtiger_im_militaerdienst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist Dienstpflichtiger waehrend des Militaerdienstes"
    reference = "SR 321.0 Art. 3 Abs. 1 Ziff. 1"


class ist_beamter_militaerverwaltung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist Beamter/Angestellter/Arbeiter der Militaerverwaltung"
    reference = "SR 321.0 Art. 3 Abs. 1 Ziff. 2"


class ist_dienstpflichtiger_in_uniform_ausser_dienst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist Dienstpflichtiger ausserhalb des Dienstes in Uniform"
    reference = "SR 321.0 Art. 3 Abs. 1 Ziff. 3"


class ist_berufs_oder_zeitmilitaer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist Berufs- oder Zeitmilitaer oder leistet Friedensfoerderungsdienst"
    reference = "SR 321.0 Art. 3 Abs. 1 Ziff. 6"


class untersteht_militaerstrafrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person untersteht dem Militaerstrafrecht (persoenlicher Geltungsbereich)"
    reference = "SR 321.0 Art. 3"

    def formula(person, period, parameters):
        dienst = person('ist_dienstpflichtiger_im_militaerdienst', period)
        beamter = person('ist_beamter_militaerverwaltung', period)
        uniform = person('ist_dienstpflichtiger_in_uniform_ausser_dienst', period)
        beruf = person('ist_berufs_oder_zeitmilitaer', period)
        return dienst + beamter + uniform + beruf > 0
