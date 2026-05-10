"""SR 131.214 Art. 17

Generated from: ch/131/de/131.214.md

Stimm- und Wahlrecht: Stimmberechtigt sind alle Schweizerinnen und Schweizer,
die das 18. Altersjahr zurückgelegt haben, im Kanton Uri wohnen und nicht
wegen Geisteskrankheit oder Geistesschwäche entmündigt sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_schweizer_buerger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Schweizer Bürgerin oder Bürger ist"
    reference = "SR 131.214 Art. 17 Abs. 1"


class alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der Person in Jahren"


class wohnt_in_kanton_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person im Kanton Uri wohnt"
    reference = "SR 131.214 Art. 17 Abs. 1"


class ist_entmuendigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person wegen Geisteskrankheit oder Geistesschwäche entmündigt ist"
    reference = "SR 131.214 Art. 17 Abs. 1"


class stimmberechtigt_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person im Kanton Uri stimmberechtigt ist"
    reference = "SR 131.214 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        schweizer = person('ist_schweizer_buerger', period)
        alter_person = person('alter', period)
        wohnt_uri = person('wohnt_in_kanton_uri', period)
        entmuendigt = person('ist_entmuendigt', period)
        return schweizer * (alter_person >= 18) * wohnt_uri * np.logical_not(entmuendigt)


class ist_kirchenangehoeriger_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person einer Landeskirche im Kanton Uri angehört"
    reference = "SR 131.214 Art. 17 Abs. 2"


class stimmberechtigt_kirchlich_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in kirchlichen Angelegenheiten stimmberechtigt ist"
    reference = "SR 131.214 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        return person('stimmberechtigt_uri', period) * person('ist_kirchenangehoeriger_uri', period)


class ist_ortsbueger_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Ortsbürger einer Gemeinde im Kanton Uri ist"
    reference = "SR 131.214 Art. 17 Abs. 2"


class stimmberechtigt_ortsbuerger_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person in Angelegenheiten der Ortsbürgergemeinde stimmberechtigt ist"
    reference = "SR 131.214 Art. 17 Abs. 2"

    def formula(person, period, parameters):
        return person('stimmberechtigt_uri', period) * person('ist_ortsbueger_uri', period)


class wahlfaehig_uri(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person im Kanton Uri wahlfähig ist"
    reference = "SR 131.214 Art. 17 Abs. 4"

    def formula(person, period, parameters):
        # Wer stimmberechtigt ist, ist wahlfähig
        return person('stimmberechtigt_uri', period)
