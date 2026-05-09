"""SR 614.0 Art. 4

Generated from: ch/614/de/614.0.md

Art. 4: Ermächtigung zu Aussagen und zur Aktenherausgabe - Zuständig für die
Ermächtigung zu Aussagen und zur Aktenherausgabe in einem gerichtlichen
Verfahren ist der Direktor oder die Direktorin der EFK.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class efk_ermaechtigungszustaendigkeit_aussagen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Zuständig für die Ermächtigung zu Aussagen und zur Aktenherausgabe "
        "in einem gerichtlichen Verfahren ist der Direktor/die Direktorin (Art. 4)"
    )
    reference = "SR 614.0 Art. 4"

    def formula(person, period, parameters):
        return person('ist_efk_direktor', period)


class ist_efk_direktor(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist der Direktor/die Direktorin der EFK"
    reference = "SR 614.0 Art. 4"


class efk_informationspflicht_departement(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Direktor/in informiert fünf Arbeitstage im Voraus den zuständigen "
        "Departementsvorsteher (Art. 4)"
    )
    reference = "SR 614.0 Art. 4"

    def formula(person, period, parameters):
        return person('ist_efk_direktor', period)
