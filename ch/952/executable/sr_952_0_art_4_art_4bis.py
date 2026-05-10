"""SR 952.0 Art. 4, 4bis

Generated from: ch/952/de/952.0.md

Eigenmittel, Liquiditaet und Risikoverteilung:
- Art. 4: Banken muessen ueber angemessene Eigenmittel und Liquiditaet
  verfuegen (einzeln und konsolidiert). Qualifizierte Beteiligung an
  Nicht-Finanz-Unternehmen max. 15% Eigenmittel, insgesamt max. 60%.
- Art. 4bis: Ausleihungen an einzelnen Kunden muessen in angemessenem
  Verhaeltnis zu eigenen Mitteln stehen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bankg_eigenmittel_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Eigene Mittel der Bank (CHF)"
    reference = "SR 952.0 Art. 4 Abs. 1"


class bankg_beteiligung_nichtfinanz_einzeln(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Groesste Einzelbeteiligung an Nicht-Finanzunternehmen (CHF)"
    reference = "SR 952.0 Art. 4 Abs. 4"


class bankg_beteiligungen_nichtfinanz_gesamt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamtbetrag Beteiligungen an Nicht-Finanzunternehmen (CHF)"
    reference = "SR 952.0 Art. 4 Abs. 4"


class bankg_beteiligung_einzeln_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Einzelbeteiligung an Nicht-Finanzunternehmen zulaessig (max. 15% EM)"
    reference = "SR 952.0 Art. 4 Abs. 4"

    def formula(person, period, parameters):
        eigenmittel = person('bankg_eigenmittel_betrag', period)
        beteiligung = person('bankg_beteiligung_nichtfinanz_einzeln', period)
        p = parameters(period).sr952_0
        max_anteil = p.max_beteiligung_einzeln  # 0.15

        return beteiligung <= eigenmittel * max_anteil


class bankg_beteiligungen_gesamt_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamtbeteiligungen an Nicht-Finanzunternehmen zulaessig (max. 60% EM)"
    reference = "SR 952.0 Art. 4 Abs. 4"

    def formula(person, period, parameters):
        eigenmittel = person('bankg_eigenmittel_betrag', period)
        gesamt = person('bankg_beteiligungen_nichtfinanz_gesamt', period)
        p = parameters(period).sr952_0
        max_anteil = p.max_beteiligungen_gesamt  # 0.60

        return gesamt <= eigenmittel * max_anteil


class bankg_ausleihung_an_kunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Groesste Ausleihung an einzelnen Kunden (CHF)"
    reference = "SR 952.0 Art. 4bis Abs. 1"


class bankg_klumpenrisiko_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Eigenmittel- und Beteiligungslimiten eingehalten"
    reference = "SR 952.0 Art. 4, 4bis"

    def formula(person, period, parameters):
        return (
            person('bankg_beteiligung_einzeln_zulaessig', period)
            * person('bankg_beteiligungen_gesamt_zulaessig', period)
        )
