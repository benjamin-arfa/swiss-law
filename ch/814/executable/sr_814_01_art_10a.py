"""SR 814.01 Art. 10a-10b

Generated from: ch/fr/814/814.01.md

Art. 10a: Etude de l'impact sur l'environnement (UVP - Umweltvertraeglichkeitspruefung)
- Abs. 1: Before deciding on planning/construction/modification, authority must examine
  compatibility with environmental law as early as possible.
- Abs. 2: EIA required for installations that may significantly affect the environment.
- Abs. 3: Federal Council designates installation types requiring EIA and may set thresholds.
Art. 10b: Rapport relatif a l'impact (UVP-Bericht)
- Abs. 1: Project proponent must submit an EIA report to competent authority.
- Abs. 2: Report must cover: initial state, project + measures, remaining impacts.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class usg_anlage_uvp_pflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Anlage UVP-pflichtig ist (wesentliche Umweltauswirkungen moeglich)"
    reference = "SR 814.01 Art. 10a Abs. 2"


class usg_uvp_bericht_eingereicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob ein UVP-Bericht eingereicht wurde"
    reference = "SR 814.01 Art. 10b Abs. 1"


class usg_uvp_bericht_vollstaendig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob der UVP-Bericht den Ausgangszustand, das Projekt und verbleibende Belastungen enthaelt"
    reference = "SR 814.01 Art. 10b Abs. 2"


class usg_uvp_anforderung_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die UVP-Anforderungen erfuellt sind"
    reference = "SR 814.01 Art. 10a-10b"

    def formula(person, period, parameters):
        pflichtig = person('usg_anlage_uvp_pflichtig', period)
        eingereicht = person('usg_uvp_bericht_eingereicht', period)
        vollstaendig = person('usg_uvp_bericht_vollstaendig', period)

        # Not UVP-required: ok
        # UVP-required: need complete report
        return not_(pflichtig) + (pflichtig * eingereicht * vollstaendig)
