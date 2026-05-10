"""SR 431.02 Art. 3

Generated from: ch/431/de/431.02.md

Begriffe - Aufenthaltsgemeinde: mindestens 3 aufeinanderfolgende Monate oder 3 Monate innerhalb eines Jahres.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufenthalt_aufeinanderfolgende_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl aufeinanderfolgender Monate des Aufenthalts in der Gemeinde"
    reference = "SR 431.02 Art. 3 Bst. c"


class aufenthalt_monate_innerhalb_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Monate des Aufenthalts in der Gemeinde innerhalb eines Jahres"
    reference = "SR 431.02 Art. 3 Bst. c"


class aufenthalt_zweck_lehranstalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aufenthalt zum Zweck des Besuchs einer Lehranstalt oder Schule"
    reference = "SR 431.02 Art. 3 Bst. c"


class aufenthalt_in_anstalt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterbringung in einer Erziehungs-, Versorgungs-, Heil- oder Strafanstalt"
    reference = "SR 431.02 Art. 3 Bst. c"


class absicht_dauernden_verbleibens(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Absicht dauernden Verbleibens in der Gemeinde"
    reference = "SR 431.02 Art. 3 Bst. c"


class ist_aufenthaltsgemeinde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gemeinde gilt als Aufenthaltsgemeinde der Person"
    reference = "SR 431.02 Art. 3 Bst. c"

    def formula(person, period, parameters):
        keine_dauerabsicht = not_(person('absicht_dauernden_verbleibens', period))

        mindestdauer = (
            (person('aufenthalt_aufeinanderfolgende_monate', period) >= 3) +
            (person('aufenthalt_monate_innerhalb_jahr', period) >= 3)
        )

        besonderer_zweck = (
            person('aufenthalt_zweck_lehranstalt', period) +
            person('aufenthalt_in_anstalt', period)
        )

        return keine_dauerabsicht * (mindestdauer + besonderer_zweck)
