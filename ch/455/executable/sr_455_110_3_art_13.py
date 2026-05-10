"""SR 455.110.3 Art. 13

Generated from: ch/455/de/455.110.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_afrikanischer_strauss(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist ein afrikanischer Strauss"
    reference = "SR 455.110.3 Art. 13 Abs. 3"


class ist_emu_oder_nandu(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist ein Emu oder Nandu"
    reference = "SR 455.110.3 Art. 13 Abs. 3"


class laufvogel_zaunhoehe_m(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoehe des Aussenzauns fuer Laufvoegel in Metern"
    reference = "SR 455.110.3 Art. 13 Abs. 3"


class verwendet_elektrozaun(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es werden Elektrozaeune verwendet"
    reference = "SR 455.110.3 Art. 13 Abs. 2"


class laufvogel_zaun_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zaun fuer Laufvoegel konform nach Art. 13 SR 455.110.3"
    reference = "SR 455.110.3 Art. 13"

    def formula(person, period, parameters):
        strauss = person('ist_afrikanischer_strauss', period)
        emu_nandu = person('ist_emu_oder_nandu', period)
        hoehe = person('laufvogel_zaunhoehe_m', period)
        elektro = person('verwendet_elektrozaun', period)

        # Abs. 2: Keine Elektrozaeune
        kein_elektro = not_(elektro)
        # Abs. 3: Mindesthoehe 1.8m fuer Strausse, 1.6m fuer Emus/Nandus
        hoehe_ok = where(strauss, hoehe >= 1.8, where(emu_nandu, hoehe >= 1.6, True))

        return kein_elektro * hoehe_ok
