"""SR 836.2 Art. 3

Generated from: ch/836/de/836.2.md

Art. 3: Arten von Familienzulagen - Types of family allowances:
- Kinderzulage: from birth month until end of month child turns 16
  (or 20 if incapacitated)
- Ausbildungszulage: from month post-obligatory education begins
  (earliest at 15), until end of education (max age 25)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_kind(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Alter des Kindes in Jahren"
    reference = "SR 836.2 Art. 3 Abs. 1"


class kind_ist_erwerbsunfaehig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind ist erwerbsunfähig (Art. 7 ATSG)"
    reference = "SR 836.2 Art. 3 Abs. 1 lit. a"


class kind_in_nachobligatorischer_ausbildung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind befindet sich in nachobligatorischer Ausbildung"
    reference = "SR 836.2 Art. 3 Abs. 1 lit. b"


class kind_besucht_obligatorische_schule(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind besucht noch die obligatorische Schule"
    reference = "SR 836.2 Art. 3 Abs. 1 lit. b"


class anspruch_kinderzulage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf Kinderzulage nach Art. 3 Abs. 1 lit. a FamZG"
    reference = "SR 836.2 Art. 3 Abs. 1 lit. a"

    def formula(person, period, parameters):
        alter = person('alter_kind', period)
        erwerbsunfaehig = person('kind_ist_erwerbsunfaehig', period)
        in_ausbildung = person('kind_in_nachobligatorischer_ausbildung', period)
        # Kinderzulage bis 16, oder bis 20 wenn erwerbsunfähig
        # Kein Anspruch wenn bereits Ausbildungszulage bezogen wird
        bis_16 = alter < 16
        bis_20_erwerbsunfaehig = (alter < 20) * erwerbsunfaehig
        return (bis_16 + bis_20_erwerbsunfaehig > 0) * (1 - in_ausbildung)


class anspruch_ausbildungszulage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf Ausbildungszulage nach Art. 3 Abs. 1 lit. b FamZG"
    reference = "SR 836.2 Art. 3 Abs. 1 lit. b"

    def formula(person, period, parameters):
        alter = person('alter_kind', period)
        in_ausbildung = person('kind_in_nachobligatorischer_ausbildung', period)
        obligatorische_schule = person('kind_besucht_obligatorische_schule', period)
        # Ab 15, frühestens wenn nachobligatorische Ausbildung beginnt
        # Wenn nach 16 noch obligatorische Schule: ab dem Folgemonat
        alt_genug = alter >= 15
        nicht_zu_alt = alter < 25
        # Vereinfacht: Ausbildungszulage wenn >= 15, in Ausbildung, < 25
        return alt_genug * in_ausbildung * nicht_zu_alt * (1 - obligatorische_schule)
