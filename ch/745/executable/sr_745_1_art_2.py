"""SR 745.1 Art. 2

Generated from: ch/745/de/745.1.md

Begriffe der Personenbefoerderung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class personenbefoerderung_gegen_entgelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Reisende werden gegen Entgelt befoerdert (Art. 2 Abs. 1 lit. b Ziff. 1)"
    reference = "SR 745.1 Art. 2 Abs. 1 lit. b Ziff. 1"


class personenbefoerderung_kostenlos_geschaeftsvorteil(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Reisende werden kostenlos befoerdert, um geschaeftlichen Vorteil zu erlangen (Art. 2 Abs. 1 lit. b Ziff. 2)"
    reference = "SR 745.1 Art. 2 Abs. 1 lit. b Ziff. 2"


class personenbefoerderung_umfasst_reisegepaeck(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zur Personenbefoerderung gehoert auch der Transport von Reisegepaeck (Art. 2 Abs. 3)"
    reference = "SR 745.1 Art. 2 Abs. 3"
    default_value = True
