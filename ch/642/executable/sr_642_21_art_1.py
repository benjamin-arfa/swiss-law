"""SR 642.21 Art. 1 - Grundsatz (Principle of Withholding Tax)

Generated from: ch/642/de/642.21.md

Art. 1: The Confederation levies a withholding tax (Verrechnungssteuer) on:
- Income from movable capital assets
- Gambling winnings (BGS)
- Lottery/skill-game winnings for sales promotion
- Insurance benefits
The tax is refunded to the recipient per this law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vstg_ertrag_bewegliches_kapitalvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ertrag aus beweglichem Kapitalvermoegen (CHF)"
    reference = "SR 642.21 Art. 1 Abs. 1"
    default_value = 0.0


class vstg_gewinn_geldspiele(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewinne aus Geldspielen im Sinne des BGS (CHF)"
    reference = "SR 642.21 Art. 1 Abs. 1"
    default_value = 0.0


class vstg_gewinn_lotterien(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsfoerderung (CHF)"
    reference = "SR 642.21 Art. 1 Abs. 1"
    default_value = 0.0


class vstg_versicherungsleistung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherungsleistungen, die der Verrechnungssteuer unterliegen (CHF)"
    reference = "SR 642.21 Art. 1 Abs. 1"
    default_value = 0.0


class vstg_steuerbare_leistung_total(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtbetrag der verrechnungssteuerpflichtigen Leistungen (CHF)"
    reference = "SR 642.21 Art. 1"

    def formula(person, period, parameters):
        kapital = person('vstg_ertrag_bewegliches_kapitalvermoegen', period)
        geldspiele = person('vstg_gewinn_geldspiele', period)
        lotterien = person('vstg_gewinn_lotterien', period)
        versicherung = person('vstg_versicherungsleistung', period)
        return kapital + geldspiele + lotterien + versicherung
