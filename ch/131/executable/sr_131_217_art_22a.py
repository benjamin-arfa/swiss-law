"""SR 131.217 Art. 22a

Generated from: ch/131/de/131.217.md

Klimaschutz: Kanton und Gemeinden setzen sich für die Begrenzung der
Klimaveränderung ein. Sie leisten den erforderlichen Beitrag zur Erreichung
der Klimaziele. Sie setzen finanzielle Anreize zur Erreichung der Klimaziele.
In Kraft seit 1. Juli 2022.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class klimamassnahme_umweltvertraeglich_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Klimaschutzmassnahme umweltverträglich ist"
    reference = "SR 131.217 Art. 22a Abs. 2"


class klimamassnahme_sozialvertraeglich_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Klimaschutzmassnahme sozialverträglich ist"
    reference = "SR 131.217 Art. 22a Abs. 2"


class klimamassnahme_wirtschaftsvertraeglich_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Klimaschutzmassnahme wirtschaftsverträglich ist"
    reference = "SR 131.217 Art. 22a Abs. 2"


class klimamassnahme_zulaessig_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Klimaschutzmassnahme im Kanton Glarus zulässig ist"
    reference = "SR 131.217 Art. 22a Abs. 2"

    def formula(person, period, parameters):
        umwelt = person('klimamassnahme_umweltvertraeglich_gl', period)
        sozial = person('klimamassnahme_sozialvertraeglich_gl', period)
        wirtschaft = person('klimamassnahme_wirtschaftsvertraeglich_gl', period)
        return umwelt * sozial * wirtschaft


class anspruch_klimaschutz_anreiz_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob finanzielle Anreize zur Erreichung der Klimaziele gesetzt werden"
    reference = "SR 131.217 Art. 22a Abs. 3"

    def formula(person, period, parameters):
        return True
