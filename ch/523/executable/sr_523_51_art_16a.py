"""SR 523.51 Art. 16a

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class zertifikat_fuehrungsorgane_erhalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat das Zertifikat fuer Lehrpersonal Fuehrungsorgane erhalten"
    reference = "SR 523.51 Art. 16a Abs. 2"


class berechtigung_titel_instruktor_fuehrungsorgane(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist berechtigt den Titel 'Instruktor Fuehrungsorgane' zu fuehren"
    reference = "SR 523.51 Art. 16a Abs. 2"

    def formula(person, period, parameters):
        return person('zertifikat_fuehrungsorgane_erhalten', period)
