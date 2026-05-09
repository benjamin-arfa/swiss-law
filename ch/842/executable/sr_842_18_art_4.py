"""SR 842.18 Art. 4

Generated from: ch/842/de/842.18.md

Vermietung: Rental priority rules for federally subsidized housing cooperatives
of federal personnel (WBG). Priority tenants are federal employees, PUBLICA-affiliated
employees, and their retirees. Exceptions allowed for 4+ room apartments with 3+ occupants.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_bundesangestellter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angestellte des Bundes nach Art. 2 Abs. 1 BPG"
    reference = "SR 842.18 Art. 4 Abs. 1 lit. a"


class ist_publica_angeschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angestellte eines Arbeitgebers, der PUBLICA angeschlossen ist"
    reference = "SR 842.18 Art. 4 Abs. 1 lit. b"


class ist_pensioniert_bund(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vor Pensionierung Bundesangestellter gewesen"
    reference = "SR 842.18 Art. 4 Abs. 1 lit. c"


class ist_pensioniert_publica(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vor Pensionierung Angestellter eines PUBLICA-Arbeitgebers gewesen"
    reference = "SR 842.18 Art. 4 Abs. 1 lit. d"


class hat_vermietungsprioritaet_wbg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Vermietungsprioritaet fuer aktuell gefoerderte WBG-Wohnungen"
    reference = "SR 842.18 Art. 4 Abs. 1"

    def formula(person, period):
        return (
            person('ist_bundesangestellter', period) +
            person('ist_publica_angeschlossen', period) +
            person('ist_pensioniert_bund', period) +
            person('ist_pensioniert_publica', period)
        ) > 0


class anzahl_zimmer_wohnung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Zimmer der Wohnung"
    reference = "SR 842.18 Art. 4 Abs. 2 lit. a"


class anzahl_bewohner(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Personen, die die Wohnung belegen"
    reference = "SR 842.18 Art. 4 Abs. 2 lit. b"


class statuten_erlauben_abweichung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Statuten der WBG sehen Abweichung von Vermietungsprioritaet vor"
    reference = "SR 842.18 Art. 4 Abs. 2 lit. c"


class darf_von_vermietungsprioritaet_abweichen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Darf von Vermietungsprioritaeten abgewichen werden"
    reference = "SR 842.18 Art. 4 Abs. 2"

    def formula(person, period):
        # All three conditions must be met: >= 4 rooms, >= 3 occupants, statutes allow
        return (
            (person('anzahl_zimmer_wohnung', period) >= 4) *
            (person('anzahl_bewohner', period) >= 3) *
            person('statuten_erlauben_abweichung', period)
        )
