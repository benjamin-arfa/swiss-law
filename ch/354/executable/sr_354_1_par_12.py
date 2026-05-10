"""SR 354.1 § 12

Generated from: ch/354/de/354.1.md
Rules for internal cantonal transports and federal transports.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transport_innerhalb_kanton(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Transport findet ausschliesslich innerhalb eines Kantons statt"
    reference = "SR 354.1 § 12 Abs. 1"


class transport_im_auftrag_des_bundes(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Transport wird im Auftrag des Bundes ausgefuehrt"
    reference = "SR 354.1 § 12 Abs. 2"


class darf_interkantonale_rechnung_stellen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kanton darf Zwischenverpflegungskosten in interkantonale Rechnung einstellen"
    reference = "SR 354.1 § 12 Abs. 1"

    def formula(person, period):
        innerhalb_kanton = person('transport_innerhalb_kanton', period)
        # Innerkantonale Transporte duerfen NICHT in die interkantonale Rechnung
        return not_(innerhalb_kanton)
