"""SR 291 Art. 5

Generated from: ch/291/de/291.md

Gerichtsstandsvereinbarung: Die Parteien koennen fuer vermoegensrechtliche
Ansprueche aus einem bestimmten Rechtsverhaeltnis einen Gerichtsstand
vereinbaren. Die Vereinbarung kann schriftlich oder in Textform erfolgen.
Das vereinbarte Gericht ist grundsaetzlich ausschliesslich zustaendig.
Die Vereinbarung ist unwirksam, wenn einer Partei ein Gerichtsstand
missbraeuchlich entzogen wird.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermoegensrechtlicher_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein vermoegensrechtlicher Anspruch vorliegt"
    reference = "SR 291 Art. 5 Abs. 1"


class gerichtsstandsvereinbarung_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Gerichtsstandsvereinbarung geschlossen wurde"
    reference = "SR 291 Art. 5 Abs. 1"


class gerichtsstandsvereinbarung_in_schriftform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gerichtsstandsvereinbarung schriftlich oder in Textform vorliegt"
    reference = "SR 291 Art. 5 Abs. 1"


class gerichtsstand_missbraeuchlich_entzogen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob einer Partei ein Gerichtsstand missbraeuchlich entzogen wird"
    reference = "SR 291 Art. 5 Abs. 2"


class gerichtsstandsvereinbarung_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gerichtsstandsvereinbarung gueltig und wirksam ist"
    reference = "SR 291 Art. 5"

    def formula(person, period, parameters):
        vermoegen = person('vermoegensrechtlicher_anspruch', period)
        vereinbarung = person('gerichtsstandsvereinbarung_vorhanden', period)
        schriftform = person('gerichtsstandsvereinbarung_in_schriftform', period)
        nicht_missbraeuchlich = not_(
            person('gerichtsstand_missbraeuchlich_entzogen', period)
        )
        return vermoegen * vereinbarung * schriftform * nicht_missbraeuchlich
