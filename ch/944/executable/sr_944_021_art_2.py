"""SR 944.021 Art. 2-3

Generated from: ch/944/de/944.021.md

Holzdeklaration: Declaration obligations for wood type and origin.
Sellers must declare trade name, scientific name, and country of harvest.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class holz_handelsname_deklariert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Handelsname des Holzes angegeben ist"
    reference = "SR 944.021 Art. 2 Abs. 1 Bst. a"


class holz_wissenschaftlicher_name_ermittelbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der wissenschaftliche Name des Holzes ermittelbar ist"
    reference = "SR 944.021 Art. 2 Abs. 1 Bst. b"


class holz_herkunftsland_deklariert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Herkunftsland (Ernteland) des Holzes angegeben ist"
    reference = "SR 944.021 Art. 3 Abs. 1-2"


class holz_deklaration_in_amtssprache(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Deklaration in einer Amtssprache des Bundes erfolgt"
    reference = "SR 944.021 Art. 4 Abs. 4"


class holz_deklaration_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Holzdeklaration den Vorschriften entspricht"
    reference = "SR 944.021 Art. 2-4"

    def formula(person, period, parameters):
        handelsname = person('holz_handelsname_deklariert', period)
        wissenschaftlich = person('holz_wissenschaftlicher_name_ermittelbar', period)
        herkunft = person('holz_herkunftsland_deklariert', period)
        sprache = person('holz_deklaration_in_amtssprache', period)
        return handelsname * wissenschaftlich * herkunft * sprache
