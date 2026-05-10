"""SR 744.103 Art. 15

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_auslaendisches_verkehrsunternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Unternehmen ist ein ausländisches Unternehmen im Personen- oder Güterverkehr"
    reference = "SR 744.103 Art. 15"

    def formula(person, period, parameters):
        return person('auslaendisches_unternehmen', period)


class verstoss_gegen_schweizerische_verkehrsvorschriften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Unternehmen hat gegen schweizerische Vorschriften über den Personen- oder Güterverkehr verstossen"
    reference = "SR 744.103 Art. 15"

    def formula(person, period, parameters):
        return person('verstoss_verkehrsvorschriften_ch', period)


class verstoss_kann_zu_entzug_der_zulassungsbewilligung_fuehren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Verstoss kann zu einem Entzug der Zulassungsbewilligung führen"
    reference = "SR 744.103 Art. 15"

    def formula(person, period, parameters):
        return person('entzug_zulassungsbewilligung_moeglich', period)


class bav_meldepflicht_an_auslaendische_behoerde(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das BAV ist verpflichtet, den Verstoss der zuständigen ausländischen Behörde zu melden"
    reference = "SR 744.103 Art. 15"

    def formula(person, period, parameters):
        ist_auslaendisch = person('ist_auslaendisches_verkehrsunternehmen', period)
        hat_verstossen = person('verstoss_gegen_schweizerische_verkehrsvorschriften', period)
        fuehrt_zu_entzug = person('verstoss_kann_zu_entzug_der_zulassungsbewilligung_fuehren', period)
        return ist_auslaendisch * hat_verstossen * fuehrt_zu_entzug


class meldung_kann_elektronisch_erfolgen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Meldung des BAV an die ausländische Behörde kann auf elektronischem Weg erfolgen"
    reference = "SR 744.103 Art. 15"

    def formula(person, period, parameters):
        meldepflicht = person('bav_meldepflicht_an_auslaendische_behoerde', period)
        return meldepflicht
