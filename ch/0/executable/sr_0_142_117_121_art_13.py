"""SR 0.142.117.121 Art. 13

Generated from: ch/0/de/0.142.117.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Currently, OpenFisca is not designed to model this regulation.
# A possible extension would involve creating a new Entity for "state" and Variables describing the different modalities and costs of the return of a person.
