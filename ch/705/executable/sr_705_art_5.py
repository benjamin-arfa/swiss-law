"""SR 705 Art. 5 - Planungspflicht und Zugaenglichkeit der Plaene

Generated from: ch/de/705.md
Cantons must ensure bicycle network plans are created, periodically reviewed,
publicly accessible in electronic form, and binding on authorities.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class kanton_hat_velowegnetzplan(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kanton hat Plaene fuer bestehende und vorgesehene Velowegnetze erstellt"
    reference = "SR 705 Art. 5 Abs. 1"
    default_value = False


class velowegnetzplan_elektronisch_zugaenglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Velowegnetzplaene sind in elektronischer Form oeffentlich zugaenglich"
    reference = "SR 705 Art. 5 Abs. 4"
    default_value = False
