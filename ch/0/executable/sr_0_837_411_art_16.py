"""SR 0.837.411 Art. 16 - Equal treatment of foreigners

Art. 16: Foreigners must receive benefits under the same conditions as
nationals. However, non-contributory benefits may be denied to nationals
of states not bound by the convention.

Generated from: ch/0/fr/0.837.411.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class est_ressortissant_etat_partie(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person is a national of a state party to ILO Convention 44 (Art. 16)"
    default_value = True


class egalite_traitement_chomage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person entitled to equal treatment for unemployment benefits (Art. 16)"

    def formula(person, period, parameters):
        est_partie = person("est_ressortissant_etat_partie", period)
        # Nationals of non-party states may be excluded from non-contributory benefits
        # but contributory benefits (indemnities) are always equal
        return est_partie + person("systeme_indemnite_chomage", period)
