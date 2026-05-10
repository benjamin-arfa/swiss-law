"""SR 961.01 Art. 21 — Participations / Beteiligungen

Generated from: ch/961/fr/961.01.md

LSA — Participation notification thresholds:
- Swiss insurer acquiring participation in another entity: notify FINMA at 10/20/33/50%
- Anyone acquiring participation in a Swiss insurer: notify FINMA at 10/20/33/50%
- Anyone reducing participation below 10/20/33/50%: notify FINMA
- FINMA can prohibit or impose conditions on harmful participations
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class taux_participation_acquise(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux de participation acquise dans une autre entreprise (% du capital ou des droits de vote)"
    reference = "SR 961.01 Art. 21 al. 1"


class taux_participation_precedent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Taux de participation avant la transaction (%)"
    reference = "SR 961.01 Art. 21"


class obligation_annonce_participation(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Obligation d'annoncer la participation à la FINMA"
    reference = "SR 961.01 Art. 21 al. 1-3"

    def formula(person, period, parameters):
        taux_actuel = person('taux_participation_acquise', period)
        taux_precedent = person('taux_participation_precedent', period)
        # Notification required when crossing 10%, 20%, 33%, or 50% thresholds
        seuils = numpy.array([10.0, 20.0, 33.0, 50.0])
        franchissement = numpy.zeros_like(taux_actuel, dtype=bool)
        for seuil in seuils:
            # Crossing upward
            franchissement = franchissement | (
                (taux_precedent < seuil) & (taux_actuel >= seuil)
            )
            # Crossing downward
            franchissement = franchissement | (
                (taux_precedent >= seuil) & (taux_actuel < seuil)
            )
        return franchissement
