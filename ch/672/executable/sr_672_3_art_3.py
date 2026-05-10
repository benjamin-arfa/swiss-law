"""SR 672.3 Art. 3 — Entzug der Anerkennung

Bundesgesetz über die Anerkennung privater Vereinbarungen zur Vermeidung der Doppelbesteuerung.
Generated from: ch/de/672/672.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class reziprozitaet_nicht_mehr_gewaehrleistet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Reziprozität ist nicht mehr gewährleistet (SR 672.3 Art. 3 lit. a)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_3"


class vereinbarung_schwer_verletzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Vereinbarung ist in schwerer Weise verletzt worden (SR 672.3 Art. 3 lit. b)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_3"


class wahrung_landesinteressen_erfordert_entzug(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Wahrung der Interessen des Landes erfordert den Entzug (SR 672.3 Art. 3 lit. c)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_3"


class entzug_anerkennung_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bundesrat kann der Vereinbarung die Anerkennung entziehen (SR 672.3 Art. 3)"
    reference = "https://www.fedlex.admin.ch/eli/cc/2011/680/de#art_3"

    def formula(person, period, parameters):
        # Art. 3: Der Bundesrat kann die Anerkennung entziehen, wenn:
        # a) Reziprozität nicht mehr gewährleistet
        # b) Vereinbarung schwer verletzt
        # c) Wahrung der Landesinteressen es erfordert
        keine_reziprozitaet = person('reziprozitaet_nicht_mehr_gewaehrleistet', period)
        schwere_verletzung = person('vereinbarung_schwer_verletzt', period)
        landesinteressen = person('wahrung_landesinteressen_erfordert_entzug', period)
        return keine_reziprozitaet + schwere_verletzung + landesinteressen > 0
