"""SR 322.1 Art. 2

Generated from: ch/322/de/322.1.md

Einteilung in die Militaerjustiz: Als Justizoffiziere koennen Angehoerige
der Armee eingeteilt werden, die ein juristisches Studium mit Lizentiat/Master
oder ein kantonales Anwaltspatent besitzen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_angehoeriger_der_armee_justiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Angehoerige der Armee ist"
    reference = "SR 322.1 Art. 2 Abs. 1"


class hat_juristisches_studium_lizentiat_master(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein juristisches Studium mit Lizentiat oder Master abgeschlossen hat"
    reference = "SR 322.1 Art. 2 Abs. 1"


class hat_kantonales_anwaltspatent(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ueber ein kantonales Anwaltspatent verfuegt"
    reference = "SR 322.1 Art. 2 Abs. 1"


class aufgabe_erfordert_juristisches_fachwissen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Aufgabe juristisches Fachwissen verlangt"
    reference = "SR 322.1 Art. 2 Abs. 2"


class kann_als_justizoffizier_eingeteilt_werden(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Justizoffizier in die Militaerjustiz eingeteilt werden kann"
    reference = "SR 322.1 Art. 2"

    def formula_2018(person, period, parameters):
        """Fassung gemaess BG vom 18. Maerz 2016, in Kraft seit 1. Jan. 2018."""
        ist_armee = person('ist_angehoeriger_der_armee_justiz', period)
        hat_studium = person('hat_juristisches_studium_lizentiat_master', period)
        hat_patent = person('hat_kantonales_anwaltspatent', period)
        erfordert_jura = person('aufgabe_erfordert_juristisches_fachwissen', period)

        # Abs. 1: Juristische Qualifikation erforderlich
        qualifiziert_abs1 = ist_armee * (hat_studium + hat_patent > 0)

        # Abs. 2: Ohne juristische Qualifikation moeglich, wenn kein Fachwissen noetig
        qualifiziert_abs2 = ist_armee * (1 - erfordert_jura)

        return (qualifiziert_abs1 + qualifiziert_abs2) > 0
