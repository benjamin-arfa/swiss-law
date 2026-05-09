"""SR 210 Art. 16

Generated from: ch/de/210.md

Urteilsfaehigkeit: Urteilsfaehig ist jede Person, der nicht wegen ihres
Kindesalters, infolge geistiger Behinderung, psychischer Stoerung, Rausch
oder aehnlicher Zustaende die Faehigkeit mangelt, vernunftgemaess zu handeln.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_urteilsfaehig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person urteilsfaehig ist (Art. 16 ZGB)"
    reference = "SR 210 Art. 16"
    default_value = True

    def formula(person, period, parameters):
        # Urteilsunfaehigkeit kann durch verschiedene Gruende eintreten:
        hat_kindesalter_einschraenkung = person('hat_kindesalter_einschraenkung', period)
        hat_geistige_behinderung = person('hat_geistige_behinderung', period)
        hat_psychische_stoerung = person('hat_psychische_stoerung', period)
        ist_berauscht = person('ist_berauscht', period)

        # Urteilsfaehig, wenn keiner der Ausschlussgruende vorliegt
        return not_(
            hat_kindesalter_einschraenkung
            + hat_geistige_behinderung
            + hat_psychische_stoerung
            + ist_berauscht
            > 0
        )


class hat_kindesalter_einschraenkung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einschraenkung der Urteilsfaehigkeit wegen Kindesalter"
    reference = "SR 210 Art. 16"


class hat_geistige_behinderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einschraenkung der Urteilsfaehigkeit wegen geistiger Behinderung"
    reference = "SR 210 Art. 16"


class hat_psychische_stoerung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einschraenkung der Urteilsfaehigkeit wegen psychischer Stoerung"
    reference = "SR 210 Art. 16"


class ist_berauscht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einschraenkung der Urteilsfaehigkeit wegen Rausch oder aehnlicher Zustaende"
    reference = "SR 210 Art. 16"
