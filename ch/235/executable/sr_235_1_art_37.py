"""SR 235.1 Art. 37

Generated from: ch/235/de/235.1.md

Vollzug durch die Kantone: Subsidiäre Geltung des DSG beim
kantonalen Vollzug von Bundesrecht.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_kantonale_datenschutzvorschriften_vorhanden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kantonale Datenschutzvorschriften mit angemessenem Schutz sind vorhanden"
    reference = "SR 235.1 Art. 37 Abs. 1"


class dsg_kantonaler_vollzug_bundesrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Kantonale Organe vollziehen Bundesrecht"
    reference = "SR 235.1 Art. 37 Abs. 1"


class dsg_bundesgesetz_gilt_fuer_kanton(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "DSG gilt subsidiaer fuer kantonale Organe beim Vollzug von Bundesrecht"
    reference = "SR 235.1 Art. 37"

    def formula(person, period, parameters):
        vollzug = person('dsg_kantonaler_vollzug_bundesrecht', period)
        kantonal = person('dsg_kantonale_datenschutzvorschriften_vorhanden', period)
        return vollzug * not_(kantonal)
