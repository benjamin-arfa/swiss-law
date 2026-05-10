"""SR 744.103 Art. 10

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fahrerbescheinigung_voraussetzungen_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Strassentransportunternehmen erfüllt Voraussetzungen nach Art. 9 SR 744.103"
    reference = "SR 744.103 Art. 10 Abs. 1 lit. a"

    def formula(person, period, parameters):
        return person('art9_voraussetzungen_erfuellt', period)


class fahrerbescheinigung_unrichtige_angaben(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Unrichtige Angaben zu erheblichen Tatsachen bei Erteilung der Fahrerbescheinigung gemacht"
    reference = "SR 744.103 Art. 10 Abs. 1 lit. b"


class fahrerbescheinigung_entzug(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Fahrerbescheinigung ist zu entziehen (BAV-Pflicht)"
    reference = "SR 744.103 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        voraussetzungen_nicht_mehr_erfuellt = not_(
            person('fahrerbescheinigung_voraussetzungen_erfuellt', period)
        )
        unrichtige_angaben = person('fahrerbescheinigung_unrichtige_angaben', period)
        return voraussetzungen_nicht_mehr_erfuellt + unrichtige_angaben


class verstoss_schwer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Schwerer Verstoss gegen einschlägige Bestimmungen zum Strassentransport"
    reference = "SR 744.103 Art. 10 Abs. 2"


class verstoss_leicht_wiederholt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Wiederholte leichte Verstösse gegen einschlägige Bestimmungen zum Strassentransport"
    reference = "SR 744.103 Art. 10 Abs. 2"


class fahrerbescheinigung_ausstellung_verweigerbar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ausstellung der Fahrerbescheinigung kann verweigert werden (Ermessen BAV)"
    reference = "SR 744.103 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        schwerer_verstoss = person('verstoss_schwer', period)
        leichte_verstoesse_wiederholt = person('verstoss_leicht_wiederholt', period)
        return schwerer_verstoss + leichte_verstoesse_wiederholt


class fahrerbescheinigung_auflagen_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Auflagen für Ausstellung der Fahrerbescheinigung können gemacht werden (Ermessen BAV)"
    reference = "SR 744.103 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        schwerer_verstoss = person('verstoss_schwer', period)
        leichte_verstoesse_wiederholt = person('verstoss_leicht_wiederholt', period)
        return schwerer_verstoss + leichte_verstoesse_wiederholt
