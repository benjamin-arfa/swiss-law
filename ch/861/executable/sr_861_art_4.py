"""SR 861 Art. 4

Generated from: ch/de/861.md

Available funds: multi-year commitment credits for each type of
financial aid; 15% cap on innovation projects; priority ordering
by EDI when demand exceeds supply.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verpflichtungskredit_betreuungsplaetze(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bundesversammlung einen Verpflichtungskredit fuer Finanzhilfen nach dem 2. Abschnitt beschliesst"
    reference = "SR 861 Art. 4 Abs. 1"


class verpflichtungskredit_subventionen_projekte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Bundesversammlung einen Verpflichtungskredit fuer Finanzhilfen nach dem 2a. Abschnitt beschliesst"
    reference = "SR 861 Art. 4 Abs. 1"


class innovationsprojekte_maxanteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstanteil der Mittel fuer Innovationsprojekte am Verpflichtungskredit (Anteil)"
    reference = "SR 861 Art. 4 Abs. 2bis"

    def formula(person, period, parameters):
        return 0.15


class prioritaetenordnung_edi(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das EDI eine Prioritaetenordnung erlaesst wenn Gesuche die Mittel uebersteigen"
    reference = "SR 861 Art. 4 Abs. 3"
