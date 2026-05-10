"""SR 831.20 Art. 28b

Generated from: ch/831/de/831.20.md

Art. 28b: Festlegung der Hoehe des Rentenanspruchs - Pension level as
percentage of a full pension, based on the degree of disability:

- IV >= 70%: 100% (full pension)
- IV 50-69%: percentage = IV degree
- IV 49%: 47.5%
- IV 48%: 45%
- IV 47%: 42.5%
- IV 46%: 40%
- IV 45%: 37.5%
- IV 44%: 35%
- IV 43%: 32.5%
- IV 42%: 30%
- IV 41%: 27.5%
- IV 40%: 25%
- IV < 40%: 0% (no entitlement)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_rentenanteil_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prozentualer Anteil an einer ganzen IV-Rente (0-100)"
    reference = "SR 831.20 Art. 28b"

    def formula(person, period, parameters):
        iv_grad = person('iv_invaliditaetsgrad_prozent', period)

        # Art. 28b Abs. 3: IV >= 70% -> full pension (100%)
        # Art. 28b Abs. 2: IV 50-69% -> percentage equals IV degree
        # Art. 28b Abs. 4: IV 40-49% -> lookup table (linear: 2.5pp per 1pp IV)
        # IV < 40%: no entitlement

        # Table for IV 40-49 (Art. 28b Abs. 4)
        anteil = select(
            [
                iv_grad >= 70,
                iv_grad >= 50,
                iv_grad >= 49,
                iv_grad >= 48,
                iv_grad >= 47,
                iv_grad >= 46,
                iv_grad >= 45,
                iv_grad >= 44,
                iv_grad >= 43,
                iv_grad >= 42,
                iv_grad >= 41,
                iv_grad >= 40,
            ],
            [
                100.0,
                iv_grad,   # 50-69: equals IV degree
                47.5,
                45.0,
                42.5,
                40.0,
                37.5,
                35.0,
                32.5,
                30.0,
                27.5,
                25.0,
            ],
            default=0.0,
        )
        return anteil
