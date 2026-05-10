"""SR 210 Art. 27

Generated from: ch/de/210.md

Schutz der Persoenlichkeit - Verzicht auf Rechts- und Handlungsfaehigkeit:
Auf die Rechts- und Handlungsfaehigkeit kann niemand ganz oder zum Teil
verzichten. Niemand kann sich seiner Freiheit entaeussern oder sich in ihrem
Gebrauch in einem das Recht oder die Sittlichkeit verletzenden Grade
beschraenken.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_verzicht_auf_rechtsfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein (unzulaessiger) Verzicht auf Rechtsfaehigkeit vorliegt"
    reference = "SR 210 Art. 27 Abs. 1"


class ist_verzicht_auf_handlungsfaehigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein (unzulaessiger) Verzicht auf Handlungsfaehigkeit vorliegt"
    reference = "SR 210 Art. 27 Abs. 1"


class ist_uebermassige_freiheitsbeschraenkung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine das Recht oder die Sittlichkeit verletzende Freiheitsbeschraenkung vorliegt"
    reference = "SR 210 Art. 27 Abs. 2"


class ist_persoenlichkeitsschutz_verletzt_art27(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Persoenlichkeitsschutz nach Art. 27 ZGB verletzt ist"
    reference = "SR 210 Art. 27"

    def formula(person, period, parameters):
        # Abs. 1: Verzicht auf Rechts-/Handlungsfaehigkeit ist unzulaessig
        verzicht_rf = person('ist_verzicht_auf_rechtsfaehigkeit', period)
        verzicht_hf = person('ist_verzicht_auf_handlungsfaehigkeit', period)
        # Abs. 2: Uebermassige Freiheitsbeschraenkung ist unzulaessig
        uebermassig = person('ist_uebermassige_freiheitsbeschraenkung', period)
        return (verzicht_rf + verzicht_hf + uebermassig) > 0
