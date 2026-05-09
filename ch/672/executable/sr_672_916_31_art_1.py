"""SR 672.916.31 Art. 1 — Kantone erheben Quellensteuer auf Grenzgänger

Verordnung zum CH-AT Doppelbesteuerungsabkommen (Besteuerung von Grenzgängern).
Art. 1: Die Kantone dürfen im Rahmen ihrer Gesetzgebung Einkünfte aus
unselbständiger Erwerbstätigkeit von in Österreich ansässigen Grenzgängern
einer Quellensteuer von höchstens 4% unterwerfen (Art. 15 Abs. 4 DBA).

Generated from: ch/672/de/672.916.31.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_switzerland.entities import Person


class ist_grenzgaenger_at_ch(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person ist in Österreich ansässiger Grenzgänger mit Erwerbstätigkeit in der Schweiz (SR 672.916.31 Art. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_1"


class einkommen_unselbstaendig_grenzgaenger_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Einkünfte aus unselbständiger Erwerbstätigkeit eines AT-Grenzgängers in der Schweiz"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_1"
    default_value = 0


class quellensteuer_grenzgaenger_at_max_satz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Quellensteuersatz auf Grenzgänger-Einkommen (höchstens 4%, Art. 15 Abs. 4 DBA)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_1"
    default_value = 0.04


class quellensteuer_grenzgaenger_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Quellensteuer auf Einkünfte von AT-Grenzgängern (SR 672.916.31 Art. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_1"

    def formula(person, period, parameters):
        # Art. 1: Kantone dürfen Einkünfte aus unselbständiger Erwerbstätigkeit
        # von in Österreich ansässigen Grenzgängern einer Quellensteuer von
        # höchstens 4% unterwerfen.
        ist_grenzgaenger = person('ist_grenzgaenger_at_ch', period)
        einkommen = person('einkommen_unselbstaendig_grenzgaenger_at', period)
        max_satz = person('quellensteuer_grenzgaenger_at_max_satz', period)
        return ist_grenzgaenger * einkommen * max_satz
