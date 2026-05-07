"""SR 0.142.112.453 Art. 1

Generated from: ch/0/de/0.142.112.453.md
"""

from openfisca_core.model_api import * 
from openfisca_switzerland.entities import Person


class agreement_scope(Variable):
    value_type = str
    entity = Person
    default_value = None
    label = "Category of passport holder (Agreement of 1972)"

    entities = [
        'SwissDiplomat',
        'SwissMilitary',
        'ChileanDiplomat',
        'ChileanOfficial'
    ]
