"""SR 831.30 Art. 16b

Generated from: ch/831/de/831.30.md

Art. 16b: Verwirkung - Prescription/forfeiture of the restitution claim.

The restitution claim expires:
- 1 year after the competent body (Art. 21 Abs. 2) becomes aware of it, or
- at the latest 10 years after each individual benefit payment.

Introduced by the EL Reform of 22 March 2019, in force since 1 Jan. 2021.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_rueckforderung_kenntnisnahme_datum(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Datum der Kenntnisnahme durch zustaendige Stelle (Art. 16b ELG)"
    reference = "SR 831.30 Art. 16b"


class el_letzte_leistungsentrichtung_datum(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Datum der letzten einzelnen Leistungsentrichtung (Art. 16b ELG)"
    reference = "SR 831.30 Art. 16b"


class el_rueckforderung_relative_frist_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Relative Verwirkungsfrist: 12 Monate ab Kenntnisnahme (Art. 16b ELG)"
    reference = "SR 831.30 Art. 16b"

    def formula(person, period, parameters):
        import numpy as np
        return np.full(len(person.ids), 12)


class el_rueckforderung_absolute_frist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Absolute Verwirkungsfrist: 10 Jahre ab Leistungsentrichtung (Art. 16b ELG)"
    reference = "SR 831.30 Art. 16b"

    def formula(person, period, parameters):
        import numpy as np
        return np.full(len(person.ids), 10)
