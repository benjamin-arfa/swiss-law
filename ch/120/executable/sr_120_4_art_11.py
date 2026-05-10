"""SR 120.4 Art. 11

Generated from: ch/120/de/120.4.md

Erweiterte Personensicherheitspruefung: Extended security check for persons
with access to GEHEIM classified information/material or Schutzzone 3.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class regelmaessiger_zugang_besonders_schuetzenswerte_personendaten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Regelmaessiger Zugang zu besonders schuetzenswerten Personendaten (BWIS/Justiz/Polizei)"
    reference = "SR 120.4 Art. 11 Abs. 2 lit. f"


class auslandeinsatz_hoheitliche_vertretung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person vertritt die Schweiz hoheitlich im Auslandeinsatz"
    reference = "SR 120.4 Art. 11 Abs. 2 lit. d"


class erweiterte_psp_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine erweiterte Personensicherheitspruefung erforderlich ist"
    reference = "SR 120.4 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        ist_bediensteter = person('ist_bediensteter_des_bundes', period)
        ist_kantonsangestellter = person('ist_angestellter_des_kantons', period)
        ist_armee = person('ist_angehoeriger_der_armee', period)
        ist_zivilschutz = person('ist_angehoeriger_des_zivilschutzes', period)
        ist_dritter = person('ist_dritter_an_klassifiziertem_projekt', period)
        zugang_g = person('zugang_geheim_klassifizierte_informationen', period)
        zugang_sz3 = person('zugang_schutzzone_3', period)

        # lit. a: Bedienstete/Kantonsangestellte mit regelm. Zugang GEHEIM
        bedienstete_geheim = (ist_bediensteter + ist_kantonsangestellter) * zugang_g

        # lit. b: Armee/Zivilschutz/Dritte mit Zugang zu GEHEIM
        armee_dritte_geheim = (ist_armee + ist_zivilschutz + ist_dritter) * zugang_g

        # lit. c: Zugang zu Schutzzone 3
        schutzzone3 = zugang_sz3

        # lit. d: Hoheitliche Vertretung im Ausland
        hoheitlich = person('auslandeinsatz_hoheitliche_vertretung', period)

        # lit. f: Regelm. Zugang zu besonders schuetzenswerten Personendaten
        personendaten = person('regelmaessiger_zugang_besonders_schuetzenswerte_personendaten', period)

        return (bedienstete_geheim + armee_dritte_geheim + schutzzone3 + hoheitlich + personendaten) > 0
