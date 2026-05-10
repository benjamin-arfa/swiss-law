"""SR 813.1 Art. 5

Generated from: ch/813/de/813.1.md

Selbstkontrolle: Pflicht der Herstellerin, Stoffe/Zubereitungen vor dem
Inverkehrbringen zu beurteilen, einzustufen, zu verpacken und zu kennzeichnen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_herstellerin_chemg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Herstellerin im Sinne des ChemG ist (beruflich/gewerblich herstellt, gewinnt oder einfuehrt)"
    reference = "SR 813.1 Art. 4 Abs. 1 Bst. f"


class bringt_stoffe_in_verkehr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Stoffe oder Zubereitungen in Verkehr bringt"
    reference = "SR 813.1 Art. 5 Abs. 1"


class hat_selbstkontrolle_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Herstellerin die Selbstkontrolle (Beurteilung, Einstufung, Verpackung, Kennzeichnung) durchgefuehrt hat"
    reference = "SR 813.1 Art. 5 Abs. 1"


class selbstkontrolle_pflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person zur Selbstkontrolle verpflichtet ist"
    reference = "SR 813.1 Art. 5"

    def formula(person, period, parameters):
        ist_herstellerin = person('ist_herstellerin_chemg', period)
        in_verkehr = person('bringt_stoffe_in_verkehr', period)
        return ist_herstellerin * in_verkehr
