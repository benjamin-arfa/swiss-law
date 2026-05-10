"""SR 523.51 Art. 16

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zertifikat_nebenberuflich_erhalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat das Zertifikat fuer nebenberufliches Zivilschutzlehrpersonal erhalten"
    reference = "SR 523.51 Art. 16 Abs. 2"


class berechtigung_titel_nebenberuflich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist berechtigt den Titel 'Nebenberuflicher Zivilschutzinstruktor' zu fuehren"
    reference = "SR 523.51 Art. 16 Abs. 2"

    def formula(person, period, parameters):
        return person('zertifikat_nebenberuflich_erhalten', period)
