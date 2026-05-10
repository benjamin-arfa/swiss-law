"""SR 746.12 Art. 1

Generated from: ch/746/de/746.12.md

Rohrleitungssicherheitsverordnung (RLSV) - Geltungsbereich.
Gilt fuer Projektierung, Bau, Betrieb und Unterhalt der dem RLG
unterstehenden Rohrleitungsanlagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unterliegt_rlsv(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anlage unterliegt der Rohrleitungssicherheitsverordnung (RLSV, SR 746.12)"
    reference = "SR 746.12 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        # Art. 1 Abs. 1: Diese Verordnung gilt fuer Projektierung, Bau,
        # Betrieb und Unterhalt der dem RLG unterstehenden Rohrleitungsanlagen.
        return person('unterliegt_rohrleitungsgesetz', period)


class ist_gasleitung_unter_5bar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gasleitung mit maximalem Betriebsdruck bis 0.5 MPa (5 bar) - nur Art. 2 und 3 gelten"
    reference = "SR 746.12 Art. 1 Abs. 2"


class rohrleitung_betriebsdruck_mpa(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Betriebsdruck der Rohrleitung in MPa"
    reference = "SR 746.12 Art. 1 Abs. 2"
