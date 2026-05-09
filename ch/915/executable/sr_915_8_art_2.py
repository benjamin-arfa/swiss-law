"""SR 915.8 Art. 2

Generated from: ch/915/de/915.8.md

FKINV - Art. 2: Grundsatz fuer die Gewaehrung der Finanzhilfe.
Finanzhilfen im Rahmen bewilligter Kredite, kein Anspruch.
Je Bereich wird ein einziges Netzwerk unterstuetzt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class fkinv_kein_anspruch_auf_finanzhilfe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Es besteht kein Anspruch auf Finanzhilfen; Gewaehrung im Rahmen "
        "der bewilligten Kredite (Art. 2 Abs. 1)"
    )
    reference = "SR 915.8 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        # Art. 2 Abs. 1: Structural provision - no entitlement to subsidies.
        # Always true as a legal principle.
        return person('fkinv_finanzhilfe_voraussetzungen_erfuellt', period) * 0 + 1


class fkinv_ein_netzwerk_pro_bereich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Je Bereich (Pflanzenzuechtung, Tierzucht, Tiergesundheit) wird ein "
        "einziges Kompetenz- und Innovationsnetzwerk unterstuetzt (Art. 2 Abs. 2)"
    )
    reference = "SR 915.8 Art. 2 Abs. 2"
