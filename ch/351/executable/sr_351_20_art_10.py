"""SR 351.20 Art. 10

Generated from: ch/351/de/351.20.md
Conditions for transfer of a person to an international court.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tat_faellt_in_zustaendigkeit_internationales_gericht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Tat faellt in die Zustaendigkeit des Internationalen Gerichts"
    reference = "SR 351.20 Art. 10 Abs. 1 lit. a"


class tat_nach_schweizerischem_recht_strafbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Tat ist nach schweizerischem Recht strafbar"
    reference = "SR 351.20 Art. 10 Abs. 1 lit. b"


class person_ist_schweizer_buerger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist Schweizer Buerger"
    reference = "SR 351.20 Art. 10 Abs. 2"


class gericht_sichert_rueckueberstellung_zu(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Internationales Gericht sichert Rueckueberstellung nach Verfahrensabschluss zu"
    reference = "SR 351.20 Art. 10 Abs. 2"


class ueberstellung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ueberstellung an Internationales Gericht ist zulaessig"
    reference = "SR 351.20 Art. 10"

    def formula(person, period):
        zustaendigkeit = person('tat_faellt_in_zustaendigkeit_internationales_gericht', period)
        strafbar = person('tat_nach_schweizerischem_recht_strafbar', period)
        schweizer = person('person_ist_schweizer_buerger', period)
        zusicherung = person('gericht_sichert_rueckueberstellung_zu', period)

        # Grundvoraussetzungen: Zustaendigkeit UND Strafbarkeit
        grundvoraussetzung = zustaendigkeit * strafbar

        # Schweizer Buerger: zusaetzlich Zusicherung der Rueckueberstellung
        schweizer_ok = schweizer * zusicherung
        nicht_schweizer = not_(schweizer)

        return grundvoraussetzung * (nicht_schweizer + schweizer_ok)
