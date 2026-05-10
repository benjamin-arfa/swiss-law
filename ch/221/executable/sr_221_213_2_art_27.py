"""SR 221.213.2 Art. 27

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erstreckung_fuer_beklagten_zumutbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Erstreckung der Pacht ist für den Beklagten zumutbar"
    reference = "SR 221.213.2 Art. 27 Abs. 1"


class paechter_schwerwiegend_gegen_pflichten_verstossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pächter hat schwerwiegend gegen gesetzliche oder vertragliche Pflichten verstossen"
    reference = "SR 221.213.2 Art. 27 Abs. 2 lit. a"


class paechter_zahlungsunfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pächter ist zahlungsunfähig"
    reference = "SR 221.213.2 Art. 27 Abs. 2 lit. b"


class verpaechter_will_selbst_bewirtschaften(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Verpächter oder naher Angehöriger will den Pachtgegenstand selber bewirtschaften"
    reference = "SR 221.213.2 Art. 27 Abs. 2 lit. c"


class gewerbe_nicht_erhaltenswuerdig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gewerbe ist nicht erhaltenswürdig"
    reference = "SR 221.213.2 Art. 27 Abs. 2 lit. d"


class erstreckung_mindest_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestdauer der Pachterstreckung in Jahren"
    reference = "SR 221.213.2 Art. 27 Abs. 4"

    def formula(person, period, parameters):
        return person.filled_array(3)


class erstreckung_hoechst_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Höchstdauer der Pachterstreckung in Jahren"
    reference = "SR 221.213.2 Art. 27 Abs. 4"

    def formula(person, period, parameters):
        return person.filled_array(6)
