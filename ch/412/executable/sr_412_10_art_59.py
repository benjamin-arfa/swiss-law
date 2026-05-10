"""SR 412.10 Art. 59

Generated from: ch/412/de/412.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Note: This article operates at the system/institutional level rather than
# individual level, but we model it as a computation on aggregate values.


class aufwendungen_oeffentliche_hand_berufsbildung(Variable):
    """Gesamtaufwendungen der oeffentlichen Hand fuer Berufsbildung"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Aufwendungen der oeffentlichen Hand fuer Berufsbildung in CHF"
    reference = "SR 412.10 Art. 59 Abs. 2"


class richtgroesse_bundesanteil(Variable):
    """Richtgroesse: ein Viertel der Aufwendungen der oeffentlichen Hand"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Richtgroesse fuer Kostenbeteiligung des Bundes (25%)"
    reference = "SR 412.10 Art. 59 Abs. 2"

    def formula(person, period, parameters):
        aufwendungen = person('aufwendungen_oeffentliche_hand_berufsbildung', period)
        return aufwendungen * 0.25


class max_anteil_projekte_leistungen(Variable):
    """Maximaler Anteil fuer Projekte und besondere Leistungen (Art. 54/55): 10%"""
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Bundesbeitrag fuer Projekte/Leistungen (10% des Bundesanteils)"
    reference = "SR 412.10 Art. 59 Abs. 2"

    def formula(person, period, parameters):
        bundesanteil = person('richtgroesse_bundesanteil', period)
        return bundesanteil * 0.10
