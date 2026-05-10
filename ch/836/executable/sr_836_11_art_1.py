"""SR 836.11 Art. 1

Generated from: ch/836/de/836.11.md

Art. 1: Unterstellte Arbeitnehmer.
Abs. 1: Arbeitnehmer in landwirtschaftlichen und nichtlandwirtschaftlichen
Betrieben desselben Arbeitgebers gelten nur dann als landwirtschaftliche
Arbeitnehmer, wenn sie vorwiegend landwirtschaftliche Arbeiten verrichten.
Abs. 2: Der Ehegatte des Eigentuemers/Miteigentuemers/Gesamteigentuemers
gilt nicht als landwirtschaftlicher Arbeitnehmer.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verrichtet_vorwiegend_landw_arbeiten(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person verrichtet vorwiegend landwirtschaftliche Arbeiten"
    reference = "SR 836.11 Art. 1 Abs. 1"


class arbeitgeber_hat_gemischten_betrieb(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitgeber hat landwirtschaftliche und nichtlandwirtschaftliche Betriebe"
    reference = "SR 836.11 Art. 1 Abs. 1"


class ist_ehegatte_betriebseigentuemer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist Ehegatte des Eigentuemers/Miteigentuemers des landwirtschaftlichen Betriebes"
    reference = "SR 836.11 Art. 1 Abs. 2"


class gilt_als_landwirtschaftlicher_arbeitnehmer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person gilt als landwirtschaftlicher Arbeitnehmer im Sinne der FLV (Art. 1)"
    reference = "SR 836.11 Art. 1"

    def formula(person, period, parameters):
        gemischt = person('arbeitgeber_hat_gemischten_betrieb', period)
        vorwiegend_landw = person('verrichtet_vorwiegend_landw_arbeiten', period)
        ehegatte = person('ist_ehegatte_betriebseigentuemer', period)

        # Abs. 1: Bei gemischtem Betrieb nur wenn vorwiegend landwirtschaftlich
        # Bei reinem Landwirtschaftsbetrieb immer
        ist_landw_an = person('ist_landwirtschaftlicher_arbeitnehmer', period)
        bei_gemischt = where(gemischt, vorwiegend_landw, ist_landw_an)

        # Abs. 2: Ehegatte gilt nicht als landw. Arbeitnehmer
        return bei_gemischt * (1 - ehegatte)
