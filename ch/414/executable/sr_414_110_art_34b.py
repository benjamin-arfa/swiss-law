"""SR 414.110 Art. 34b

Generated from: ch/414/de/414.110.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Note: This article defines the federal funding mechanism for the ETH domain.
# The computation is at institutional level. We model the key duration rule.


class zahlungsrahmen_dauer_jahre(Variable):
    """Dauer des Zahlungsrahmens fuer den ETH-Bereich (immer 4 Jahre)"""
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer des Zahlungsrahmens in Jahren"
    reference = "SR 414.110 Art. 34b Abs. 2"

    def formula(person, period, parameters):
        # Die Bundesversammlung legt jeweils fuer vier Jahre den Zahlungsrahmen fest
        return person.filled_array(4)


class finanzierungsbeitrag_unabhaengig_drittmittel(Variable):
    """Der Finanzierungsbeitrag ist unabhaengig von den Drittmitteln"""
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Finanzierungsbeitrag unabhaengig von Drittmitteln"
    reference = "SR 414.110 Art. 34b Abs. 3"

    def formula(person, period, parameters):
        # Immer wahr gemaess Gesetz
        return person.filled_array(True)
