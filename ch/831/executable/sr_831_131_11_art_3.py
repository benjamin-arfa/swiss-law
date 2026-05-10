"""SR 831.131.11 Art. 3

Generated from: ch/831/de/831.131.11.md

Refugees abroad: those who left Switzerland and reside in a country
with a bilateral social insurance agreement are treated as nationals
of that country for ordinary pension claims.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class fluechtling_im_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Fluechtling die Schweiz verlassen hat und im Ausland wohnt"
    reference = "SR 831.131.11 Art. 3"


class wohnsitzstaat_hat_vereinbarung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Wohnsitzstaat eine Sozialversicherungsvereinbarung mit der Schweiz hat"
    reference = "SR 831.131.11 Art. 3 Abs. 1"


class fluechtling_ausland_gleichstellung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Gleichstellung mit Angehoerigen des Wohnsitzstaates fuer ordentliche Renten"
    reference = "SR 831.131.11 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        ist_fl = person('ist_fluechtling', period)
        im_ausland = person('fluechtling_im_ausland', period)
        vereinbarung = person('wohnsitzstaat_hat_vereinbarung', period)
        return ist_fl * im_ausland * vereinbarung


class fluechtling_ausland_beitragsrueckerstattung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Anspruch auf Rueckerstattung der Beitraege (Art. 18 Abs. 3 AHVG)"
    reference = "SR 831.131.11 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        ist_fl = person('ist_fluechtling', period)
        im_ausland = person('fluechtling_im_ausland', period)
        vereinbarung = person('wohnsitzstaat_hat_vereinbarung', period)
        # Only if Abs. 1 does NOT apply (no bilateral agreement)
        return ist_fl * im_ausland * not_(vereinbarung)
