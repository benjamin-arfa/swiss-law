"""SR 351.6 Art. 57

Generated from: ch/351/de/351.6.md
Cost rules for execution of ICC sentences.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transportkosten_icc_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Transportkosten und Kosten nach Art. 100 Abs. 1 lit. c-e Statut in CHF"
    reference = "SR 351.6 Art. 57 Abs. 1"


class uebrige_vollzugskosten_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Uebrige Kosten des Strafvollzugs in CHF"
    reference = "SR 351.6 Art. 57 Abs. 2"


class gerichtshof_traegt_kosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten die der Gerichtshof traegt in CHF"
    reference = "SR 351.6 Art. 57 Abs. 1"

    def formula(person, period):
        return person('transportkosten_icc_chf', period)


class bund_traegt_vollzugskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten die der Bund fuer den Strafvollzug traegt in CHF"
    reference = "SR 351.6 Art. 57 Abs. 2"

    def formula(person, period):
        return person('uebrige_vollzugskosten_chf', period)
