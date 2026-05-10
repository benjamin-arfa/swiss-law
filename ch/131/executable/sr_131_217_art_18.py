"""SR 131.217 Art. 18

Generated from: ch/131/de/131.217.md

Staatshaftung: Kanton, Gemeinden und andere öffentlich-rechtliche
Körperschaften haften für den Schaden, den ihre Behördenmitglieder,
Angestellten und Lehrpersonen oder andere im öffentlichen Auftrag
tätige Personen durch eine Amtshandlung rechtswidrig verursacht haben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class person_handelt_im_oeffentlichen_auftrag_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person im öffentlichen Auftrag tätig ist (Behördenmitglied, Angestellte, Lehrperson)"
    reference = "SR 131.217 Art. 18 Abs. 1"


class amtshandlung_rechtswidrig_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Amtshandlung rechtswidrig war"
    reference = "SR 131.217 Art. 18 Abs. 1"


class schaden_durch_amtshandlung_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Schaden durch die Amtshandlung verursacht wurde"
    reference = "SR 131.217 Art. 18 Abs. 1"


class staatshaftung_gl(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Staatshaftung des Kantons Glarus greift"
    reference = "SR 131.217 Art. 18 Abs. 1"

    def formula(person, period, parameters):
        oeffentlich = person('person_handelt_im_oeffentlichen_auftrag_gl', period)
        rechtswidrig = person('amtshandlung_rechtswidrig_gl', period)
        schaden = person('schaden_durch_amtshandlung_gl', period)
        return oeffentlich * rechtswidrig * schaden
