"""SR 836.1 Art. 2

Generated from: ch/836/de/836.1.md

Art. 2: Arten der Zulagen; Ansätze.
Abs. 1: Familienzulagen umfassen Haushaltungszulage sowie Kinder-/Ausbildungszulagen.
Abs. 2: Haushaltungszulage beträgt 100 CHF/Monat.
Abs. 3: Kinder-/Ausbildungszulagen nach FamZG Art. 5; im Berggebiet +20 CHF.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class betrieb_im_berggebiet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Landwirtschaftlicher Betrieb befindet sich im Berggebiet"
    reference = "SR 836.1 Art. 2 Abs. 3"


class haushaltungszulage_landwirtschaft(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Haushaltungszulage für landwirtschaftliche Arbeitnehmer (Art. 2 Abs. 2 FLG)"
    reference = "SR 836.1 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        # Abs. 2: 100 CHF pro Monat
        return 100.0


class kinderzulage_landwirtschaft(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = (
        "Kinderzulage für landwirtschaftliche Arbeitnehmer: Mindestansatz "
        "nach FamZG Art. 5, im Berggebiet +20 CHF (Art. 2 Abs. 3 FLG)"
    )
    reference = "SR 836.1 Art. 2 Abs. 3"

    def formula(person, period, parameters):
        # Mindestansatz FamZG Art. 5 Abs. 1: 215 CHF (Stand 2025)
        mindestansatz = 215.0
        berggebiet = person('betrieb_im_berggebiet', period)
        zuschlag = berggebiet * 20.0
        return mindestansatz + zuschlag


class ausbildungszulage_landwirtschaft(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = (
        "Ausbildungszulage für landwirtschaftliche Arbeitnehmer: Mindestansatz "
        "nach FamZG Art. 5, im Berggebiet +20 CHF (Art. 2 Abs. 3 FLG)"
    )
    reference = "SR 836.1 Art. 2 Abs. 3"

    def formula(person, period, parameters):
        # Mindestansatz FamZG Art. 5 Abs. 2: 268 CHF (Stand 2025)
        mindestansatz = 268.0
        berggebiet = person('betrieb_im_berggebiet', period)
        zuschlag = berggebiet * 20.0
        return mindestansatz + zuschlag
