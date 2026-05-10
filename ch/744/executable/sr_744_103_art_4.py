"""SR 744.103 Art. 4

Generated from: ch/744/de/744.103.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class VerkehrsSparte(Enum):
    __order__ = 'KEINE_BESCHRAENKUNG GUETERVERKEHR PERSONENVERKEHR'
    KEINE_BESCHRAENKUNG = 'keine_beschraenkung'
    GUETERVERKEHR = 'gueterverkehr'
    PERSONENVERKEHR = 'personenverkehr'


class fachausweis_artikel_6_7(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fachausweis nach Art. 6 und 7 SR 744.103"
    reference = "SR 744.103 Art. 4 Abs. 1 lit. a"


class eu_fachausweis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "In der EU gültiger Fachausweis"
    reference = "SR 744.103 Art. 4 Abs. 1 lit. b"


class fachausweis_strassentransport_disponent(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eidgenössischer Fachausweis Strassentransport-Disponent/in oder Disponent/in Transport und Logistik"
    reference = "SR 744.103 Art. 4 Abs. 1 lit. c"


class diplom_betriebsleiter_strassentransport(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eidgenössisches Diplom diplomierter Betriebsleiter/in im Strassentransport oder Transport und Logistik"
    reference = "SR 744.103 Art. 4 Abs. 1 lit. d"


class fachausweis_carfuehrer_reiseleiter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eidgenössischer Fachausweis Carführer-Reiseleiter/in"
    reference = "SR 744.103 Art. 4 Abs. 1 lit. e"


class nachweis_fachlicher_eignung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nachweis der fachlichen Eignung nach Art. 4 SR 744.103"
    reference = "SR 744.103 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('fachausweis_artikel_6_7', period)
            | person('eu_fachausweis', period)
            | person('fachausweis_strassentransport_disponent', period)
            | person('diplom_betriebsleiter_strassentransport', period)
            | person('fachausweis_carfuehrer_reiseleiter', period)
        )


class fachausweis_nur_gueterverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorgelegter Fachausweis gilt nur für Güterverkehr"
    reference = "SR 744.103 Art. 4 Abs. 2"


class fachausweis_nur_personenverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vorgelegter Fachausweis gilt nur für Personenverkehr"
    reference = "SR 744.103 Art. 4 Abs. 2"


class zulassung_beschraenkung_sparte(Variable):
    value_type = bool
    possible_values = VerkehrsSparte
    default_value = VerkehrsSparte.KEINE_BESCHRAENKUNG
    entity = Person
    definition_period = YEAR
    label = "Beschränkung der Unternehmenszulassung auf Verkehrssparte (Art. 4 Abs. 2 SR 744.103)"
    reference = "SR 744.103 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        nur_gueter = person('fachausweis_nur_gueterverkehr', period)
        nur_personen = person('fachausweis_nur_personenverkehr', period)
        return select(
            [nur_gueter, nur_personen],
            [VerkehrsSparte.GUETERVERKEHR, VerkehrsSparte.PERSONENVERKEHR],
            default=VerkehrsSparte.KEINE_BESCHRAENKUNG,
        )
