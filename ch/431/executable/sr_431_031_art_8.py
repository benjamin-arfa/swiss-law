"""SR 431.031 Art. 8

Generated from: ch/431/de/431.031.md

UID-Ergaenzung - HR/RC fuer Handelsregister, MWST/TVA/IVA fuer Mehrwertsteuer.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class uid_ergaenzung_handelsregister_de(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "UID-Ergaenzung fuer Handelsregister (deutsch)"
    reference = "SR 431.031 Art. 8 Abs. 1 Bst. a"
    default_value = "HR"


class uid_ergaenzung_handelsregister_fr(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "UID-Ergaenzung fuer Handelsregister (franzoesisch)"
    reference = "SR 431.031 Art. 8 Abs. 1 Bst. b"
    default_value = "RC"


class uid_ergaenzung_mwst_de(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "UID-Ergaenzung fuer Mehrwertsteuerregister (deutsch)"
    reference = "SR 431.031 Art. 8 Abs. 2 Bst. a"
    default_value = "MWST"


class uid_ergaenzung_mwst_fr(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "UID-Ergaenzung fuer Mehrwertsteuerregister (franzoesisch)"
    reference = "SR 431.031 Art. 8 Abs. 2 Bst. b"
    default_value = "TVA"


class uid_ergaenzung_mwst_it(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "UID-Ergaenzung fuer Mehrwertsteuerregister (italienisch)"
    reference = "SR 431.031 Art. 8 Abs. 2 Bst. c"
    default_value = "IVA"


class uid_ergaenzung_fuehrung_freiwillig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fuehrung der UID-Ergaenzung in Datenbanken ist freiwillig"
    reference = "SR 431.031 Art. 8 Abs. 4"
    default_value = True
