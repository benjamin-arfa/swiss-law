"""SR 281.1 Art. 27

Generated from: ch/281/de/281.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class person_handlungsfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist handlungsfähig"
    reference = "SR 281.1 Art. 27 Abs. 1"


class vertretung_ist_gewerbsmaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vertretung erfolgt gewerbsmässig"
    reference = "SR 281.1 Art. 27 Abs. 1"


class vertretung_im_zwangsvollstreckungsverfahren_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vertretung im Zwangsvollstreckungsverfahren ist zulässig"
    reference = "SR 281.1 Art. 27 Abs. 1"

    def formula(person, period, parameters):
        # Jede handlungsfähige Person ist berechtigt, andere zu vertreten
        return person('person_handlungsfaehig', period)


class vertretungskosten_gegenpartei_ueberbindbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vertretungskosten dürfen der Gegenpartei überbunden werden"
    reference = "SR 281.1 Art. 27 Abs. 2"

    def formula(person, period, parameters):
        # Kosten der Vertretung dürfen nicht der Gegenpartei überbunden werden
        return person.filled_array(False)
