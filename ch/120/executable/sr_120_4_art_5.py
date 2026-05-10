"""SR 120.4 Art. 5

Generated from: ch/120/de/120.4.md

Stellungspflichtige sowie Angehoerige der Armee und des Zivilschutzes.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_stellungspflichtiger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person stellungspflichtig ist"
    reference = "SR 120.4 Art. 5"


class ist_angehoeriger_der_armee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Angehoerige/r der Armee ist"
    reference = "SR 120.4 Art. 5"


class funktion_nach_anhang_2(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person fuer eine Funktion nach Anhang 2 vorgesehen ist"
    reference = "SR 120.4 Art. 5 Abs. 1 lit. a"


class ist_angehoeriger_des_zivilschutzes(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Angehoerige/r des Zivilschutzes ist"
    reference = "SR 120.4 Art. 5 Abs. 1 lit. b"


class psp_pflicht_armee_zivilschutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Armee-/Zivilschutzangehoerige einer PSP unterzogen werden"
    reference = "SR 120.4 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        # Abs. 1 lit. a: Stellungspflichtige/Armeeangehoerige fuer Funktion nach Anhang 2
        armee_anhang2 = (
            person('ist_stellungspflichtiger', period) +
            person('ist_angehoeriger_der_armee', period)
        ) * person('funktion_nach_anhang_2', period)

        # Abs. 1 lit. b: Zivilschutzangehoerige mit Zugang zu klassifizierten Infos
        zivilschutz = person('ist_angehoeriger_des_zivilschutzes', period) * (
            person('zugang_vertraulich_klassifizierte_informationen', period) +
            person('zugang_geheim_klassifizierte_informationen', period) +
            person('zugang_schutzzone_2', period) +
            person('zugang_schutzzone_3', period)
        )

        return armee_anhang2 + zivilschutz > 0
