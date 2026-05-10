"""SR 142.201.1 Art. 2

Generated from: ch/142/de/142.201.1.md

Aufenthalt ohne Erwerbstaetigkeit von Staatsangehoerigen von
Nichtmitgliedstaaten der EU oder der EFTA: Bewilligungen, die dem
SEM zur Zustimmung zu unterbreiten sind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_student_doktorand_postdoc(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Schueler/in, Student/in, Doktorand/in oder Postdoc ist"
    reference = "SR 142.201.1 Art. 2 Bst. a"


class kommt_aus_sicherheitsrisikoland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person aus einem Land mit erhoehtem Sicherheitsrisiko stammt (SEM-Liste)"
    reference = "SR 142.201.1 Art. 2 Bst. a"


class aufenthalt_medizinische_behandlung_ueber_1_jahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Aufenthalt fuer medizinische Behandlung voraussichtlich ein Jahr oder laenger dauert"
    reference = "SR 142.201.1 Art. 2 Bst. b"


class ist_rentner(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Rentner/in ist (Art. 28 AIG)"
    reference = "SR 142.201.1 Art. 2 Bst. c"


class ist_pflegekind_zur_adoption(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person ein Pflegekind zur Adoption ist (Art. 48 AIG)"
    reference = "SR 142.201.1 Art. 2 Bst. d"


class zustimmung_sem_ohne_erwerbstaetigkeit_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustimmung des SEM fuer Aufenthalt ohne Erwerbstaetigkeit erforderlich ist"
    reference = "SR 142.201.1 Art. 2"

    def formula(person, period, parameters):
        nicht_eu = person('ist_staatsangehoeriger_nicht_eu_efta', period)
        student_risiko = (
            person('ist_student_doktorand_postdoc', period)
            * person('kommt_aus_sicherheitsrisikoland', period)
        )
        return nicht_eu * (
            student_risiko
            + person('aufenthalt_medizinische_behandlung_ueber_1_jahr', period)
            + person('ist_rentner', period)
            + person('ist_pflegekind_zur_adoption', period)
        ) > 0
