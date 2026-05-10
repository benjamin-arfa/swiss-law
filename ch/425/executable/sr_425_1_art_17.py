"""SR 425.1 Art. 17

Generated from: ch/425/de/425.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_gericht_oder_kantonale_behoerde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist ein Gericht oder eine kantonale Behoerde"
    reference = "SR 425.1 Art. 17 Abs. 2"


class ist_internationale_organisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist eine internationale Organisation"
    reference = "SR 425.1 Art. 17 Abs. 3"


class rechtsgutachten_im_oeffentlichen_interesse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Rechtsgutachten ist im oeffentlichen Interesse"
    reference = "SR 425.1 Art. 17 Abs. 3"


class gebuehr_ermaessigung_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gebuehren-Ermaessigung ist anwendbar"
    reference = "SR 425.1 Art. 17 Abs. 2-3"

    def formula(person, period, parameters):
        gericht_kantonal = person('ist_gericht_oder_kantonale_behoerde', period)
        international_org = person('ist_internationale_organisation', period)
        oeffentliches_interesse = person('rechtsgutachten_im_oeffentlichen_interesse', period)
        return gericht_kantonal + (international_org * oeffentliches_interesse)
