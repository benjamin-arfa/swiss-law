"""SR 511.41 Art. 1 – Ausbildungen mit Rückerstattungspflicht

Generated from: ch/511/de/511.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class ausbildung_fuehrerausweis_kategorie(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Kategorie des durch die Armee erworbenen Führerausweises (C oder CE)"
    reference = "SR 511.41 Art. 1"
    default_value = ""


class rueckerstattungsbetrag_ausbildungskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Rückerstattungsbetrag für Ausbildungskosten (CHF)"
    reference = "SR 511.41 Art. 1"

    def formula(person, period, parameters):
        kategorie = person('ausbildung_fuehrerausweis_kategorie', period)

        # Art. 1 Abs. 1: Kat. C = 7000 CHF, Kat. CE = 10000 CHF
        betrag = where(kategorie == 'CE', 10000.0,
                 where(kategorie == 'C', 7000.0, 0.0))

        # Art. 1 Abs. 2: Beträge werden nicht kumuliert; es gilt der höchste Betrag
        return betrag
