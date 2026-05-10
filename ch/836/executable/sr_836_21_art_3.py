"""SR 836.21 Art. 3 - Adoption allowance (Adoptionszulage)

Art. 3: Entitlement to an adoption allowance exists when the cantonal family
allowance scheme provides for one. The allowance is paid if (a) entitlement
under FamZG exists, (b) the adoption placement authorization is final, and
(c) the child has actually been received by the adoptive parents in Switzerland.
If multiple persons are entitled, the same differentiation rules as for
birth allowances apply (Art. 2 par. 4).

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kanton_sieht_adoptionszulage_vor(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Canton provides for an adoption allowance (Art. 3 par. 1 FamZV)"
    default_value = False


class adoptionsbewilligung_endgueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Adoption placement authorization is final (Art. 3 par. 3 let. b FamZV)"
    default_value = False


class kind_in_schweiz_aufgenommen(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child actually received by adoptive parents in Switzerland (Art. 3 par. 3 let. c FamZV)"
    default_value = False


class anspruch_adoptionszulage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitlement to adoption allowance (Art. 3 FamZV)"

    def formula(person, period, parameters):
        kanton = person("kanton_sieht_adoptionszulage_vor", period)
        famzg = person("anspruch_familienzulagen_famzg", period)
        bewilligung = person("adoptionsbewilligung_endgueltig", period)
        aufnahme = person("kind_in_schweiz_aufgenommen", period)
        return kanton * famzg * bewilligung * aufnahme
