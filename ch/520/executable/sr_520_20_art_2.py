"""SR 520.20 Art. 2

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class berechtigt_zur_requisition(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist berechtigt, Schutzanlagen und Liegestellen zu requirieren"
    reference = "SR 520.20 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        ist_babs = person('ist_babs_mit_antrag_sem', period)
        ist_kantonale_stelle = person('ist_kantonale_zivilschutzstelle', period)
        return ist_babs + ist_kantonale_stelle


class ist_babs_mit_antrag_sem(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist das BABS auf Antrag des SEM"
    reference = "SR 520.20 Art. 2 Abs. 1 lit. a"


class ist_kantonale_zivilschutzstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist die fuer den Zivilschutz zustaendige Stelle des Kantons"
    reference = "SR 520.20 Art. 2 Abs. 1 lit. b"


class geschuetztes_spital_eignung_geprueft(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Bei geschuetzten Spitaelern ist die Eignung im Einzelfall geprueft"
    reference = "SR 520.20 Art. 2 Abs. 2"
