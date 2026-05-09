"""SR 672.201 Art. 3 — Steuerpflicht als Voraussetzung

Art. 3: Die Anrechnung kann nur beansprucht werden für Erträge, die den
Einkommens- oder Gewinnsteuern des Bundes, der Kantone und Gemeinden unterliegen.
Erträge sind ohne Abzug der ausländischen Steuer zu deklarieren.

Generated from: ch/672/de/672.201.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_switzerland.entities import Person


class ertrag_unterliegt_ch_einkommenssteuer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ertrag unterliegt den Einkommens-/Gewinnsteuern von Bund, Kantonen und Gemeinden (SR 672.201 Art. 3 Abs. 1)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_3"


class voraussetzung_anrechnung_steuerpflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzung Steuerpflicht für Anrechnung erfüllt (SR 672.201 Art. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_3"

    def formula(person, period, parameters):
        # Art. 3 Abs. 1: Anrechnung nur für Erträge, die den schweizerischen
        # Einkommens- oder Gewinnsteuern unterliegen.
        hat_anspruch = person('anspruch_anrechnung_auslaendischer_quellensteuern', period)
        unterliegt_steuer = person('ertrag_unterliegt_ch_einkommenssteuer', period)
        return hat_anspruch * unterliegt_steuer


class deklaration_brutto_ohne_abzug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erträge sind ohne Abzug der Steuer des Vertragsstaates zu deklarieren (SR 672.201 Art. 3 Abs. 2)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1967/1319_1375_1361/de#art_3"
    default_value = True
