"""SR 913.211 Art. 4

Generated from: ch/913/de/913.211.md

Berücksichtigung der Lage der landwirtschaftlichen Nutzfläche:
- Wenn > 2/3 in einer Zone: Ansatz dieser Zone
- Wenn nicht > 2/3 in einer Zone: Mittelwert der mehrheitlich betroffenen Zonen
- Entfernte Flächen (>15km) nur bei traditioneller Stufenwirtschaft berücksichtigt
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anteil_nutzflaeche_hauptzone(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Nutzfläche in der Hauptzone (0.0 bis 1.0)"
    reference = "SR 913.211 Art. 4 Abs. 1"


class ansatz_hauptzone(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Investitionshilfe-Ansatz der Hauptzone in CHF"
    reference = "SR 913.211 Art. 4 Abs. 1 Bst. a"


class mittelwert_ansatz_zonen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mittelwert der Ansätze der mehrheitlich betroffenen Zonen in CHF"
    reference = "SR 913.211 Art. 4 Abs. 1 Bst. b"


class entfernung_zum_betriebszentrum_km(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Entfernung der Nutzfläche zum Betriebszentrum in km"
    reference = "SR 913.211 Art. 4 Abs. 2"


class ist_traditioneller_stufenbetrieb(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um einen traditionellen Stufenbetrieb handelt"
    reference = "SR 913.211 Art. 4 Abs. 2"


class anwendbarer_investitionshilfe_ansatz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwendbarer Investitionshilfe-Ansatz in CHF"
    reference = "SR 913.211 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        anteil = person('anteil_nutzflaeche_hauptzone', period)
        ansatz_haupt = person('ansatz_hauptzone', period)
        mittelwert = person('mittelwert_ansatz_zonen', period)
        schwelle = parameters(period).sr_913_211.schwelle_hauptzone_anteil

        return np.where(anteil > schwelle, ansatz_haupt, mittelwert)


class entfernte_flaeche_anrechenbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob entfernte Flächen (>15km) anrechenbar sind"
    reference = "SR 913.211 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        entfernung = person('entfernung_zum_betriebszentrum_km', period)
        stufenbetrieb = person('ist_traditioneller_stufenbetrieb', period)
        max_km = parameters(period).sr_913_211.max_entfernung_betriebszentrum_km

        return np.where(
            entfernung > max_km,
            stufenbetrieb,
            True
        )
