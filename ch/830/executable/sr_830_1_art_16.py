"""SR 830.1 Art. 16

Generated from: ch/830/de/830.1.md

Art. 16: Grad der Invalidität - The degree of disability is determined by
comparing the income the insured person could earn after disability
(Invalideneinkommen) with the income they could earn if not disabled
(Valideneinkommen).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class valideneinkommen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = (
        "Erwerbseinkommen, das die versicherte Person erzielen könnte, wenn "
        "sie nicht invalid geworden wäre (Valideneinkommen)"
    )
    reference = "SR 830.1 Art. 16"


class invalideneinkommen(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = (
        "Erwerbseinkommen, das die versicherte Person nach Eintritt der Invalidität "
        "und nach Durchführung medizinischer Behandlung und Eingliederungsmassnahmen "
        "durch zumutbare Tätigkeit bei ausgeglichener Arbeitsmarktlage erzielen könnte"
    )
    reference = "SR 830.1 Art. 16"


class grad_der_invaliditaet(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Invaliditätsgrad nach Art. 16 ATSG (0.0 bis 1.0)"
    reference = "SR 830.1 Art. 16"

    def formula(person, period, parameters):
        validen = person('valideneinkommen', period)
        invaliden = person('invalideneinkommen', period)
        # Einkommensvergleich: (Valideneinkommen - Invalideneinkommen) / Valideneinkommen
        # Guard against division by zero
        return where(validen > 0, (validen - invaliden) / validen, 0)
