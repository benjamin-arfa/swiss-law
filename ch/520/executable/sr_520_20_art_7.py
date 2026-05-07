"""SR 520.20 Art. 7

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class kanton_traegt_anpassungskosten(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Der Kanton oder die Gemeinde traegt die Kosten fuer die Anpassung der Infrastruktur bei mangelnder Ausruestung oder mangelndem Unterhalt"
    reference = "SR 520.20 Art. 7 Abs. 1"


class infrastruktur_ergaenzung_entschaedigung_oder_rueckbau(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Nach Beendigung der Requisition wird entschieden ob Entschaedigung oder Rueckbau der Ergaenzungen"
    reference = "SR 520.20 Art. 7 Abs. 2"
