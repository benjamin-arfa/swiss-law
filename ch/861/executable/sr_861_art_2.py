"""SR 861 Art. 2

Generated from: ch/de/861.md

Recipients of financial aid: day-care centres, after-school care
facilities, family day-care coordination structures, and natural/legal
persons for innovation projects.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzhilfe_empfaenger_kindertagesstaette(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Kindertagesstaetten Finanzhilfen erhalten koennen"
    reference = "SR 861 Art. 2 Abs. 1 Bst. a"


class finanzhilfe_empfaenger_schulergaenzend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Einrichtungen fuer schulergaenzende Betreuung Finanzhilfen erhalten koennen"
    reference = "SR 861 Art. 2 Abs. 1 Bst. b"


class finanzhilfe_empfaenger_tagesfamilien_koordination(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Strukturen fuer die Koordination der Betreuung in Tagesfamilien Finanzhilfen erhalten koennen"
    reference = "SR 861 Art. 2 Abs. 1 Bst. c"


class finanzhilfe_empfaenger_innovationsprojekte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob natuerliche/juristische Personen fuer Innovationsprojekte Finanzhilfen erhalten koennen"
    reference = "SR 861 Art. 2 Abs. 1 Bst. d"


class finanzhilfe_primaer_neue_institutionen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Finanzhilfen in erster Linie fuer neue Institutionen gewaehrt werden"
    reference = "SR 861 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return True


class finanzhilfe_bestehende_institution_wesentliche_erhoehung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine bestehende Institution ihr Angebot wesentlich erhoeht"
    reference = "SR 861 Art. 2 Abs. 2"
