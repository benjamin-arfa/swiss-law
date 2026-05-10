"""SR 831.232.51 Art. 9

Generated from: ch/831/de/831.232.51.md

Art. 9: Anspruch auf Verguetung von Dienstleistungen - Entitlement to
compensation for services provided by third parties as substitute for aids.

Abs. 1: The insured person is entitled to compensation for documented
disability-related costs for special services provided by third parties
that are necessary in lieu of an aid, to:
a. overcome the commute to work
b. practice the profession
c. acquire special skills enabling contact with the environment

Abs. 2: Annual compensation may not exceed EITHER the insured person's
annual employment income OR 1.5x the annual minimum full AHV pension
(Art. 34 AHVG).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hvi_dienstleistungskosten_dritter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ausgewiesene invaliditaetsbedingte Kosten fuer Dienstleistungen Dritter"
    reference = "SR 831.232.51 Art. 9 Abs. 1"


class hvi_dienstleistung_notwendig_statt_hilfsmittel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Dienstleistung ist anstelle eines Hilfsmittels notwendig (Arbeitsweg, Beruf, Kontakt)"
    reference = "SR 831.232.51 Art. 9 Abs. 1"


class hvi_jahres_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliches Erwerbseinkommen der versicherten Person"
    reference = "SR 831.232.51 Art. 9 Abs. 2"


class hvi_mindestbetrag_vollrente_ahv(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Mindestbetrag der Vollrente nach Art. 34 AHVG"
    reference = "SR 831.232.51 Art. 9 Abs. 2"


class hvi_dienstleistungsverguetung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Verguetung fuer Dienstleistungen Dritter (Art. 9 HVI)"
    reference = "SR 831.232.51 Art. 9"

    def formula(person, period, parameters):
        kosten = person('hvi_dienstleistungskosten_dritter', period)
        notwendig = person('hvi_dienstleistung_notwendig_statt_hilfsmittel', period)
        einkommen = person('hvi_jahres_erwerbseinkommen', period)
        min_vollrente = person('hvi_mindestbetrag_vollrente_ahv', period)

        # Cap: lower of (annual income, 1.5x minimum full pension)
        obergrenze = min_(einkommen, min_vollrente * 1.5)

        return notwendig * min_(kosten, obergrenze)
