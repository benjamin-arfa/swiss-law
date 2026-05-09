"""SR 654.11 Art. 4 - Einreichungspflicht eines anderen konstitutiven Rechtstraegers

Generated from: ch/654/de/654.11.md

When the ESTV obliges another Swiss-resident constituent entity to
file the CbC report and it does not wish to file itself, it must
inform the ESTV within 30 days which entity will file.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class estv_verpflichtet_anderen_rechtstraeger(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die ESTV hat einen anderen konstitutiven Rechtstraeger zur Einreichung verpflichtet"
    reference = "SR 654.11 Art. 4"


class will_bericht_nicht_selbst_einreichen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der konstitutive Rechtstraeger will den Bericht nicht selbst einreichen"
    reference = "SR 654.11 Art. 4"


class mitteilungsfrist_30_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist zur Mitteilung, welcher Rechtstraeger den Bericht einreichen wird (30 Tage)"
    reference = "SR 654.11 Art. 4"
    default_value = 30
