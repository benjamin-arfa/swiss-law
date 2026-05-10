"""SR 321.0 Art. 30

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class geldstrafe_nicht_bezahlt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Verurteilte hat die Geldstrafe nicht bezahlt und sie ist auf dem Betreibungsweg uneinbringlich"
    reference = "SR 321.0 Art. 30 Abs. 1"


class ersatzfreiheitsstrafe_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Ersatzfreiheitsstrafe in Tagen (1 Tagessatz = 1 Tag Freiheitsstrafe)"
    reference = "SR 321.0 Art. 30 Abs. 1"

    def formula(person, period, parameters):
        nicht_bezahlt = person('geldstrafe_nicht_bezahlt', period)
        anzahl = person('geldstrafe_anzahl_tagessaetze', period)
        return nicht_bezahlt * anzahl
