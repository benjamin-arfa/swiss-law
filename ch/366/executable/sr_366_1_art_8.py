"""SR 366.1 Art. 8

Generated from: ch/366/de/366.1.md

Zusammenarbeit mit Privaten: Bedingungen fuer Orientierung/Informationseinholung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class drohende_gefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Drohende Gefahr zur Abwendung der das NZB juristische Personen orientiert"
    reference = "SR 366.1 Art. 8 Abs. 1 Bst. a"


class mitteilung_im_interesse_betroffener(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Mitteilung erfolgt im Interesse der betroffenen Person mit deren Zustimmung"
    reference = "SR 366.1 Art. 8 Abs. 1 Bst. b"


class nzb_orientierung_private_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "NZB darf juristische Personen zur Verhinderung/Aufklaerung von Straftaten orientieren"
    reference = "SR 366.1 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        gefahr = person('drohende_gefahr', period)
        interesse = person('mitteilung_im_interesse_betroffener', period)
        return gefahr + interesse
