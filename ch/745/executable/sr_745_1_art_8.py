"""SR 745.1 Art. 8

Generated from: ch/745/de/745.1.md

Grenzueberschreitender Personenverkehr.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_grenzueberschreitender_personenverkehr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Personenbefoerderung befaehrt ausschliesslich grenzueberschreitenden Verkehr"
    reference = "SR 745.1 Art. 8 Abs. 1"


class grenzueberschreitende_bewilligung_maximale_dauer_jahre(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer der Bewilligung fuer grenzueberschreitenden Personenverkehr in Jahren"
    reference = "SR 745.1 Art. 8 Abs. 4"
    default_value = 5.0


class grenzueberschreitende_bewilligung_uebertragbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bewilligung fuer grenzueberschreitenden Verkehr ist nicht uebertragbar"
    reference = "SR 745.1 Art. 8 Abs. 4"
    default_value = False
