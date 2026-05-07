"""SR 614.0 Art. 19

Generated from: ch/614/de/614.0.md

Art. 19: Sonderregelungen - SNB und SUVA (ausser Militärversicherung)
unterstehen nicht der Finanzaufsicht durch die EFK. Weitere
Sonderregelungen bedürfen einer ausdrücklichen gesetzlichen Bestimmung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_schweizerische_nationalbank(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entität ist die Schweizerische Nationalbank (SNB)"
    reference = "SR 614.0 Art. 19 Abs. 1 lit. a"


class ist_suva(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entität ist die Schweizerische Unfallversicherungsanstalt (SUVA)"
    reference = "SR 614.0 Art. 19 Abs. 1 lit. b"


class ist_suva_militaerversicherung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entität ist die Militärversicherung der SUVA"
    reference = "SR 614.0 Art. 19 Abs. 1 lit. b"


class ausgenommen_von_efk_aufsicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Entität ist von der Finanzaufsicht durch die EFK ausgenommen "
        "(Art. 19 Abs. 1)"
    )
    reference = "SR 614.0 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        # Art. 19 Abs. 1 lit. a: SNB
        snb = person('ist_schweizerische_nationalbank', period)
        # Art. 19 Abs. 1 lit. b: SUVA, ausgenommen Militärversicherung
        suva = person('ist_suva', period)
        militaerversicherung = person('ist_suva_militaerversicherung', period)
        suva_ausgenommen = suva * (1 - militaerversicherung)
        return snb + suva_ausgenommen
