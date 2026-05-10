"""SR 745.1 Art. 4

Generated from: ch/745/de/745.1.md

Personenbefoerderungsregal - Grundsatz.
Der Bund hat das ausschliessliche Recht, Reisende mit regelmaessigen und
gewerbsmaessigen Fahrten zu befoerdern.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unterliegt_personenbefoerderungsregal(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit unterliegt dem Personenbefoerderungsregal des Bundes"
    reference = "SR 745.1 Art. 4"

    def formula(person, period, parameters):
        # Art. 4: Der Bund hat das ausschliessliche Recht, Reisende mit
        # regelmaessigen und gewerbsmaessigen Fahrten zu befoerdern,
        # soweit nicht durch andere Erlasse oder voelkerrechtliche Vertraege
        # eingeschraenkt.
        unterliegt_pbg = person('unterliegt_personenbefoerderungsgesetz', period)
        ist_ausgenommen = person('personenbefoerderungsregal_ausnahme', period)
        return unterliegt_pbg * ~ist_ausgenommen


class personenbefoerderungsregal_ausnahme(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausnahme vom Personenbefoerderungsregal durch andere Erlasse oder voelkerrechtliche Vertraege"
    reference = "SR 745.1 Art. 4-5"
