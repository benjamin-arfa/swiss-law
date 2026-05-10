"""SR 131.214 Art. 20

Generated from: ch/131/de/131.214.md

Ausübung des Stimmrechts: Die Teilnahme an den Abstimmungen und Wahlen und an den
Gemeindeversammlungen ist Bürgerpflicht.
Establishes civic duty to participate in democratic processes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class teilnahme_abstimmung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person an Abstimmungen teilgenommen hat"
    reference = "SR 131.214 Art. 20"


class teilnahme_wahlen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person an Wahlen teilgenommen hat"
    reference = "SR 131.214 Art. 20"


class teilnahme_gemeindeversammlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person an Gemeindeversammlungen teilgenommen hat"
    reference = "SR 131.214 Art. 20"


class buergerpflicht_demokratische_teilnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bürgerpflicht zur Teilnahme an demokratischen Prozessen"
    reference = "SR 131.214 Art. 20"

    def formula(person, period, parameters):
        import numpy as np

        # Civic duty applies to all citizens eligible to vote
        stimmberechtigt = person('stimmberechtigt_uri', period)

        return np.where(
            stimmberechtigt,
            parameters(period).buergerpflichten_uri.demokratische_teilnahme,
            False
        )


class erfuellung_buergerpflicht_teilnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Erfüllung der Bürgerpflicht zur demokratischen Teilnahme"
    reference = "SR 131.214 Art. 20"

    def formula(person, period, parameters):
        import numpy as np

        # Check if civic duty exists
        buergerpflicht = person('buergerpflicht_demokratische_teilnahme', period)

        # Check participation in democratic processes
        teilnahme_abstimmung = person('teilnahme_abstimmung', period)
        teilnahme_wahlen = person('teilnahme_wahlen', period)
        teilnahme_gemeindeversammlung = person('teilnahme_gemeindeversammlung', period)

        # Civic duty is fulfilled if person participated in any democratic process
        # (Constitution requires participation, but doesn't specify frequency)
        teilnahme_irgendwo = teilnahme_abstimmung + teilnahme_wahlen + teilnahme_gemeindeversammlung

        return np.where(
            buergerpflicht,
            teilnahme_irgendwo,
            True  # No duty means it's automatically fulfilled
        )


class verletzung_buergerpflicht_teilnahme(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verletzung der Bürgerpflicht zur demokratischen Teilnahme"
    reference = "SR 131.214 Art. 20"

    def formula(person, period, parameters):
        import numpy as np

        buergerpflicht = person('buergerpflicht_demokratische_teilnahme', period)
        erfuellung = person('erfuellung_buergerpflicht_teilnahme', period)

        return buergerpflicht * np.logical_not(erfuellung)