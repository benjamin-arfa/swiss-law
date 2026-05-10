"""SR 0.121 Art. IV

Generated from: ch/0/de/0.121.md

Territorial sovereignty: The Treaty does not constitute a renunciation
of previously asserted territorial claims. No new claims or enlargements
of existing claims shall be asserted while the Treaty is in force.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class antarktis_gebietshoheit_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein vorher geltend gemachter Anspruch auf Gebietshoheit in der Antarktis besteht"
    reference = "SR 0.121 Art. IV Abs. 1"


class antarktis_neue_ansprueche_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob neue Ansprueche auf Gebietshoheit in der Antarktis waehrend Vertragsgeltung verboten sind"
    reference = "SR 0.121 Art. IV Abs. 2"

    def formula(person, period, parameters):
        return 1
