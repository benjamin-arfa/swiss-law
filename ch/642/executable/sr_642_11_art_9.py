"""SR 642.11 Art. 9

Generated from: ch/642/de/642.11.md

Art. 9 Ehegatten; eingetragene Partnerinnen oder Partner; Kinder unter
elterlicher Sorge:
1. Income of spouses living in legally and factually undissolved marriage
   is combined regardless of matrimonial property regime.
1bis. Income of registered partners living together is combined. The status
   of registered partners corresponds to that of spouses throughout the law.
2. Income of children under parental authority is attributed to the holder
   of parental authority; income from gainful employment is taxed
   independently for the child.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_verheiratet_zusammenlebend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ehegatten leben in rechtlich und tatsaechlich ungetrennter Ehe"
    reference = "SR 642.11 Art. 9 Abs. 1"


class ist_eingetragene_partnerschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person lebt in rechtlich und tatsaechlich ungetrennter eingetragener Partnerschaft"
    reference = "SR 642.11 Art. 9 Abs. 1bis"


class einkommen_ehegatte(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eigenes Einkommen des Ehegatten/Partners (CHF)"
    reference = "SR 642.11 Art. 9 Abs. 1"


class einkommen_partner(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkommen des anderen Ehegatten/Partners (CHF)"
    reference = "SR 642.11 Art. 9 Abs. 1"


class einkommen_kinder_unter_elterlicher_sorge(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einkommen der Kinder unter elterlicher Sorge (ohne Erwerbseinkommen, CHF)"
    reference = "SR 642.11 Art. 9 Abs. 2"


class gemeinsame_veranlagung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person gemeinsam mit Ehegatte/Partner veranlagt wird"
    reference = "SR 642.11 Art. 9 Abs. 1, 1bis"

    def formula(person, period, parameters):
        verheiratet = person('ist_verheiratet_zusammenlebend', period)
        partnerschaft = person('ist_eingetragene_partnerschaft', period)
        return verheiratet + partnerschaft


class zusammengerechnetes_einkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zusammengerechnetes Einkommen der Ehegatten/Partner inkl. Kindereinkommen (CHF)"
    reference = "SR 642.11 Art. 9"

    def formula(person, period, parameters):
        gemeinsam = person('gemeinsame_veranlagung', period)
        eigenes = person('einkommen_ehegatte', period)
        partner = person('einkommen_partner', period)
        kinder = person('einkommen_kinder_unter_elterlicher_sorge', period)

        # Art. 9 Abs. 1/1bis: Zusammenrechnung bei gemeinsamer Veranlagung
        # Art. 9 Abs. 2: Kindereinkommen (ohne Erwerbseinkommen) wird zugerechnet
        return where(gemeinsam,
                     eigenes + partner + kinder,
                     eigenes + kinder)
