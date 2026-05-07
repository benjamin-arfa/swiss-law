"""SR 614.0 Art. 2

Generated from: ch/614/de/614.0.md

Art. 2: Organisation - Die EFK wird von einem Direktor/einer Direktorin
geleitet. Wahl durch Bundesrat für 6 Jahre, Genehmigung durch
Bundesversammlung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class efk_direktor_amtsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Amtsdauer des EFK-Direktors/der EFK-Direktorin in Jahren (Art. 2 Abs. 2)"
    reference = "SR 614.0 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        # Art. 2 Abs. 2: Der Bundesrat wählt den Direktor oder die Direktorin
        # für eine Amtsdauer von sechs Jahren.
        return 6


class efk_direktor_wahl_genehmigung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Wahl des EFK-Direktors bedarf der Genehmigung durch die "
        "Bundesversammlung (Art. 2 Abs. 2)"
    )
    reference = "SR 614.0 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        # Die Wahl bedarf der Genehmigung durch die Bundesversammlung.
        return True


class efk_direktor_abberufung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Bundesrat kann EFK-Direktor bei schwerwiegender Amtspflichtverletzung "
        "vor Ablauf der Amtsdauer abberufen (Art. 2 Abs. 2)"
    )
    reference = "SR 614.0 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return person('schwerwiegende_amtspflichtverletzung_efk_direktor', period)


class schwerwiegende_amtspflichtverletzung_efk_direktor(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Schwerwiegende Amtspflichtverletzung des EFK-Direktors liegt vor"
    reference = "SR 614.0 Art. 2 Abs. 2"
