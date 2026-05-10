"""AG 290.100 § 1

Generated from: ch/ag/de/290.100.md

§ 1 Geltungsbereich: This law regulates the practice of the legal
profession in the canton of Aargau.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ag_uebt_anwaltsberuf_aus(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Uebt den Anwaltsberuf im Kanton Aargau aus (AG 290.100 § 1)"
    reference = "AG 290.100 § 1 Abs. 1"


class ag_unterliegt_eg_bgfa(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Unterliegt dem EG BGFA des Kantons Aargau (AG 290.100 § 1)"
    reference = "AG 290.100 § 1 Abs. 1"

    def formula(person, period, parameters):
        return person('ag_uebt_anwaltsberuf_aus', period)
