"""SR 142.209 Art. 8

Generated from: ch/142/de/142.209.md

Kantonale Hoechstgebuehren fuer auslaenderrechtliche Bewilligungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class art_auslaenderrechtliche_verfuegung(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Art der auslaenderrechtlichen Verfuegung (z.B. 'ermaechtigungVisum', 'erteilungBewilligung', etc.)"
    reference = "SR 142.209 Art. 8"
    default_value = ''


class ist_eu_efta_staatsangehoeriger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Staatsangehoerige/r eines FZA- oder EFTA-Vertragsstaats ist"
    reference = "SR 142.209 Art. 8 Abs. 4"


class ist_ledig_unter_18(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ledig und unter 18 Jahre alt ist"
    reference = "SR 142.209 Art. 8 Abs. 4 Bst. c"


# Fee constants (Abs. 1)
HOECHSTGEBUEHR_ERMAECHTIGUN_VISUM = 95
HOECHSTGEBUEHR_ERTEILUNG_BEWILLIGUNG = 95
HOECHSTGEBUEHR_STELLENANTRITT = 95
HOECHSTGEBUEHR_NIEDERLASSUNG = 95
HOECHSTGEBUEHR_VERLAENGERUNG_BEWILLIGUNG = 75
HOECHSTGEBUEHR_VERLAENGERUNG_NIEDERLASSUNG = 65
HOECHSTGEBUEHR_VERLAENGERUNG_VORLAEUFIG = 40
HOECHSTGEBUEHR_STRAFREGISTER = 25
HOECHSTGEBUEHR_ZEMIS_AENDERUNG = 30
HOECHSTGEBUEHR_MELDEBESTAETIGUNG = 25
HOECHSTGEBUEHR_UEBRIGE_AENDERUNGEN = 40
HOECHSTGEBUEHR_DUPLIKAT = 40

# Fee constants EU/EFTA (Abs. 4)
HOECHSTGEBUEHR_EU_EFTA_GESAMT = 65
HOECHSTGEBUEHR_EU_EFTA_UNTER_18_GESAMT = 30
HOECHSTGEBUEHR_EU_EFTA_UNTER_18_STRAFREGISTER = 20


class kantonale_hoechstgebuehr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kantonale Hoechstgebuehr fuer die auslaenderrechtliche Verfuegung (CHF)"
    reference = "SR 142.209 Art. 8"

    def formula(person, period, parameters):
        eu_efta = person('ist_eu_efta_staatsangehoeriger', period)
        unter_18 = person('ist_ledig_unter_18', period)

        # Vereinfachte Berechnung: EU/EFTA-Buerger haben reduzierte Gebuehren
        # Standard-Hoechstgebuehr fuer Erteilung/Erneuerung
        standard = 95.0
        eu_standard = where(unter_18, 30.0, 65.0)

        return where(eu_efta, eu_standard, standard)
