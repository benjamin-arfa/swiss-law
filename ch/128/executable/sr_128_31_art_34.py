"""SR 128.31 Art. 34

Generated from: ch/128/de/128.31.md

Gebuehrenerhebung: Fees for checks outside central federal administration
and army, at CHF 100-400/hour. No fees for ISG-based PSP and BPG checks.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_zentrale_bundesverwaltung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Stelle zur zentralen Bundesverwaltung oder Armee gehoert"
    reference = "SR 128.31 Art. 34 Abs. 1"


class ist_psp_nach_isg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine PSP nach dem ISG handelt"
    reference = "SR 128.31 Art. 34 Abs. 3"


class ist_pruefung_nach_bpg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um eine Pruefung der Vertrauenswuerdigkeit nach Art. 20b BPG handelt"
    reference = "SR 128.31 Art. 34 Abs. 3"


class gebuehrenpflicht_psp(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob fuer die Personensicherheitspruefung Gebuehren erhoben werden"
    reference = "SR 128.31 Art. 34"

    def formula(person, period, parameters):
        import numpy as np
        extern = np.logical_not(person('ist_zentrale_bundesverwaltung', period))
        nicht_isg = np.logical_not(person('ist_psp_nach_isg', period))
        nicht_bpg = np.logical_not(person('ist_pruefung_nach_bpg', period))
        return extern * nicht_isg * nicht_bpg


class stundenansatz_min(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Minimaler Stundenansatz in CHF"
    reference = "SR 128.31 Art. 34 Abs. 2"
    default_value = 100


class stundenansatz_max(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximaler Stundenansatz in CHF"
    reference = "SR 128.31 Art. 34 Abs. 2"
    default_value = 400
