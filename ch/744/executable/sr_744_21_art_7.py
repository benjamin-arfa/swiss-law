"""SR 744.21 Art. 7

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bav_aufsicht_ueber_unternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das BAV übt die Aufsicht über das Unternehmen aus (SR 744.21 Art. 7 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1999/17/de#art_7"

    def formula(person, period, parameters):
        # The Federal Office of Transport (BAV) exercises supervision
        # over all companies subject to SR 744.21 by operation of law.
        # This is a statutory supervisory relationship — always true for
        # covered undertakings; modelled as unconditionally applicable.
        return True


class mitarbeit_motorfahrzeugverkehr_behoerden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das BAV zieht die für den Motorfahrzeugverkehr zuständigen Behörden zur Mitarbeit heran (SR 744.21 Art. 7 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1999/17/de#art_7"

    def formula(person, period, parameters):
        # Authorities responsible for motor vehicle traffic are involved
        # in the supervision by the BAV. Unconditionally applicable
        # wherever BAV supervision applies.
        bav_aufsicht = person('bav_aufsicht_ueber_unternehmen', period)
        return bav_aufsicht


class bundesrat_regelt_zusammenarbeit_behoerden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bundesrat regelt die Zusammenarbeit der beteiligten Behörden (SR 744.21 Art. 7 Abs. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1999/17/de#art_7"

    def formula(person, period, parameters):
        # The Federal Council regulates inter-authority cooperation.
        # This is a constitutional/legislative delegation — applicable
        # wherever the supervisory regime of Art. 7 applies.
        bav_aufsicht = person('bav_aufsicht_ueber_unternehmen', period)
        return bav_aufsicht
