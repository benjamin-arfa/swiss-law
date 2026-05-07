"""SR 611.01 Art. 1

Generated from: ch/611/de/611.01.md

Finanzhaushaltverordnung (FHV) - Art. 1: Geltungsbereich. Bestimmungen
gelten sinngemäss für Bundesversammlung, eidgenössische Gerichte,
Bundesanwaltschaft, EDÖB etc.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_bundesversammlung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Bundesversammlung (Art. 1 Abs. 1 lit. a)"
    reference = "SR 611.01 Art. 1 Abs. 1 lit. a"


class ist_eidgenoessisches_gericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein eidgenössisches Gericht (Art. 1 Abs. 1 lit. b)"
    reference = "SR 611.01 Art. 1 Abs. 1 lit. b"


class ist_bundesanwaltschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Bundesanwaltschaft (Art. 1 Abs. 1 lit. d)"
    reference = "SR 611.01 Art. 1 Abs. 1 lit. d"


class ist_edoeb(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist der EDÖB (Art. 1 Abs. 1 lit. g)"
    reference = "SR 611.01 Art. 1 Abs. 1 lit. g"


class fhv_gilt_sinngemaess(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "FHV-Bestimmungen über Verwaltungseinheiten gelten sinngemäss "
        "(Art. 1 Abs. 1)"
    )
    reference = "SR 611.01 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        bv = person('ist_bundesversammlung', period)
        gericht = person('ist_eidgenoessisches_gericht', period)
        ba = person('ist_bundesanwaltschaft', period)
        edoeb = person('ist_edoeb', period)
        return bv + gericht + ba + edoeb
