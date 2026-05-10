"""SR 821.421 Art. 1

Generated from: ch/821/de/821.421.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wbf_ermaechtigt_einigungsstelle(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "WBF ist ermaechtigt, von Fall zu Fall eine eidgenoessische "
        "Einigungsstelle einzusetzen"
    )
    reference = "SR 821.421 Art. 1 Abs. 1"


class kollektivstreitigkeit_mehrkantonal(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Vom Streit betroffene Betriebe oder Zweigbetriebe liegen "
        "in mehr als einem Kanton"
    )
    reference = "SR 821.421 Art. 1 Abs. 3"


class voraussetzungen_einigungsstelle_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "Voraussetzungen fuer die Einsetzung der Einigungsstelle sind erfuellt "
        "(keine vertragliche Stelle, mehrkantonal)"
    )
    reference = "SR 821.421 Art. 1 Abs. 1-3"

    def formula(person, period, parameters):
        mehrkantonal = person('kollektivstreitigkeit_mehrkantonal', period)
        keine_vertragliche = not_(person('vertragliche_einigungsstelle_vorhanden', period))
        return mehrkantonal * keine_vertragliche
