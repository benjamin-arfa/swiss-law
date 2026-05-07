"""SR 0.101.094 Art. 3

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

class Artikel24Abolition(Variable):
    value_type = bool
    entity = Person
    label = u"Abolition of Artikel 24 of the Convention"

    def valid(self, period):
        return False

    def default_period(self):
        return Period('always')
This code defines an OpenFisca variable that always returns False, effectively abolishing the Artikel 24.
