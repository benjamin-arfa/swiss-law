"""SR 836.21 Art. 6 - Siblings and grandchildren; predominant maintenance

Art. 6: The entitled person predominantly maintains the child if:
(a) the child lives in their household AND third-party maintenance payments
    do not exceed the maximum full AHV orphan's pension; OR
(b) the child does NOT live in their household AND the entitled person pays
    at least the maximum full AHV orphan's pension for maintenance.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class ist_geschwister_oder_enkelkind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child is a sibling or grandchild of the entitled person (Art. 6 FamZV)"
    default_value = False


class kind_lebt_im_haushalt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Child lives in the household of the entitled person (Art. 6 let. a FamZV)"
    default_value = False


class unterhaltsbeitrag_dritter(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Third-party maintenance amount paid for the child (Art. 6 let. a FamZV)"
    default_value = 0


class maximale_volle_waisenrente_ahv(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Maximum full AHV orphan's pension (Art. 6 FamZV)"
    default_value = 980


class eigener_unterhaltsbeitrag(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Entitled person's own maintenance payment for a child not in household (Art. 6 let. b FamZV)"
    default_value = 0


class ueberwiegender_unterhalt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Entitled person predominantly maintains the child (Art. 6 FamZV)"

    def formula(person, period, parameters):
        im_haushalt = person("kind_lebt_im_haushalt", period)
        dritter = person("unterhaltsbeitrag_dritter", period)
        max_rente = person("maximale_volle_waisenrente_ahv", period)
        eigener = person("eigener_unterhaltsbeitrag", period)

        # (a) child in household AND third-party payments <= max orphan's pension
        bedingung_a = im_haushalt * (dritter <= max_rente)
        # (b) child NOT in household AND own payments >= max orphan's pension
        bedingung_b = not_(im_haushalt) * (eigener >= max_rente)

        return bedingung_a + bedingung_b
