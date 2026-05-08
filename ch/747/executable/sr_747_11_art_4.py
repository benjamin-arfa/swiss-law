"""SR 747.11 Art. 4

Generated from: ch/747/de/747.11.md

Art. 4: Mandatory registration of inland vessels in the Swiss ship register.
Requirements:
a. >50% Swiss ownership (person with domicile or company with seat in CH)
b. commercial transport of persons/goods on Swiss waters or Rhine below Rheinfelden
c. carrying capacity >= 20t, or water displacement >= 10m³ (non-cargo)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class schiffsreg_eigentumsanteil_schweiz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eigentumsanteil mit Wohnsitz/Sitz in der Schweiz (0-1)"
    reference = "SR 747.11 Art. 4 Abs. 1 Bst. a"


class schiffsreg_gewerbsmaessige_befoerderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schiff wird zur gewerbsmässigen Beförderung von Personen oder Gütern verwendet"
    reference = "SR 747.11 Art. 4 Abs. 1 Bst. b"


class schiffsreg_tragfaehigkeit_tonnen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tragfähigkeit des Schiffes in Tonnen"
    reference = "SR 747.11 Art. 4 Abs. 1 Bst. c"


class schiffsreg_wasserverdraengung_m3(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Wasserverdrängung des Schiffes in Kubikmetern"
    reference = "SR 747.11 Art. 4 Abs. 1 Bst. c"


class schiffsreg_ist_gueterschiff(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schiff dient der Beförderung von Gütern"
    reference = "SR 747.11 Art. 4 Abs. 1 Bst. c"


class schiffsreg_registrierungspflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Obligatorische Aufnahme in das Schiffsregister (Art. 4)"
    reference = "SR 747.11 Art. 4"

    def formula(person, period, parameters):
        eigentum_ch = person('schiffsreg_eigentumsanteil_schweiz', period)
        gewerbe = person('schiffsreg_gewerbsmaessige_befoerderung', period)
        tragfaehigkeit = person('schiffsreg_tragfaehigkeit_tonnen', period)
        verdraengung = person('schiffsreg_wasserverdraengung_m3', period)
        ist_gueter = person('schiffsreg_ist_gueterschiff', period)

        p = parameters(period).sr_747_11

        # a. >50% Swiss ownership
        eigentum_ok = eigentum_ch > 0.5

        # b. commercial transport
        gewerbe_ok = gewerbe

        # c. carrying capacity >= 20t (cargo) or displacement >= 10m³ (non-cargo)
        groesse_ok = where(
            ist_gueter,
            tragfaehigkeit >= p.mindest_tragfaehigkeit_obligatorisch,
            verdraengung >= p.mindest_verdraengung_obligatorisch
        )

        return eigentum_ok * gewerbe_ok * groesse_ok
