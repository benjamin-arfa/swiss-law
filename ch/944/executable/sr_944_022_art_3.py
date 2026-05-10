"""SR 944.022 Art. 2a-5

Generated from: ch/944/de/944.022.md

Pelzdeklaration: Declaration obligations for fur and fur products.
Must declare: real fur label, animal species, origin, and method of
acquisition (cage, enclosure, or hunt).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pelz_echtpelz_deklariert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Deklaration 'Echtpelz' angebracht ist"
    reference = "SR 944.022 Art. 2a"


class pelz_tierart_deklariert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der wissenschaftliche und zoologische Name der Tierart angegeben ist"
    reference = "SR 944.022 Art. 3"


class pelz_herkunft_deklariert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Herkunft des Fells (Land) angegeben ist"
    reference = "SR 944.022 Art. 4 Abs. 1-2"


class pelz_gewinnungsart_deklariert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Gewinnungsart des Fells angegeben ist"
    reference = "SR 944.022 Art. 5 Abs. 1"


class pelz_deklaration_in_amtssprache(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Pelzdeklaration in mindestens einer Amtssprache erfolgt"
    reference = "SR 944.022 Art. 7 Abs. 2"


class pelz_deklaration_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Pelzdeklaration den Vorschriften entspricht"
    reference = "SR 944.022 Art. 2a-7"

    def formula(person, period, parameters):
        echtpelz = person('pelz_echtpelz_deklariert', period)
        tierart = person('pelz_tierart_deklariert', period)
        herkunft = person('pelz_herkunft_deklariert', period)
        gewinnung = person('pelz_gewinnungsart_deklariert', period)
        sprache = person('pelz_deklaration_in_amtssprache', period)
        return echtpelz * tierart * herkunft * gewinnung * sprache
