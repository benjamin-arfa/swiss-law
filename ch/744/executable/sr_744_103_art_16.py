"""SR 744.103 Art. 16

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class traegt_fahrerbescheinigung_bei_sich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person führt die Fahrerbescheinigung mit sich"
    reference = "SR 744.103 Art. 16 lit. a"

    def formula(person, period, parameters):
        return person('hat_fahrerbescheinigung_dabei', period)


class traegt_kopie_zulassungsbewilligung_bei_sich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person führt eine beglaubigte Kopie der Zulassungsbewilligung mit sich"
    reference = "SR 744.103 Art. 16 lit. b"

    def formula(person, period, parameters):
        return person('hat_kopie_zulassungsbewilligung_dabei', period)


class hat_fahrerbescheinigung_dabei(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Fahrerbescheinigung wird mitgeführt (Eingabevariable)"
    reference = "SR 744.103 Art. 16 lit. a"


class hat_kopie_zulassungsbewilligung_dabei(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Beglaubigte Kopie der Zulassungsbewilligung wird mitgeführt (Eingabevariable)"
    reference = "SR 744.103 Art. 16 lit. b"


class mitfuehrpflicht_verletzt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hat die Mitführpflicht gemäss Art. 16 verletzt (Voraussetzung für Busse)"
    reference = "SR 744.103 Art. 16"

    def formula(person, period, parameters):
        fahrerbescheinigung_fehlt = not_(person('hat_fahrerbescheinigung_dabei', period))
        zulassung_fehlt = not_(person('hat_kopie_zulassungsbewilligung_dabei', period))
        return fahrerbescheinigung_fehlt + zulassung_fehlt


class busse_mitfuehrpflicht_art16(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist strafbar mit Busse wegen Verletzung der Mitführpflicht (Art. 16)"
    reference = "SR 744.103 Art. 16"

    def formula(person, period, parameters):
        verletzung = person('mitfuehrpflicht_verletzt', period)
        vorsatz_oder_fahrlaessigkeit = person('handelt_vorsaetzlich_oder_fahrlaessig_art16', period)
        return verletzung * vorsatz_oder_fahrlaessigkeit


class handelt_vorsaetzlich_oder_fahrlaessig_art16(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person handelt vorsätzlich oder fahrlässig bezüglich Mitführpflicht (Art. 16)"
    reference = "SR 744.103 Art. 16"
