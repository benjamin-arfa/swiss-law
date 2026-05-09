"""SR 831.30 Art. 15

Generated from: ch/831/de/831.30.md

Art. 15: Frist fuer die Geltendmachung von Krankheits- und
Behinderungskosten - Deadline for claiming health and disability costs.

Reimbursement is granted if:
a. the claim is submitted within 15 months of invoicing, AND
b. the costs arose during a period in which the applicant met the
   conditions of Art. 4-6.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_rechnungsdatum_krankheitskosten(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Rechnungsdatum der Krankheits-/Behinderungskosten (YYYY-MM-DD)"
    reference = "SR 831.30 Art. 15 Bst. a"


class el_antragsdatum_verguetung(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Datum der Geltendmachung der Verguetung (YYYY-MM-DD)"
    reference = "SR 831.30 Art. 15 Bst. a"


class el_verguetungsantrag_fristgerecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Verguetungsantrag innert 15 Monaten nach Rechnungstellung eingereicht (Art. 15 Bst. a ELG)"
    reference = "SR 831.30 Art. 15 Bst. a"


class el_kosten_waehrend_anspruchsperiode(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Kosten sind waehrend der EL-Anspruchsperiode entstanden (Art. 15 Bst. b ELG)"
    reference = "SR 831.30 Art. 15 Bst. b"


class el_krankheitskosten_verguetbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Krankheits-/Behinderungskosten sind verguetbar (Art. 15 ELG)"
    reference = "SR 831.30 Art. 15"

    def formula(person, period, parameters):
        fristgerecht = person('el_verguetungsantrag_fristgerecht', period)
        waehrend_anspruch = person('el_kosten_waehrend_anspruchsperiode', period)
        return fristgerecht * waehrend_anspruch
