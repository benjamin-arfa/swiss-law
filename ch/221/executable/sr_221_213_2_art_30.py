"""SR 221.213.2 Art. 30

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class parzellenweise_verpachtung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einzelne Grundstücke oder Teile von einem landwirtschaftlichen Gewerbe verpachtet"
    reference = "SR 221.213.2 Art. 30 Abs. 1"


class anteil_verpachteter_nutzflaeche(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der verpachteten Nutzfläche an der ursprünglichen Nutzfläche des Gewerbes (0-1)"
    reference = "SR 221.213.2 Art. 30 Abs. 2"


class pachtgegenstand_umfasst_gebaeude(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pachtgegenstand umfasst Gebäude"
    reference = "SR 221.213.2 Art. 30 Abs. 2"


class bewilligungspflicht_parzellenweise_verpachtung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Parzellenweise Verpachtung bedarf einer Bewilligung"
    reference = "SR 221.213.2 Art. 30"

    def formula(person, period, parameters):
        parzellenweise = person('parzellenweise_verpachtung', period)
        anteil = person('anteil_verpachteter_nutzflaeche', period)
        hat_gebaeude = person('pachtgegenstand_umfasst_gebaeude', period)
        # Keine Bewilligung nötig wenn max 10% und keine Gebäude
        befreit = (anteil <= 0.10) * not_(hat_gebaeude)
        return parzellenweise * not_(befreit)
