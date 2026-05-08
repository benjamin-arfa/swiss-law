"""SR 124 Art. 2 - Gesetzliche Grundlage (Legal Basis)

Generated from: ch/de/124.md
A protection task may only be delegated to a private company if a legal basis exists.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class schutzaufgabe_gesetzliche_grundlage(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesetzliche Grundlage fuer Uebertragung der Schutzaufgabe an privates Sicherheitsunternehmen besteht"
    reference = "SR 124 Art. 2"
    default_value = False
