"""SR 251.4 Art. 4

Generated from: ch/251/de/251.4.md

Berechnung des Umsatzes: Erloese abzueglich Skonti, Rabatte, MWST
und andere Verbrauchssteuern. Geschaeftsjahre unter 12 Monaten
werden auf 12 Monate umgerechnet. Vorgaenge innerhalb von 2 Jahren
gelten als ein Zusammenschluss.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erloese_waren_leistungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erloese mit Waren und Leistungen im normalen Geschaeftsbereich"
    reference = "SR 251.4 Art. 4 Abs. 1"


class erloesminderungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Erloesminderungen (Skonti, Rabatte)"
    reference = "SR 251.4 Art. 4 Abs. 1"


class mehrwertsteuer_verbrauchssteuern(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mehrwertsteuern und andere Verbrauchssteuern"
    reference = "SR 251.4 Art. 4 Abs. 1"


class umsatzbezogene_steuern(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Weitere unmittelbar auf den Umsatz bezogene Steuern"
    reference = "SR 251.4 Art. 4 Abs. 1"


class geschaeftsjahr_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Monate des letzten Geschaeftsjahres"
    reference = "SR 251.4 Art. 4 Abs. 2"


class umsatz_berechnet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Berechneter Umsatz fuer die Zusammenschlusskontrolle"
    reference = "SR 251.4 Art. 4"

    def formula(person, period, parameters):
        erloese = person('erloese_waren_leistungen', period)
        minderungen = person('erloesminderungen', period)
        mwst = person('mehrwertsteuer_verbrauchssteuern', period)
        sonstige = person('umsatzbezogene_steuern', period)
        monate = person('geschaeftsjahr_monate', period)

        netto_umsatz = erloese - minderungen - mwst - sonstige
        # Auf 12 Monate umrechnen wenn noetig
        return where(monate < 12, netto_umsatz * 12 / monate, netto_umsatz)
