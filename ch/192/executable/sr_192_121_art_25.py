"""SR 192.121 Art. 25

Generated from: ch/192/de/192.121.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class grundstueck_nettowohnflaeche_m2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Nettowohnflaeche des zu erwerbenden Gebaeudes in m2"
    reference = "SR 192.121 Art. 25"

class grundstueck_wohnflaeche_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nettowohnflaeche ueberschreitet nicht 200 m2 (Art. 25 Abs. 3)"
    reference = "SR 192.121 Art. 25"

    def formula(person, period, parameters):
        flaeche = person('grundstueck_nettowohnflaeche_m2', period)
        return flaeche <= 200
