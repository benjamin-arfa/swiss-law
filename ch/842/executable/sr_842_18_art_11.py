"""SR 842.18 Art. 11

Generated from: ch/842/de/842.18.md

Verzinsung und Amortisation der Darlehen: Interest rate rules for WBG loans.
- PUBLICA loans: max rate = reference mortgage rate + 0.25 percentage points
- Federal loans: max rate = PUBLICA rate minus up to 1 percentage point
- Interest and amortization payable semi-annually
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class referenzzinssatz_hypotheken_art11_pct(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Referenzzinssatz fuer Hypotheken nach Art. 12a VMWG (Prozent)"
    reference = "SR 842.18 Art. 11 Abs. 1"


class hoechstzinssatz_publica_darlehen_pct(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstzinssatz fuer PUBLICA-Darlehen an WBG (Prozent)"
    reference = "SR 842.18 Art. 11 Abs. 1"

    def formula(person, period):
        # Referenzzinssatz + 0.25 Prozentpunkte
        return person('referenzzinssatz_hypotheken_art11_pct', period) + 0.25


class verbilligung_bundesdarlehen_pp(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Verbilligung des Bundesdarlehens-Zinssatzes in Prozentpunkten (max 1.0)"
    reference = "SR 842.18 Art. 11 Abs. 2"
    default_value = 1.0


class hoechstzinssatz_bundesdarlehen_pct(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstzinssatz fuer Bundesdarlehen an WBG (Prozent)"
    reference = "SR 842.18 Art. 11 Abs. 2"

    def formula(person, period):
        # PUBLICA-Hoechstzinssatz minus Verbilligung (max 1 Prozentpunkt)
        publica_satz = person('hoechstzinssatz_publica_darlehen_pct', period)
        verbilligung = person('verbilligung_bundesdarlehen_pp', period)
        # Verbilligung darf maximal 1.0 Prozentpunkte betragen
        import numpy as np
        verbilligung_begrenzt = np.minimum(verbilligung, 1.0)
        return np.maximum(publica_satz - verbilligung_begrenzt, 0)


class darlehen_publica_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hypothekardarlehen aus Mitteln von PUBLICA (CHF)"
    reference = "SR 842.18 Art. 11 Abs. 1"


class darlehen_bund_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hypothekardarlehen aus Mitteln des Bundes (CHF)"
    reference = "SR 842.18 Art. 11 Abs. 2"


class jaehrliche_zinslast_publica_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jaehrliche Zinslast auf PUBLICA-Darlehen (CHF)"
    reference = "SR 842.18 Art. 11"

    def formula(person, period):
        return (
            person('darlehen_publica_chf', period) *
            person('hoechstzinssatz_publica_darlehen_pct', period) / 100
        )


class jaehrliche_zinslast_bund_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jaehrliche Zinslast auf Bundesdarlehen (CHF)"
    reference = "SR 842.18 Art. 11"

    def formula(person, period):
        return (
            person('darlehen_bund_chf', period) *
            person('hoechstzinssatz_bundesdarlehen_pct', period) / 100
        )
