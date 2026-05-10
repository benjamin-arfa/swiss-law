"""SR 442.132.3 Art. 8

Generated from: ch/442/de/442.132.3.md

Familienzulagen und ergaenzende Leistungen: Familienzulage nach FamZG.
Wenn Familienzulage tiefer als massgebende ergaenzende Leistungen,
zahlt Stiftung die Differenz. Ergaenzende Leistungen nach Beschaeftigungsgrad.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class familienzulage_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Familienzulage nach Familienzulagengesetz (CHF/Monat)"
    reference = "SR 442.132.3 Art. 8 Abs. 1"


class massgebender_betrag_ergaenzende_leistungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Massgebender Betrag der ergaenzenden Leistungen nach Anhang 2 (CHF/Monat)"
    reference = "SR 442.132.3 Art. 8 Abs. 2"


class ergaenzende_leistungen_pro_helvetia(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Ergaenzende Leistungen (Differenz Familienzulage zu massgebendem Betrag)"
    reference = "SR 442.132.3 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        zulage = person('familienzulage_betrag', period)
        massgebend = person('massgebender_betrag_ergaenzende_leistungen', period)
        grad = person('beschaeftigungsgrad', period.this_year)
        import numpy as np
        differenz = np.maximum(massgebend - zulage, 0)
        return differenz * grad
