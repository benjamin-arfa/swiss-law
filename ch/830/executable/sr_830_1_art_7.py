"""SR 830.1 Art. 7

Generated from: ch/830/de/830.1.md

Art. 7: Erwerbsunfähigkeit - Full or partial loss of earning capacity on the
balanced labor market, caused by health impairment and remaining after
reasonable treatment and integration.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class grad_erwerbsunfaehigkeit(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = (
        "Grad der Erwerbsunfähigkeit (0.0 bis 1.0): durch Gesundheitsbeeinträchtigung "
        "verursachter und nach zumutbarer Behandlung und Eingliederung verbleibender "
        "Verlust der Erwerbsmöglichkeiten (Art. 7 Abs. 1 ATSG)"
    )
    reference = "SR 830.1 Art. 7 Abs. 1"


class erwerbsunfaehigkeit_objektiv_nicht_ueberwindbar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Erwerbsunfähigkeit ist aus objektiver Sicht nicht überwindbar "
        "(Art. 7 Abs. 2 ATSG)"
    )
    reference = "SR 830.1 Art. 7 Abs. 2"


class ist_erwerbsunfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist erwerbsunfähig im Sinne von Art. 7 ATSG"
    reference = "SR 830.1 Art. 7"

    def formula(person, period, parameters):
        # Abs. 1: Verlust der Erwerbsmöglichkeiten vorhanden
        # Abs. 2: nur wenn aus objektiver Sicht nicht überwindbar
        grad = person('grad_erwerbsunfaehigkeit', period)
        nicht_ueberwindbar = person('erwerbsunfaehigkeit_objektiv_nicht_ueberwindbar', period)
        return (grad > 0) * nicht_ueberwindbar
