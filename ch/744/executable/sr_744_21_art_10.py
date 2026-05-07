"""SR 744.21 Art. 10

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class sr_744_21_art_10_bundesrecht_elektrische_anlagen_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "SR 744.21 Art. 10: Auf die Erstellung, den Unterhalt und Betrieb "
        "der elektrischen Anlagen und Einrichtungen der Nationalstrassen finden "
        "die Bestimmungen der Bundesgesetzgebung über elektrische Anlagen Anwendung."
    )
    reference = "https://www.fedlex.admin.ch/eli/cc/1960/1025_1067_1077/de#art_10"

    def formula(person, period, parameters):
        # Art. 10 is a blanket applicability provision: federal legislation on
        # electrical installations always governs construction, maintenance and
        # operation of electrical installations on national roads.
        return True
