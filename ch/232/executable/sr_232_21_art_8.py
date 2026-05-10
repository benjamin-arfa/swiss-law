"""SR 232.21 Art. 8

Generated from: ch/232/de/232.21.md

Art. 8 regulates the use of coats of arms (Wappen). Only the entitled
public entity may use them, with specific exceptions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_berechtigtes_gemeinwesen_wappen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ist das Gemeinwesen, zu dem das Wappen gehoert"
    reference = "SR 232.21 Art. 8 Abs. 1"


class wappen_verwendung_in_woerterbuch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwendung des Wappens als Abbildung in Woerterbuechern, Nachschlagewerken oder wissenschaftlichen Werken"
    reference = "SR 232.21 Art. 8 Abs. 4 lit. a"


class wappen_verwendung_fuer_fest(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwendung des Wappens bei der Ausschmueckung von Festen und Veranstaltungen"
    reference = "SR 232.21 Art. 8 Abs. 4 lit. b"


class wappen_verwendung_kunstgewerbe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwendung des Wappens auf kunstgewerblichen Gegenstaenden fuer Feste"
    reference = "SR 232.21 Art. 8 Abs. 4 lit. c"


class wappen_verwendung_patentzeichen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwendung als Bestandteil des schweizerischen Patentzeichens"
    reference = "SR 232.21 Art. 8 Abs. 4 lit. d"


class wappen_verwendung_kollektivmarke(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Verwendung in Kollektiv- oder Garantiemarken eines Gemeinwesens"
    reference = "SR 232.21 Art. 8 Abs. 4 lit. e"


class hat_weiterbenuetzungsrecht_art_35(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Hat ein Weiterbenuetzungsrecht nach Art. 35 WSchG"
    reference = "SR 232.21 Art. 8 Abs. 4 lit. f"


class darf_wappen_gebrauchen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Darf das Schweizerwappen oder Kantonswappen gebrauchen"
    reference = "SR 232.21 Art. 8"

    def formula(person, period, parameters):
        # Abs. 1: nur das berechtigte Gemeinwesen
        ist_gemeinwesen = person('ist_berechtigtes_gemeinwesen_wappen', period)

        # Abs. 4: Ausnahmen fuer andere Personen
        woerterbuch = person('wappen_verwendung_in_woerterbuch', period)
        fest = person('wappen_verwendung_fuer_fest', period)
        kunstgewerbe = person('wappen_verwendung_kunstgewerbe', period)
        patent = person('wappen_verwendung_patentzeichen', period)
        kollektiv = person('wappen_verwendung_kollektivmarke', period)
        weiterben = person('hat_weiterbenuetzungsrecht_art_35', period)

        ausnahme = woerterbuch + fest + kunstgewerbe + patent + kollektiv + weiterben

        return ist_gemeinwesen + (ausnahme > 0) > 0
