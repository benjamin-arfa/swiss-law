"""SR 824.0 Art. 8

Generated from: ch/824/de/824.0.md

Art. 8: Duration of civilian service (Zivildienst):
- Standard multiplier: 1.5x remaining military service days
- Former higher NCOs/officers: 1.1x remaining military service days
- Foreign deployments: can volunteer for up to 1.5x the total duration
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zdg_verbleibende_militaerdiensttage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Verbleibende, noch nicht geleistete Ausbildungsdiensttage nach Militärgesetzgebung"
    reference = "SR 824.0 Art. 8 Abs. 1"


class zdg_war_hoeher_unteroffizier_oder_offizier(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "War höherer Unteroffizier oder Offizier"
    reference = "SR 824.0 Art. 8 Abs. 1"
    default_value = False


class zdg_zivildienstdauer_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Gesamtdauer des Zivildienstes in Tagen"
    reference = "SR 824.0 Art. 8 Abs. 1"

    def formula(person, period, parameters):
        mil_tage = person('zdg_verbleibende_militaerdiensttage', period)
        ist_offizier = person('zdg_war_hoeher_unteroffizier_oder_offizier', period)

        p = parameters(period).sr_824_0

        # 1.5x for standard, 1.1x for former higher NCOs/officers
        faktor = where(ist_offizier, p.faktor_offizier, p.faktor_standard)
        return (mil_tage * faktor).astype(int)


class zdg_auslandeinsatz_max_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Zivildienstdauer bei Auslandeinsätzen (Tage)"
    reference = "SR 824.0 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        zd_tage = person('zdg_zivildienstdauer_tage', period)
        # Max 1.5x the total civilian service duration
        return (zd_tage * 1.5).astype(int)
