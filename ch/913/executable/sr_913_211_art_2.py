"""SR 913.211 Art. 2

Generated from: ch/913/de/913.211.md

Kriterien für die Abgrenzung von gefährdeten Gebieten:
- Bewirtschaftung gefährdet wenn: keine/geringe Nachfrage nach Pachtland,
  Zunahme des Brachlandes, Zunahme der Verbuschung/Waldfläche
- Besiedelungsdichte gefährdet wenn Einwohnerzahl für soziales Gefüge
  längerfristig nicht sichergestellt
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class liegt_im_berg_oder_huegelgebiet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Betrieb im Berg- und Hügelgebiet liegt"
    reference = "SR 913.211 Art. 2 Abs. 1"


class keine_nachfrage_pachtland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Keine oder kleine Nachfrage nach Pachtland mit tiefen Pachtzinsen"
    reference = "SR 913.211 Art. 2 Abs. 1 Bst. a"


class zunahme_brachland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Zunahme des Brachlandes festgestellt wird"
    reference = "SR 913.211 Art. 2 Abs. 1 Bst. b"


class zunahme_verbuschung_wald(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Zunahme der Verbuschung und Waldfläche festgestellt wird"
    reference = "SR 913.211 Art. 2 Abs. 1 Bst. c"


class bewirtschaftung_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bewirtschaftung im Gebiet gefährdet ist"
    reference = "SR 913.211 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        berg_huegel = person('liegt_im_berg_oder_huegelgebiet', period)
        return berg_huegel * (
            person('keine_nachfrage_pachtland', period) +
            person('zunahme_brachland', period) +
            person('zunahme_verbuschung_wald', period)
        )


class besiedelungsdichte_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die genügende Besiedelungsdichte gefährdet ist"
    reference = "SR 913.211 Art. 2 Abs. 2"
