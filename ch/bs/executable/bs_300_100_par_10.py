"""BS 300.100 § 10

Generated from: ch/bs/de/300.100.md

§ 10 Beitraege an die Pflege zu Hause durch Angehoerige oder Dritte:
Permanently care-dependent persons with domicile in BS who are cared for
by relatives or third parties are entitled to financial contributions if
significant care and support expenditure is necessary and provided.
Care dependency and service provision are reviewed by the competent department.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bs_dauernd_pflegebeduertig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauernd pflegebeduertig (BS 300.100 § 10 Abs. 1)"
    reference = "BS 300.100 § 10 Abs. 1"


class bs_pflege_durch_angehoerige_oder_dritte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Wird durch Angehoerige oder Dritte gepflegt (BS 300.100 § 10 Abs. 1)"
    reference = "BS 300.100 § 10 Abs. 1"


class bs_bedeutender_pflege_und_betreuungsaufwand(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bedeutender Pflege- und Betreuungsaufwand notwendig und erbracht (BS 300.100 § 10 Abs. 1)"
    reference = "BS 300.100 § 10 Abs. 1"


class bs_beitrag_pflege_zu_hause(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf Beitrag an Pflege zu Hause durch Angehoerige oder Dritte (BS 300.100 § 10)"
    reference = "BS 300.100 § 10 Abs. 1"

    def formula(person, period, parameters):
        wohnsitz = person('bs_wohnsitz_bs', period.this_year)
        dauernd_pflegebeduertig = person('bs_dauernd_pflegebeduertig', period)
        durch_angehoerige = person('bs_pflege_durch_angehoerige_oder_dritte', period)
        bedeutend = person('bs_bedeutender_pflege_und_betreuungsaufwand', period)
        return wohnsitz * dauernd_pflegebeduertig * durch_angehoerige * bedeutend
