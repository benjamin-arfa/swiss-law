"""SR 836.2 Art. 9

Generated from: ch/836/de/836.2.md

Art. 9: Auszahlung an Dritte.
Abs. 1: Werden die Familienzulagen nicht fuer die Beduerfnisse der
berechtigten Person verwendet, kann diese oder ihr gesetzlicher
Vertreter die direkte Auszahlung verlangen.
Abs. 2: Auf begruendetes Gesuch hin kann die Ausbildungszulage
in Abweichung von Art. 20 Abs. 1 ATSG auch dem muendigen Kind
direkt ausgerichtet werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class familienzulage_nicht_zweckmaessig_verwendet(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Familienzulagen werden nicht fuer die Beduerfnisse der berechtigten Person verwendet"
    reference = "SR 836.2 Art. 9 Abs. 1"


class drittauszahlung_verlangt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Direkte Auszahlung an die berechtigte Person oder deren Vertreter verlangt"
    reference = "SR 836.2 Art. 9 Abs. 1"


class kind_ist_muendig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kind ist muendig (volljaehrig)"
    reference = "SR 836.2 Art. 9 Abs. 2"


class direktauszahlung_an_muendiges_kind(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ausbildungszulage wird direkt an das muendige Kind ausgerichtet (Art. 9 Abs. 2)"
    reference = "SR 836.2 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        muendig = person('kind_ist_muendig', period)
        in_ausbildung = person('kind_in_nachobligatorischer_ausbildung', period)
        return muendig * in_ausbildung
