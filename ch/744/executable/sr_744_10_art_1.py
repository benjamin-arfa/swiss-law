"""SR 744.10 Art. 1

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class strassentransportunternehmen_zulassung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unterliegt der Zulassungspflicht als Strassentransportunternehmen im Personen- oder Güterverkehr"
    reference = "SR 744.10 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        personenverkehr = person('strassentransportunternehmen_personenverkehr', period)
        gueterverkehr = person('strassentransportunternehmen_gueterverkehr', period)
        return personenverkehr + gueterverkehr


class strassentransportunternehmen_personenverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tätigkeit als Strassentransportunternehmen im Personenverkehr"
    reference = "SR 744.10 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_strassentransportunternehmen', period) * person('taetig_im_personenverkehr', period)


class strassentransportunternehmen_gueterverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tätigkeit als Strassentransportunternehmen im Güterverkehr"
    reference = "SR 744.10 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return person('ist_strassentransportunternehmen', period) * person('taetig_im_gueterverkehr', period)


class strassentransportunternehmen_beauftragung_gueterverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beauftragung von Strassentransportunternehmen im Güterverkehr gemäss Art. 1 Abs. 1bis"
    reference = "SR 744.10 Art. 1 Abs. 1bis (in Kraft seit 1. Mai 2025)"

    def formula(person, period, parameters):
        return person('ist_auftraggeber_gueterverkehr', period) * person('strassentransportunternehmen_gueterverkehr', period)


class personenbefoerderung_konzessionspflichtig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Regelmässige und gewerbsmässige Personenbeförderung unterliegt Konzessionspflicht nach PBG Art. 6-8 (SR 745.1), nicht diesem Gesetz"
    reference = "SR 744.10 Art. 1 Abs. 2; SR 745.1 Art. 6-8"

    def formula(person, period, parameters):
        regelmaessig = person('personenbefoerderung_regelmaessig', period)
        gewerbsmaessig = person('personenbefoerderung_gewerbsmaessig', period)
        return regelmaessig * gewerbsmaessig


class ist_strassentransportunternehmen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person oder Unternehmen ist ein Strassentransportunternehmen"
    reference = "SR 744.10 Art. 1"


class taetig_im_personenverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tätigkeit im Strassenpersonenverkehr"
    reference = "SR 744.10 Art. 1 Abs. 1"


class taetig_im_gueterverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tätigkeit im Strassengüterverkehr"
    reference = "SR 744.10 Art. 1 Abs. 1"


class ist_auftraggeber_gueterverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person beauftragt Strassentransportunternehmen im Güterverkehr"
    reference = "SR 744.10 Art. 1 Abs. 1bis"


class personenbefoerderung_regelmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Personenbeförderung erfolgt regelmässig"
    reference = "SR 744.10 Art. 1 Abs. 2; SR 745.1 Art. 6-8"


class personenbefoerderung_gewerbsmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Personenbeförderung erfolgt gewerbsmässig"
    reference = "SR 744.10 Art. 1 Abs. 2; SR 745.1 Art. 6-8"
