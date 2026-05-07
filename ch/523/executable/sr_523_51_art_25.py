"""SR 523.51 Art. 25

Generated from: ch/523/de/523.51.md

Note: Art. 25 imposes a duty of confidentiality on the oversight commission
members and teaching staff regarding performance evaluations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class schweigepflicht_leistungsbewertung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist zur Verschwiegenheit ueber Leistungsbewertungen verpflichtet"
    reference = "SR 523.51 Art. 25"
