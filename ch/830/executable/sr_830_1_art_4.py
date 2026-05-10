"""SR 830.1 Art. 4

Generated from: ch/830/de/830.1.md

Art. 4: Unfall - Definition of accident in social insurance law.
A sudden, unintended, harmful effect of an unusual external factor on the
human body causing health impairment or death.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einwirkung_ist_ploetzlich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Einwirkung ist plötzlich"
    reference = "SR 830.1 Art. 4"


class einwirkung_ist_nicht_beabsichtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Einwirkung ist nicht beabsichtigt"
    reference = "SR 830.1 Art. 4"


class einwirkung_ist_schaedigend(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Einwirkung ist schädigend"
    reference = "SR 830.1 Art. 4"


class einwirkung_ungewoehnlicher_aeusserer_faktor(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Einwirkung eines ungewöhnlichen äusseren Faktors auf den menschlichen Körper"
    reference = "SR 830.1 Art. 4"


class einwirkung_hat_gesundheitsbeeintraechtigung_oder_tod(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Einwirkung hat eine Beeinträchtigung der körperlichen, geistigen oder "
        "psychischen Gesundheit oder den Tod zur Folge"
    )
    reference = "SR 830.1 Art. 4"


class ist_unfall(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Vorliegen eines Unfalls im Sinne von Art. 4 ATSG: plötzliche, nicht "
        "beabsichtigte schädigende Einwirkung eines ungewöhnlichen äusseren Faktors"
    )
    reference = "SR 830.1 Art. 4"

    def formula(person, period, parameters):
        ploetzlich = person('einwirkung_ist_ploetzlich', period)
        nicht_beabsichtigt = person('einwirkung_ist_nicht_beabsichtigt', period)
        schaedigend = person('einwirkung_ist_schaedigend', period)
        aeusserer_faktor = person('einwirkung_ungewoehnlicher_aeusserer_faktor', period)
        folge = person('einwirkung_hat_gesundheitsbeeintraechtigung_oder_tod', period)
        return ploetzlich * nicht_beabsichtigt * schaedigend * aeusserer_faktor * folge
