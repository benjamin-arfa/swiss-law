"""SR 120.4 Art. 10

Generated from: ch/120/de/120.4.md

Grundsicherheitspruefung: Basic security check conducted for persons with
access to VERTRAULICH classified information/material or Schutzzone 2.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class grundsicherheitspruefung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Grundsicherheitspruefung erforderlich ist"
    reference = "SR 120.4 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        ist_bediensteter = person('ist_bediensteter_des_bundes', period)
        ist_kantonsangestellter = person('ist_angestellter_des_kantons', period)
        ist_armee = person('ist_angehoeriger_der_armee', period)
        ist_zivilschutz = person('ist_angehoeriger_des_zivilschutzes', period)
        ist_dritter = person('ist_dritter_an_klassifiziertem_projekt', period)
        zugang_v = person('zugang_vertraulich_klassifizierte_informationen', period)
        zugang_sz2 = person('zugang_schutzzone_2', period)

        # lit. a: Bedienstete/Kantonsangestellte mit regelmaessigem Zugang zu VERTRAULICH
        bedienstete_vertraulich = (ist_bediensteter + ist_kantonsangestellter) * zugang_v

        # lit. b: Armee/Zivilschutz/Dritte mit Zugang zu VERTRAULICH
        armee_dritte_vertraulich = (ist_armee + ist_zivilschutz + ist_dritter) * zugang_v

        # lit. c: Zugang zu Schutzzone 2
        schutzzone = zugang_sz2

        return (bedienstete_vertraulich + armee_dritte_vertraulich + schutzzone) > 0
